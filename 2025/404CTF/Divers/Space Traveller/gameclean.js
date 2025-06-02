import { jsx, jsxs } from "react/jsx-runtime";
import { useEffect, useState } from "react";
import { io } from "socket.io-client";

const socket = io(); // Connects to server
const Asteroid = ({ position }) => (
    <img
      src="/images/asteroid.png"
      alt="asteroid"
      className="asteroid"
      style={{ left: position.x, top: position.y }}
      draggable={false}
    />
);

const Player = ({ position, size }) => (
<img
    src="/images/player.png"
    alt="player"
    className="player"
    style={{
    left: position.x,
    top: position.y,
    width: `${size.width}px`,
    height: `${size.height}px`
    }}
    draggable={false}
/>
);

const clamp = (value, min, max) => Math.min(Math.max(value, min), max);

const PLAYER_SIZE = { width: 49, height: 40 };
const ASTEROID_SIZE = { width: 55, height: 48 };


// 4. Main Game Component
const Game = ({ eventTarget, sendPacket, sendPacketWithData }) => {
    const [playerPos, setPlayerPos] = useState({ x: 50, y: 200 });
    const [asteroids, setAsteroids] = useState([]);
    const [waves, setWaves] = useState([]);
    const [isGameOver, setGameOver] = useState(false);
    const [score, setScore] = useState(0);
    const [gameStarted, setGameStarted] = useState(false);
    const [flag, setFlag] = useState("");
  
    const moveUp = () => {
      setPlayerPos(pos => ({ ...pos, y: clamp(pos.y - 20, 0, 560) }));
    };
  
    const moveDown = () => {
      setPlayerPos(pos => ({ ...pos, y: clamp(pos.y + 20, 0, 560) }));
    };
  
    const checkCollision = () => {
      const px = playerPos.x, py = playerPos.y;
      asteroids.forEach(({ x, y }) => {
        const hitX = x < px + PLAYER_SIZE.width && x + ASTEROID_SIZE.width > px;
        const hitY = y < py + PLAYER_SIZE.height && y + ASTEROID_SIZE.height > py;
        if (hitX && hitY) endGame(true);
      });
    };
  
    const endGame = (sendEvent) => {
      if (sendEvent && !isGameOver) sendPacket("game_over");
      setGameOver(true);
      setGameStarted(false);
    };
  
    const handleKeyDown = e => {
      if (!gameStarted) return;
      if (e.key === "z") moveUp();
      if (e.key === "s") moveDown();
    };
  
    const onNewWave = e => {
      const spawns = e.detail.spawns.map(s => ({ x: 400, y: s.y, speed: s.speed }));
      setAsteroids(prev => [...prev, ...spawns]);
      setWaves(prev => [
        ...prev,
        {
          x: 400,
          index: e.detail.i,
          speed: e.detail.spawns[0].speed,
          completed: false
        }
      ]);
    };
  
    const onReward = e => {
      setFlag(e.detail.flag);
    };
  
    const updatePositions = () => {
      if (isGameOver || !gameStarted) return;
  
      setAsteroids(prev => prev.map(a => ({ ...a, x: a.x - a.speed })));
      setAsteroids(prev => prev.filter(a => a.x >= -ASTEROID_SIZE.width));
  
      setWaves(prev => prev.map(w => ({ ...w, x: w.x - w.speed })));
      setWaves(prev => prev.filter(w => !w.completed));
    };
  
    const checkWaveCompletion = () => {
      setWaves(prev => {
        return prev.map(w => {
          if (!w.completed && w.x < playerPos.x - PLAYER_SIZE.width / 2 - ASTEROID_SIZE.width / 2) {
            w.completed = true;
            sendPacketWithData("wave_completed", JSON.stringify({
              playerY: playerPos.y,
              waveIndex: w.index
            }));
          }
          return w;
        });
      });
    };
  
    useEffect(() => {
      checkCollision();
    }, [playerPos, asteroids]);
  
    useEffect(() => {
      const interval = setInterval(updatePositions, 30);
      return () => clearInterval(interval);
    }, [isGameOver, gameStarted]);
  
    useEffect(() => {
      checkWaveCompletion();
    }, [waves]);
  
    useEffect(() => {
      if (gameStarted) {
        document.addEventListener("keydown", handleKeyDown);
        return () => document.removeEventListener("keydown", handleKeyDown);
      }
    }, [gameStarted]);
  
    useEffect(() => {
      eventTarget.addEventListener("wave", onNewWave);
      eventTarget.addEventListener("score_up", () => setScore(s => s + 1));
      eventTarget.addEventListener("game_over", () => endGame(false));
      eventTarget.addEventListener("reward", onReward);
    }, []);
  
    const handleClick = () => {
      if (isGameOver) {
        setPlayerPos({ x: 50, y: 200 });
        setAsteroids([]);
        setWaves([]);
        setGameOver(false);
        setGameStarted(true);
        setScore(0);
        sendPacket("game_start");
      } else if (!gameStarted) {
        setGameStarted(true);
        setScore(0);
        sendPacket("game_start");
      }
    };
  
    return (
      <div className={`Game ${isGameOver ? "game-over" : ""}`} onClick={handleClick}>
        <Player position={playerPos} size={PLAYER_SIZE} />
        {asteroids.map((a, i) => <Asteroid position={a} key={i} />)}
  
        <center>
          <div className="score">{score}</div>
          <div className="flag">{flag}</div>
        </center>
  
        {isGameOver && (
          <center>
            <div className="game-over-message">
              Game Over!<br />
              Z to go UP, S to go DOWN<br />
              <p style={{ backgroundColor: "blue", padding: "2px 6px", borderRadius: "5px" }}>
                Click anywhere to Restart
              </p>
            </div>
          </center>
        )}
  
        {!gameStarted && !isGameOver && (
          <center>
            <div className="game-over-message">
              Space Explorer<br />
              Z to go UP, S to go DOWN<br />
              <p style={{ backgroundColor: "blue", padding: "2px 6px", borderRadius: "5px" }}>
                Click anywhere to Start
              </p>
            </div>
          </center>
        )}
      </div>
    );
  };

// 5. Main Entry Point: Initializes Socket and Events
  const GameWrapper = () => {
    const eventTarget = new EventTarget();
  
    useEffect(() => {
      socket.on("message", (...args) => {
        if (!args.length) return;
  
        switch (args.shift()) {
          case "ping":
            socket.send("pong");
            break;
          case "message":
            const msg = JSON.parse(args[0]);
            switch (msg.event) {
              case "new_wave":
                eventTarget.dispatchEvent(new CustomEvent("wave", { detail: msg }));
                break;
              case "game_over":
                eventTarget.dispatchEvent(new CustomEvent("game_over"));
                break;
              case "score_up":
                eventTarget.dispatchEvent(new CustomEvent("score_up"));
                break;
              case "reward":
                eventTarget.dispatchEvent(new CustomEvent("reward", { detail: msg }));
                break;
            }
            break;
        }
      });
  
      return () => socket.off("message");
    }, []);
  
    return (
      <Game
        eventTarget={eventTarget}
        sendPacket={msg => socket.send(msg)}
        sendPacketWithData={(msg, data) => socket.send(msg, data)}
      />
    );
  };
  
  export default GameWrapper;
  


/*
✅ Summary
Feature	Explanation
Z key	Moves the player up
S key	Moves the player down
Asteroids	Spawn at x=400 and move left
Waves	Are sets of asteroids
Collision	Ends the game
Completion	Player avoids all asteroids in a wave
Socket	Handles server events like waves, game over, score, reward
Flag	Sent after enough wavesz
*/
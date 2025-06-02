const io = require("socket.io-client");

const PLAYER_X = 50;
const PLAYER_WIDTH = 49;
const PLAYER_HEIGHT = 40;
const ASTEROID_WIDTH = 55;
const ASTEROID_HEIGHT = 48;
const ASTEROID_START_X = 400;
const TICK_TIME = 0.03;
const CANDIDATE_Ys = Array.from({ length: 57 }, (_, i) => i * 10);
score = 0;

const socket = io("https://space-traveler.404ctf.fr", {
  transports: ["websocket"],
});

function simpleFindSafeY(spawns) {
    // Loop through candidate Y positions
    for (const candidateY of CANDIDATE_Ys) {
      // Check if candidateY collides with any asteroid in spawns
      const collision = spawns.some(({ y: asteroidY }) => {
        // Check vertical overlap
        const playerTop = candidateY;
        const playerBottom = candidateY + PLAYER_HEIGHT;
  
        const asteroidTop = asteroidY;
        const asteroidBottom = asteroidY + ASTEROID_HEIGHT;
  
        // Check if rectangles overlap vertically
        return !(playerBottom <= asteroidTop || playerTop >= asteroidBottom);
      });
  
      // If no collision found, return this candidateY as safe
      if (!collision) {
        return candidateY;
      }
    }
  
    // If no safe position found, just return 0 (or some fallback)
    return 0;
  }

  

// === EVENT HANDLERS ===
socket.on("connect", () => {
  console.log("[*] Connected!");
});

socket.on("disconnect", () => {
  console.log("[!] Disconnected");
});

socket.on("message", (type, data) => {
  try {
    const event = JSON.parse(data);
    const eventType = event.event;

    if (eventType === "init") {
      GAME = true;
      console.log("[*] Game STARTED!");
      socket.emit("message", "game_start");
    }

    if (eventType === "new_wave") 
    {
      const index = event.i;
      const spawns = event.spawns;
      console.log(`[~] New wave ${index} =>`, spawns);
    
      // Preemptively find safe Y
      y = simpleFindSafeY(spawns);
    
      // Send immediate response
      const payload = JSON.stringify({
        playerY: Math.floor(y),
        waveIndex: index,
      });
      socket.emit("message", "wave_completed", payload);
      console.log(`\x1b[36m[→] Preemptive wave ${index} complete at y=${y}\x1b[0m`);
    }

    if (eventType === "score_up") {
      score += 1;
      console.log(`\x1b[32m[+] Score up!: ${score}\x1b[0m`);
    }

    if (eventType === "game_over") {
      console.log("\x1b[31m[!] Game over! Restarting...\x1b[0m");
      restartGame();
    }

    if (eventType === "reward") {
      console.log(`[🏁] FLAG: ${data}`);
    }
  } catch (e) {
    console.log("[x] Failed to parse message:", data, e);
  }
});

// === GAME LOGIC ===
function restartGame() {
  score = 0;
  processedWaves = new Set();
}


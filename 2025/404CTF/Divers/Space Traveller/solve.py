import os
os.environ["SSLKEYLOGFILE"] = "/tmp/sslkeys.log"

import socketio
import time
import json
import threading


# === Constants from game source code ===
PLAYER_X = 50
y = 300
PLAYER_WIDTH = 49
ASTEROID_WIDTH = 55
ASTEROID_START_X = 400
WAVE_COMPLETE_X = PLAYER_X - (PLAYER_WIDTH / 2) - (ASTEROID_WIDTH / 2)  # -2
TICK_TIME = 0.03  # 50ms
pending_spawns = []
GAME = False


# === State ===
waves = {}
processed_waves = set()
score = 0

sio = socketio.Client()




# === EVENTS ===
@sio.event
def connect():
    print("[*] Connected!")


@sio.event
def disconnect():
    GAME = False
    print("[!] Disconnected")

@sio.on("message")
def on_message(type, data):
    global score
    global GAME
        
    try:
        event = json.loads(data)
        event_type = event.get("event")
        if event_type == "init":
            GAME = True
            print("[*] Game STARTED!")
            sio.emit("message", "game_start")
        if event_type == "new_wave":
            index = event["i"]
            spawns = event["spawns"]
            print(f"[~] New wave {index} => {spawns}")
            handle_wave(index, spawns)
        elif event_type == "score_up":
            score += 1
            print(f"\033[92m[+] Score up!: {score}\033[0m")
        elif event_type == "game_over":
            print("\033[91m[!] Game over! Restarting...\033[0m")
            restart_game()
        elif event_type == "reward":
            
            print(f"[🏁] FLAG: {data}")
    except Exception as e:
        print("[x] Failed to parse message:", data, e)



# === GAME LOGIC ===
def restart_game():
    global score, waves, processed_waves, GAME
    score = 0
    waves.clear()
    processed_waves.clear()
    GAME = False
    # sio.emit("message", "game_start")

def find_safe_y(spawns, player_current_y, min_safe_distance=60):
    candidate_ys = list(range(0, 560, 20))
    # Don't include the current spawns for safety calc
    now = time.time()
    active_spawns = [s for s in pending_spawns if s["arrival_time"] > now]

    safe_ys = []

    for y in candidate_ys:
        min_dist = min(abs(y - s["y"]) for s in active_spawns) if active_spawns else float('inf')
        if min_dist >= min_safe_distance:
            safe_ys.append((abs(y - player_current_y), y))

    if safe_ys:
        best_y = min(safe_ys)[1]
    else:
        best_y = min(candidate_ys, key=lambda y: (
            min(abs(y - s["y"]) for s in active_spawns),
            abs(y - player_current_y)
        ))

    return best_y





def handle_wave(index, spawns):
    global y

    # Tag spawns with expected arrival time
    for s in spawns:
        s["arrival_time"] = time.time() + (ASTEROID_START_X / s["speed"]) * TICK_TIME
    pending_spawns.extend(spawns)

    now = time.time()
    pending_spawns[:] = [s for s in pending_spawns if s["arrival_time"] > now]


    speed = spawns[0]["speed"]
    distance_to_travel = ASTEROID_START_X
    time_to_complete = (distance_to_travel / speed) * TICK_TIME  # seconds

    y = find_safe_y(spawns, y)

    def send_wave_completed():
        if index not in processed_waves:
            payload = json.dumps({
                "playerY": int(y),
                "waveIndex": int(index)
            })
            sio.emit("message", "wave_completed", payload)
            print(f"\033[92m[✔] Wave {index} completed at y={y} (after {time_to_complete:.3f}s)\033[0m")
            processed_waves.add(index)

    # Schedule exact time of wave completion
    timer = threading.Timer(time_to_complete, send_wave_completed)
    timer.start()



# === Start game loop ===
if __name__ == "__main__":
    sio.connect("https://space-traveler.404ctf.fr/socket.io", transports=["websocket"])
    try:
        # while True:
        #     time.sleep(1)
        sio.wait()
    except KeyboardInterrupt:
        sio.disconnect()

import asyncio
import websockets
import json
import os

# 儲存玩家寵物狀態
pets = {}

async def handle_client(websocket, path):
    async for message in websocket:
        request = json.loads(message)
        player = request["player"]
        action = request["action"]

        if player not in pets:
            pets[player] = {"hunger": 50, "happiness": 50}

        if action == "feed":
            pets[player]["hunger"] = max(0, pets[player]["hunger"] - 10)
        elif action == "play":
            pets[player]["happiness"] = min(100, pets[player]["happiness"] + 10)

        await websocket.send(json.dumps(pets[player]))

# Render 會提供 PORT 環境變數
port = int(os.environ.get("PORT", 12345))
start_server = websockets.serve(handle_client, "0.0.0.0", port)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event

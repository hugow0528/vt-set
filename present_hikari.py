import keyboard
import requests
import json
import os
import sys
from urllib.parse import quote

# 自動獲取當前資料夾路徑
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
JSON_PATH = os.path.join(BASE_DIR, "script.json")
BASE_URL = "http://127.0.0.1:12393/tts"

def load_script():
    if not os.path.exists(JSON_PATH):
        print(f"Error: {JSON_PATH} not found!")
        return []
    with open(JSON_PATH, 'r', encoding='utf-8') as f:
        return json.load(f)

script_lines = load_script()
current_line = 0

def speak_next():
    global current_line
    if current_line < len(script_lines):
        text = script_lines[current_line]
        print(f"\n[ Hikari Speaking {current_line + 1}/{len(script_lines)} ]")
        print(f"Text: {text}")
        try:
            requests.get(f"{BASE_URL}?text={quote(text)}")
            current_line += 1
        except Exception as e:
            print(f"Connect Error: {e}")
    else:
        print("\n[ Finish ] End of script.")

print("====================================================")
print("   HikariSnowbell Portable Presenter (F9 Mode)   ")
print("====================================================")
print(f" Loaded {len(script_lines)} lines from script.json")
print(" [Press F9]   - Speak Next Line")
print(" [Press ESC]  - Exit Script")
print("====================================================")

keyboard.add_hotkey('f9', speak_next)
keyboard.wait('esc')

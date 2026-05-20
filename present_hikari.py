import os
import sys
import subprocess

# --- Auto install missing tools to USB ---
def ensure_tools():
    try:
        import keyboard
        import requests
    except ImportError:
        print("[INFO] Installing presentation tools to USB...")
        # Path to uv.exe in the same folder
        uv_path = os.path.join(os.getcwd(), "uv.exe")
        subprocess.check_call([uv_path, "pip", "install", "keyboard", "requests"])

ensure_tools()

import keyboard
import requests
from urllib.parse import quote

# Your Speech Script
SPEECH_SCRIPT = [
    "Good morning Principal, teachers, and fellow students.",
    "Today, I would like to talk about the responsible use of Generative AI.",
    "Generative AI tools, such as chatbots and image generators, can help us write and brainstorm.",
    "The key message today is simple: Learn with AI. Think for yourself.",
    "First, Use AI to Support Learning. AI is a learning assistant, not a replacement for your effort.",
    "Second, Be Honest. Follow instructions and acknowledge AI use. This shows academic honesty.",
    "Third, Protect Privacy. Never enter personal data or passwords into AI tools.",
    "Fourth, Check for Accuracy. AI can make mistakes. Always verify output before using it.",
    "Fifth, Think Critically. Ask yourself: Is this answer reasonable? Is it biased?",
    "Sixth, Respect Copyright. Avoid plagiarism and respect the work of original creators.",
    "Seventh, Be Kind and Safe Online. Technology should not be used to hurt others or spread rumors.",
    "Finally, Write Better Prompts. Clearer directions lead to better answers. But our judgment is necessary.",
    "To conclude: AI is a tool, not a replacement for your thinking. Use it ethically.",
    "Students who use AI responsibly will become better thinkers, creators, and problem-solvers.",
    "So once again, remember: Learn with AI. Think for yourself. Thank you."
]

current_line = 0

def speak():
    global current_line
    if current_line < len(SPEECH_SCRIPT):
        text = SPEECH_SCRIPT[current_line]
        print(f"\n[ Hikari Speaking {current_line+1}/{len(SPEECH_SCRIPT)} ]")
        print(f"Content: {text}")
        try:
            requests.get(f"http://127.0.0.1:12393/tts?text={quote(text)}")
            current_line += 1
        except:
            print("[ERROR] VTuber Backend not ready yet!")
    else:
        print("\n[ FINISH ] No more lines.")

print("\n====================================================")
print("   HIKARI SNOWBELL PRESENTATION TOOL (PORTABLE)   ")
print("====================================================")
print(" >> PRESS [F8] TO SPEAK NEXT LINE")
print(" >> PRESS [ESC] TO QUIT")
print("====================================================")

keyboard.add_hotkey('f8', speak)
keyboard.wait('esc')

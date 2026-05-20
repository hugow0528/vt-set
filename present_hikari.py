import keyboard
import requests
import time
from urllib.parse import quote

# VTuber API Endpoint
BASE_URL = "http://127.0.0.1:12393/tts"

# YOUR FULL PRESENTATION SCRIPT
SPEECH_SCRIPT = [
    "Good morning Principal, teachers, and fellow students.",
    "Today, I would like to talk about a topic that is becoming more and more important in our daily learning — the responsible use of Generative AI.",
    "Generative AI tools, such as chatbots and image generators, can help us write, brainstorm, explain difficult ideas, create images, summarize information, and practise different skills.",
    "They are powerful tools. However, like any powerful tool, they must be used wisely, safely, and honestly.",
    "The key message today is simple: Learn with AI. Think for yourself. AI should support our learning, but it should not replace our own thinking.",
    "1. Use AI to Support Learning. First, we should use AI to support learning. AI can be useful when we want to understand a difficult concept, generate ideas, practise questions, or receive feedback on our work.",
    "For example, if you do not understand a programming concept, you may ask AI to explain it in simpler words. If you are writing an essay, you may ask AI to suggest possible arguments or improve the clarity of your sentences.",
    "However, AI should not do all the work for you. If you simply copy and submit AI-generated work, you may finish the task quickly, but you have not really learnt anything. Remember: AI is a learning assistant, not a replacement for your effort.",
    "2. Be Honest. Second, we must be honest. If your teacher allows you to use AI, follow the instructions carefully. If you are required to acknowledge AI use, you should clearly state how you used it.",
    "For example, you may write: I used Generative AI to brainstorm ideas, or, I used AI to check the grammar of my paragraph. This shows academic honesty.",
    "But submitting AI-generated work as if it were completely your own is dishonest. It is similar to asking someone else to complete the assignment for you. Being honest is about building trust and developing good learning habits.",
    "3. Protect Privacy. Third, we must protect privacy. When using AI tools, never enter personal data or confidential information.",
    "This includes your full name, phone number, address, passwords, student information, photos of others, or internal school information.",
    "Sometimes, students may think, I am only asking AI to help me rewrite something. It should be fine. But once information is entered into an online tool, we may not fully control how it is processed or stored. Before using AI, pause and ask: Does this contain personal or confidential information? If yes, do not enter it.",
    "4. Check for Accuracy. Fourth, we need to check for accuracy. AI can sound very confident, but it can still make mistakes. It may give wrong facts, incorrect calculations, fake references, or outdated information.",
    "Do not believe everything just because it sounds professional. A responsible student should always review and verify AI output before using it.",
    "5. Think Critically. Fifth, we should think critically. AI does not truly understand the world in the same way humans do. Sometimes, its answers may be biased, incomplete, or unsuitable for the situation.",
    "Critical thinking is one of the most important skills in the AI era. The goal is not just to get an answer. The goal is to understand, evaluate, and improve the answer.",
    "6. Respect Copyright and Original Work. Sixth, we must respect copyright and original work. AI can generate content quickly, but this does not mean we can use it without thinking about ownership and fairness.",
    "We should avoid plagiarism. We should respect the work of writers, artists, designers, programmers, and other creators. Creativity is also about respecting others and developing our own original ideas.",
    "7. Be Kind and Safe Online. Seventh, we should be kind and safe online. AI must not be used to bully others, create harmful content, spread rumours, cheat, or produce unsafe materials.",
    "A good digital citizen uses technology with respect, kindness, and responsibility. Technology should help us communicate positively.",
    "8. Write Better Prompts, Learn Better. Finally, we should write better prompts. A prompt is the instruction we give to AI. If the prompt is unclear, the answer may also be unclear.",
    "A good prompt includes a clear task, context, and format. Better prompts help us learn better, but our judgement is still necessary.",
    "Closing Reminder. To conclude, let us remember four important points. First, AI is a tool, not a replacement for your thinking. Second, always review before you use. Third, use AI ethically and responsibly. Fourth, when in doubt, ask your teacher.",
    "Generative AI will continue to change the way we learn and work. Students who use AI responsibly will become better thinkers, creators, and problem-solvers.",
    "So once again, remember: Learn with AI. Think for yourself. Thank you."
]

index = 0

def on_press_f8():
    global index
    if index < len(SPEECH_SCRIPT):
        text = SPEECH_SCRIPT[index]
        print(f"[{index+1}/{len(SPEECH_SCRIPT)}] Hikari Speaking: {text[:50]}...")
        try:
            requests.get(f"{BASE_URL}?text={quote(text)}")
            index += 1
        except:
            print("Error: Server not ready yet!")
    else:
        print("Presentation Finished!")

print("========================================")
print(" PRESENTATION HOTKEY SCRIPT LOADED")
print("========================================")
print(" Press F8 to speak the next chunk.")
print(" Press ESC to quit.")
print("========================================")

keyboard.add_hotkey('f8', on_press_f8)
keyboard.wait('esc')
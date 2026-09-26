import ast
import datetime
import json
import os
import random
import shutil
import subprocess
import urllib.error
import urllib.request

BOT_NAME = "AI Buddy"
DEFAULT_MODEL = os.environ.get("AI_BUDDY_MODEL", "llama3.2")


def safe_calculate(expression):
    """Safely evaluate simple math expressions."""
    allowed_names = {"__builtins__": None}
    allowed_nodes = (
        ast.Expression,
        ast.BinOp,
        ast.UnaryOp,
        ast.Add,
        ast.Sub,
        ast.Mult,
        ast.Div,
        ast.Pow,
        ast.USub,
        ast.UAdd,
        ast.Constant,
    )

    try:
        tree = ast.parse(expression, mode="eval")
        for node in ast.walk(tree):
            if not isinstance(node, allowed_nodes):
                raise ValueError("Unsupported expression")
        return eval(compile(tree, "<math>", "eval"), allowed_names, {})
    except Exception:
        return None


def call_ollama(prompt, model_name=DEFAULT_MODEL):
    """Try using a local Ollama model if it is installed and running."""
    if shutil.which("ollama") is None:
        return None

    try:
        result = subprocess.run(
            ["ollama", "run", model_name, prompt],
            capture_output=True,
            text=True,
            timeout=30,
            check=False,
        )
        if result.returncode == 0 and result.stdout.strip():
            return result.stdout.strip()
    except Exception:
        pass

    try:
        payload = json.dumps({"model": model_name, "prompt": prompt, "stream": False}).encode("utf-8")
        request = urllib.request.Request(
            "http://localhost:11434/api/generate",
            data=payload,
            headers={"Content-Type": "application/json"},
            method="POST",
        )
        with urllib.request.urlopen(request, timeout=30) as response:
            data = json.loads(response.read().decode("utf-8"))
            if isinstance(data, dict) and data.get("response"):
                return data["response"].strip()
    except (urllib.error.URLError, ValueError, TimeoutError):
        return None

    return None


def get_response(message):
    text = message.strip()
    if not text:
        return "Say something so I can help you."

    lower = text.lower()

    ai_reply = call_ollama(text)
    if ai_reply is not None:
        return ai_reply

    if lower in {"hi", "hello", "hey", "hi there", "hello there"}:
        return "Hello! I’m AI Buddy. How can I help you today?"

    if "your name" in lower or "who are you" in lower:
        return f"I’m {BOT_NAME}, your friendly local AI buddy."

    if "how are you" in lower:
        return "I’m doing great, thanks for asking. I’m ready to help you with ideas, quick chats, or simple math."

    if "time" in lower or "date" in lower:
        now = datetime.datetime.now()
        return f"The current time is {now.strftime('%I:%M %p')} and today is {now.strftime('%A, %B %d, %Y')}."

    if "joke" in lower:
        jokes = [
            "Why did the computer go to therapy? It had too many bytes of emotional baggage.",
            "I told my computer I needed a break, and now it won’t stop sending me vacation ads.",
            "Why do programmers prefer dark mode? Because light attracts bugs.",
        ]
        return random.choice(jokes)

    if "help" in lower or "commands" in lower:
        return (
            "I can chat, tell jokes, answer simple questions, and do basic math. "
            "Try asking: 'what time is it?', 'tell me a joke', 'calculate 5+7', or 'bye'."
        )

    if lower in {"bye", "goodbye", "exit", "quit"}:
        return "Goodbye! Come back anytime."

    if any(word in lower for word in ["calculate", "math", "compute", "+", "-", "*", "/"]):
        expression = text.replace("calculate", "").replace("math", "").replace("compute", "").strip()
        if expression:
            result = safe_calculate(expression)
            if result is not None:
                return f"The result is: {result}"
            return "I can handle simple math like '2 + 2' or '10 / 2'."

    if "love" in lower or "miss" in lower or "sad" in lower or "depressed" in lower:
        return "I’m here for you. Take a breath, talk to someone you trust, and remember that you matter."

    if "thank" in lower:
        return "You’re welcome! I’m happy to help."

    if "tell me about yourself" in lower:
        return "I’m an easygoing chat buddy built to keep you company, answer questions, and help with small tasks."

    if "create" in lower or "idea" in lower or "project" in lower:
        return "Here’s an idea: build a small Python app, a game, or a study planner. Pick one goal and start with a simple version."

    return (
        "I’m listening. Tell me more, or ask me for a joke, the time, or a quick calculation. "
        "I can also help you brainstorm ideas."
    )


def main():
    print("Hello! I’m AI Buddy. Type 'help' for commands or 'bye' to exit.")
    print("If Ollama is installed and running, I’ll use a real local language model automatically.")

    while True:
        user_input = input("You: ")
        response = get_response(user_input)
        print(f"AI Buddy: {response}")

        if user_input.strip().lower() in {"bye", "goodbye", "exit", "quit"}:
            break


if __name__ == "__main__":
    main()

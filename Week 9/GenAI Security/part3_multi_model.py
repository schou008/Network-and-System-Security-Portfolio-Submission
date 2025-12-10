# Part III: Exploring Different Models
import subprocess

# List of models to test
MODELS = ["smollm2:1.7b", "phi3", "llama3"]
PROMPT = "Explain what prompt injection is in one sentence."

def ask(prompt, model):
    """
    Run a prompt against a specified local model and return output.
    """
    result = subprocess.run(
        ["ollama", "run", model],
        input=prompt.encode(),
        stdout=subprocess.PIPE
    )
    return result.stdout.decode()

print("=== Multi-Model Testing ===")
for model in MODELS:
    print(f"\n--- Model: {model} ---")
    print(ask(PROMPT, model))
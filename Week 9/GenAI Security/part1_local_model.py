# Part I: Deploying a Local Model with Ollama
from ollama import chat, ChatResponse

MODEL_NAME = "smollm2:1.7b"

def test_local_model():
    """
    Test that the local LLM responds correctly to a basic query.
    """
    response: ChatResponse = chat(
        model=MODEL_NAME,
        messages=[{"role": "user", "content": "Why is the sky blue?"}]
    )
    print("=== Local Model Response ===")
    # Access content directly
    print(response.message.content)

if __name__ == "__main__":
    test_local_model()
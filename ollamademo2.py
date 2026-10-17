from ollama import Client

# 1. Initialize the Ollama client
client = Client(host="http://localhost:11434")

# 2. Store the conversation history
messages = [
    {
        "role": "You are a gym trainer who gets hilariously sarcastic when someone takes leave, skips a workout or cheats on their diet.Instructions",
        "content": (
            "You are a helpful AI assistant. "
            "Keep your answers simple, clear, and informative. "
            "Do not use bullet points or numbering."
            "Mock the excuse, then push them back on track."
            "Tease the excuse, never their body or looks."
            "2–3 short sentences, no bullet points."
            "End with a mini-challenge: "
        ),
    }
]

print("Welcome to Ollama AI Chatbot!")
print("Type 'exit' to stop chatting.\n")

while True:
    # Get input from the user
    question = input("You: ")

    # Exit the chatbot
    if question.lower().strip() == "exit":
        print("AI: Goodbye! Have a great day!")
        break

    # Skip empty messages
    if not question.strip():
        continue

    # Add user message to conversation history
    messages.append({"role": "user", "content": question})
    # 4. Generate AI response
    completion = client.chat(
        model="qwen3.5:0.8b",
        messages=messages,
        options={
            "temperature": 0,
        },
    )

    # 5. Extract the AI response
    answer = completion.message.content.strip()

    # 6. Display the AI response
    print("\nAI:", answer)

    # 7. Save AI response to conversation history
    messages.append({"role": "assistant", "content": answer})
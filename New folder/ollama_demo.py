from ollama import Client

# 1. Initialize the Ollama client
client = Client(host="http://localhost:11434")

# 2. Get the question from the user
question = input("User: ")

# 3. Generate a response using Qwen 3.5
completion = client.chat(
    model="qwen3.5:0.8b",
    messages=[
        {
            "role": "system",
            "content": (
                "Keep each sentence simple, clear, and informative. "
                "Do not use bullet points or numbering."
            ),
        },
        {"role": "user", "content": question},
    ],
    options={
        "temperature": 0,
    },
)

# 4. Extract and display the answer
answer = completion.message.content.strip()
print("\nAI:", answer)
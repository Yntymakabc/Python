import openai

client = openai.OpenAI(
    api_key="io-v2-eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJvd25lciI6ImQ2MzE3NDM0LThiMDAtNDNhZC04YzFhLTM3YzhmMjM5NmIyZSIsImV4cCI6NDkwMjEzNjc3MX0.XkLy-o-6RVS9KftqHZ2OnJ3zozDAefhgOMjRf7MjaesIneIUNPrv3CVEolcEw6goWe4XN2QPPX_G6r14bqvP7A",  # Replace with your actual key or use an environment variable
    base_url="https://api.intelligence.io.solutions/api/v1/",
)

user_message = input("You: ")

response = client.chat.completions.create(
    model="deepseek-ai/DeepSeek-R1-Distill-Llama-70B",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": user_message},
    ],
    temperature=0.7,
    stream=False,
    max_completion_tokens=100
)

print("AI:", response.choices[0].message.content)


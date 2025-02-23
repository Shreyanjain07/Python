from openai import OpenAI

client = OpenAI(
    api_key = "Use your api key here"
)

completion = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "system", "content": "You are a virtual assistant named jarvis who performs general tasks asked by the user like alexa and google assistant."},
        {"role": "user", "content": "Explain what is coding"}
    ]
)

print(completion.choices[0].message)

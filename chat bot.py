from google import genai

def get_weather(location: str) -> str:
    return f"The weather in {location} is 22C and sunny."

client = genai.Client()

response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents="What is the weather like in London today?",
    config={"tools": [get_weather]}
)

print(response.text)
from google import genai

# Pass API key directly
client = genai.Client(api_key="")

result = client.models.embed_content(
    model="models/embedding-001",
    content="What is the meaning of life?"

)
print(result["embedding"])

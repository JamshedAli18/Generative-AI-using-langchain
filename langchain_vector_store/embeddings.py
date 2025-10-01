from google import genai

# Pass API key directly
client = genai.Client(api_key="AIzaSyD5TuOW0ShMiyLIwNGX4Afejee7Wc9HO7U")

result = client.models.embed_content(
    model="models/embedding-001",
    content="What is the meaning of life?"

)
print(result["embedding"])

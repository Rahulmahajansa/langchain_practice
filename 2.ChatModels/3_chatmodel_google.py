from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
# Load environment variables from .env file
load_dotenv()
# Initialize the chat model
chat_model = ChatGoogleGenerativeAI(model="gemini-1.5-flash", temperature=0.7)
# Example usage of the chat model
response = chat_model.invoke("What is the capital of France?")
# Output: "The capital of France is Paris."
print("Response from Chat Model:", response.content)

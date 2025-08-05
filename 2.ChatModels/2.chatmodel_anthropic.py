from langchain_anthropic import ChatAnthropic
from dotenv import load_dotenv
# Load environment variables from .env file
load_dotenv()
# Initialize the chat model
chat_model = ChatAnthropic(model="claude-2", temperature=0.7)
# Example usage of the chat model
response = chat_model.invoke("What is the capital of France?")
# Output: "The capital of France is Paris."
print("Response from Chat Model:", response.content)

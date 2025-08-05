from langchain_openai import OpenAI
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()
llm = OpenAI(model="gpt-3.5-turbo", temperature=0.7)
response =llm.invoke("What is the capital of France?")
# Output: "The capital of France is Paris."
print("Response from LLM:", response)
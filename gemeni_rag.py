from langchain_community.document_loaders import TextLoader
from langchain.indexes import VectorstoreIndexCreator
from langchain_text_splitters import CharacterTextSplitter
from langchain_google_genai import GoogleGenerativeAI,GoogleGenerativeAIEmbeddings
import os
from dotenv import load_dotenv
load_dotenv()

llm = GoogleGenerativeAI(model="gemini-1.5-flash", google_api_key=os.getenv("GOOGLE_API_KEY"))

try:
    loader = TextLoader("data.txt")

except  Exception as e:
    print("Error while loading file=", e)

#  Create embeings

embedding = GoogleGenerativeAIEmbeddings(model="models/embedding-001")
#  use a smaller chunk size to manage token limits
text_splitter= CharacterTextSplitter(chunk_size=500, chunk_overlap=100)

# Create the index with the specified embedding and text splitter
index_creator = VectorstoreIndexCreator(
    embedding=embedding,
    text_splitter=text_splitter
) 
index = index_creator.from_loaders([loader])

# Query the index with LLM
while True:
    human_message=input("How i can help you today?")
    response = index.query(human_message, llm=llm)  
    print(response)
from langchain_google_genai import GoogleGenerativeAI
from dotenv import load_dotenv
from langchain.prompts import PromptTemplate
import  os

load_dotenv()
llm = GoogleGenerativeAI(model="gemini-1.5-flash", google_api_key=os.getenv("GOOGLE_API_KEY"))

# prompt = PromptTemplate(tamplate="create stiry of two friends who are going to buy fruits to market? use this characters name {characters}", inputVariable=["characters"])
# response = llm.invoke("create stiry of two friends who are going to buy fruits to market")
prompt = PromptTemplate(
    template="Create a story of two friends who are going to buy fruits at the market. Use these characters' names: {characters}, your respose sould be start from character  after the name add  colon e.g name: ,Repose should be json based ",
    input_variables=["characters"]  # Correct parameter name
)

chain = prompt | llm
response=chain.invoke({"characters":"Farrukh and Ahmad"})
print(response)
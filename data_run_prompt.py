
from langchain_google_genai import GoogleGenerativeAI
from data_prompt import workout_prompt,user_profile,example_generation,final_output,feedback,workout_generation,workout_history



prompt = workout_prompt(user_profile=user_profile, 
                        workout_history=workout_history, 
                        workout_generation=workout_generation,
                        feedback=feedback,
                        example_generation=example_generation,
                        final_output=final_output)



def call_llm(prompt:str) -> str:
    """this function calls the Google Generative AI model to generate a response based on the prompt"""
    llm = GoogleGenerativeAI(model="gemini-1.5-flash", api_key="AIzaSyCTMJ_00Z-oV8c2XMCiyGpybwR-otvsAhU")
    result = llm.invoke(prompt)
    return result


response = call_llm(prompt)

print(response)

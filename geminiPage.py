import google.generativeai as genai
from dotenv import load_dotenv
import os
# Load the .env file 
load_dotenv()

gemini_api = os.getenv("GOOGLE_API_KEY")

genai.configure(api_key=gemini_api)
model = genai.GenerativeModel("gemini-2.0-flash-exp")

text = input("Enter the propt: ")
response = model.generate_content(text)
print(response.text)
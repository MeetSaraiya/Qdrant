from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate

model = OllamaLLM(model="llama3.2")

requirement = "nothing"
content = "nothing"

input_to_go = f"""
        I need to {requirement}. The content provided below is a markdown representation of a website that was scraped. The content contains various sections and information, and I would like you to use it to {requirement}. You can analyze the entire markdown content to extract the relevant data.

        Markdown content:
        {content}

        Please ensure you extract only the information related to {requirement}, and return the result in a clear and organized manner. Your output should strictly adhere only to the requirements specified above.
        And please provide the best accuracy as you can, this is an important task. 
        """
def get_answer_from_ollama(requirement, dom_content,input_1):
    
    return model.invoke(input=input_to_go)

result = model.invoke(input=input_to_go)
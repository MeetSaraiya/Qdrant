import streamlit as st
from scrape import scrape_website,split_dom_content
from chucks import upload_embeddings
from ingest import search_in_qdrant
from llamaPage import get_answer_from_ollama
from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate

model = OllamaLLM(model="llama3.2")

st.title("**Your Scraper**")

url = st.text_input("Insert the URL you want to fetch", "www.example.com")

if st.button("Scrape"):
    dom_content = scrape_website(url)
    if dom_content:
        print("Scraping successful!")
        #uploading text content if it is not empty
        st.session_state.dom_content = dom_content
        upload_embeddings(dom_content)

    with st.expander("**View DOM**"):
        st.text_area("**DOM content**", dom_content, height=400)
    
# requirement = st.text_input("What do you want to extract from the content", "Extract the title")

if "Extract Information" :
    parse_description = st.text_area("Describe what you want to parse")

    if st.button("Parse Content"):
        if parse_description:
            st.write("Parsing the content...")
            answer = search_in_qdrant(parse_description)
           
            input_to_go = f"""
                    I need to {parse_description}. The content provided below is a markdown representation of a website that was scraped. The content contains various sections and information, and I would like you to use it to {parse_description}. You can analyze the entire markdown content to extract the relevant data.

                    Markdown content:
                    {answer}

                    Please ensure you extract only the information related to {parse_description}, and return the result in a clear and organized manner.
                    """


            answer = model.invoke(input=input_to_go)
            st.text_area("**DOM content**", answer, height=800)
           



            # Parse the content with Ollama
            # dom_chunks = split_dom_content(st.session_state.dom_content)
            # parsed_result = parse_with_gemini(st.session_state.dom_content, parse_description)
            # st.write(parsed_result)
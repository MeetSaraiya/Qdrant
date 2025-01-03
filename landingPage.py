import streamlit as st
from scrape import scrape_website
from chucks import upload_embeddings
from ingest import search_in_qdrant
from llamaPage import get_answer_from_ollama
from llamaPage import input_to_go

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
            if answer:
                final_result = get_answer_from_ollama(parse_description, answer,input_1=input_to_go)
                # st.write(final_result)
                with st.expander("**View ANS**"):
                    st.text_area("**DOM content**", final_result, height=800)
            # Parse the content with Ollama
            # dom_chunks = split_dom_content(st.session_state.dom_content)
            # parsed_result = parse_with_gemini(st.session_state.dom_content, parse_description)
            # st.write(parsed_result)
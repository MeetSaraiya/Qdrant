from selenium.webdriver import Remote, ChromeOptions
from selenium.webdriver.chromium.remote_connection import ChromiumRemoteConnection
from bs4 import BeautifulSoup
from dotenv import load_dotenv
import os
import requests
import streamlit as st

load_dotenv()

def scrape_website(website):
    if website:
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:133.0) Gecko/20100101 Firefox/133.0"
        }

        # Send a GET request to the URL with the headers
        response = requests.get("https://r.jina.ai/"+website)
        # st.write(response.text)
        return response.text


# def extract_body_content(html_content):
#     soup = BeautifulSoup(html_content, "html.parser")
#     body_content = soup.body
#     if body_content:
#         return str(body_content)
#     return ""


# def clean_body_content(body_content):
#     soup = BeautifulSoup(body_content, "html.parser")

#     for script_or_style in soup(["script", "style"]):
#         script_or_style.extract()

#     # Get text or further process the content
#     cleaned_content = soup.get_text(separator="\n")
#     cleaned_content = "\n".join(
#         line.strip() for line in cleaned_content.splitlines() if line.strip()
#     )

#     return cleaned_content


def split_dom_content(dom_content, max_length=6000):
    return [
        dom_content[i : i + max_length] for i in range(0, len(dom_content), max_length)
    ]

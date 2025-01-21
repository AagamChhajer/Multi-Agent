import requests
from bs4 import BeautifulSoup
from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain

# Function to extract content from a webpage
def extract_web_content(url):
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Extract headings and paragraphs
        headings = [h.get_text() for h in soup.find_all(['h1', 'h2', 'h3'])]
        paragraphs = [p.get_text() for p in soup.find_all('p')]
        
        content = "\n".join(headings + paragraphs)
        return content
    else:
        return None

# LangChain setup with ChatOpenAI
def summarize_content(content):
    llm = ChatOpenAI(
        model="gpt-4o",
        temperature=0,
        max_tokens=None,
        timeout=None,
        max_retries=2,
    )
    prompt_template = PromptTemplate(
        input_variables=["text"],
        template="Summarize the following content concisely:\n\n{text}"
    )
    chain = LLMChain(llm=llm, prompt=prompt_template)
    
    summary = chain.run(text=content)
    return summary

# Main
if __name__ == "__main__":
    # Example URL
    url = "https://en.wikipedia.org/wiki/Natural_language_processing"
    
    print("Extracting content from the webpage...")
    content = extract_web_content(url)
    
    if content:
        print("Content extracted successfully. Generating summary...\n")
        summary = summarize_content(content)
        print("Summary:\n", summary)
    else:
        print("Failed to extract content. Check the URL or internet connection.")

# import requests
# from bs4 import BeautifulSoup
# from langchain_openai import ChatOpenAI
# from langchain.prompts import PromptTemplate
# from langchain_ollama import ChatOllama
# from langchain_core.prompts import ChatPromptTemplate
# # from langchain.schema import RunnableSequence

# # Function to extract content from a webpage
# def extract_web_content(url):
#     response = requests.get(url)
#     if response.status_code == 200:
#         soup = BeautifulSoup(response.text, 'html.parser')
        
#         # Extract headings and paragraphs
#         headings = [h.get_text() for h in soup.find_all(['h1', 'h2', 'h3'])]
#         paragraphs = [p.get_text() for p in soup.find_all('p')]
        
#         content = "\n".join(headings + paragraphs)
#         return content
#     else:
#         return None

# # LangChain setup with ChatOpenAI
# def summarize_content(content):
#     llm = ChatOpenAI(
#         model="gpt-4o-mini",
#         temperature=0,
#         max_tokens=None,
#         timeout=None,
#         max_retries=2,
#         api_key=...
#     )

#     ollama_llm = ChatOllama(
#     model="phi4:latest",
#     temperature=0,
#     # other params...
# )
#     prompt_template = PromptTemplate(
#         input_variables=["text"],
#         template="Summarize the following content concisely:\n\n{text}"
#     )

#     prompt_template_2 = ChatPromptTemplate.from_messages(
#     [
#         (
#             "system",
#             "You are a helpful assistant that translates content to Hindi and summarizes it concisely.",
#         ),
#         ("human", "Convert the content to Hindi and summarize it in very short:\n\n{text}"),
#     ]
# )

#     # Use RunnableSequence for chaining the prompt and LLM
#     chain = prompt_template | ollama_llm | prompt_template_2 | ollama_llm
    
#     # Use invoke instead of run
#     summary = chain.invoke({"text": content})
#     return summary

# # Main
# if __name__ == "__main__":
#     # Example URL
#     url = "https://en.wikipedia.org/wiki/Natural_language_processing"
    
#     print("Extracting content from the webpage...")
#     content = extract_web_content(url)
    
#     if content:
#         print("Content extracted successfully. Generating summary...\n")
#         summary = summarize_content(content)
#         print("Summary:\n", summary)
#     else:
#         print("Failed to extract content. Check the URL or internet connection.")
import os
import requests
from bs4 import BeautifulSoup
from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain_ollama import ChatOllama
from langchain_core.prompts import ChatPromptTemplate

# Function to extract content from a webpage
def extract_web_content(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raises an HTTPError for bad responses
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Extract headings and paragraphs
        headings = [h.get_text() for h in soup.find_all(['h1', 'h2', 'h3'])]
        paragraphs = [p.get_text() for p in soup.find_all('p')]
        
        content = "\n".join(headings + paragraphs)
        return content
    except requests.RequestException as e:
        print(f"Error fetching URL: {e}")
        return None

# LangChain setup with ChatOpenAI
def summarize_content(content):
    try:
        llm = ChatOpenAI(
            model="gpt-4o-mini",  # Verify the correct model name
            temperature=0,
            max_tokens=None,
            timeout=None,
            max_retries=2,
            api_key= ...
        )

        ollama_llm = ChatOllama(
            model="phi4:latest",
            temperature=0,
            # Include other necessary parameters...
        )

        prompt_template = PromptTemplate(
            input_variables=["text"],
            template="Summarize the following content concisely:\n\n{text}"
        )

        prompt_template_2 = ChatPromptTemplate.from_messages(
            [
                ("system", "You are a helpful assistant that translates content to Hindi and summarizes it concisely."),
                ("human", "Convert the content to Hindi and summarize it in very short:\n\n{text}"),
            ]
        )

        # Create a chain of operations (ensure RunnableSequence is properly used if needed)
        chain = prompt_template | ollama_llm | prompt_template_2 | ollama_llm
        
        summary = chain.invoke({"text": content})
        return summary
    except Exception as e:
        print(f"Error during summarization: {e}")
        return None

# Main execution block
if __name__ == "__main__":
    url = "https://en.wikipedia.org/wiki/Natural_language_processing"
    
    print("Extracting content from the webpage...")
    content = extract_web_content(url)
    
    if content:
        print("Content extracted successfully. Generating summary...\n")
        summary = summarize_content(content)
        
        if summary:
            print("Summary:\n", summary)
        else:
            print("Failed to generate summary.")
    else:
        print("Failed to extract content. Check the URL or internet connection.")


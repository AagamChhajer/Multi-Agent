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

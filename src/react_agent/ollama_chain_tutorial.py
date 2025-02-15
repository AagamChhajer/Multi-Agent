from langchain_core.messages import AIMessage
from langchain_ollama import ChatOllama

llm = ChatOllama(
    # model="phi4",
    model="phi4:latest",
    temperature=0,
    # other params...
)
messages = [
    (
        "system",
        "You are a helpful assistant that translates English to French. Translate the user sentence.",
    ),
    ("human", "I love programming."),
]
ai_msg = llm.invoke(messages)
print(ai_msg.content)

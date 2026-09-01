
from langchain_mistralai import ChatMistralAI
from langchain_core.prompts import ChatPromptTemplate
from dotenv import load_dotenv

load_dotenv()

model = ChatMistralAI(
    model="mistral-small-latest"
)

chat_prompt = ChatPromptTemplate.from_messages([
    (
        "system",
        "You are a helpful AI study assistant. "
        "Explain study topics clearly and simply. "
        "Give clean, well-structured answers."
    ),
    (
        "human",
        "{question}"
    )
])


def ask_ai(question):

    messages = chat_prompt.invoke({
        "question": question
    })

    result = model.invoke(messages)

    return result.content

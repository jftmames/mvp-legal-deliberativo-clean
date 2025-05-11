import os
from dotenv import load_dotenv
load_dotenv()
from langchain.prompts import PromptTemplate
from langchain.schema import HumanMessage
from langchain_community.chat_models import ChatOpenAI

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
modelo = ChatOpenAI(model_name="gpt-3.5-turbo", openai_api_key=OPENAI_API_KEY)

def generar_subpreguntas(pregunta: str, n: int = 3):
    prompt = PromptTemplate(
        input_variables=["pregunta", "n"],
        template="Dada la pregunta '{pregunta}', genera {n} subpreguntas legales."
    )
    human_msg = HumanMessage(content=prompt.format(pregunta=pregunta, n=n))
    resp = modelo.generate([[human_msg]]).generations[0][0].message.content
    return [line.strip("- ").strip() for line in resp.split("\n") if line.strip()]

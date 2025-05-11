import os
from dotenv import load_dotenv
load_dotenv()
from langchain_community.embeddings import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_community.chat_models import ChatOpenAI
from langchain.chains import ConversationalRetrievalChain

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

def build_inquiry_engine(k: int = 2):
    embeddings = OpenAIEmbeddings(openai_api_key=OPENAI_API_KEY)
    vectorstore = FAISS.load_local(
        "data/vectors/faiss_index", embeddings, allow_dangerous_deserialization=True
    )
    retriever = vectorstore.as_retriever(search_kwargs={"k": k})
    llm = ChatOpenAI(model_name="gpt-3.5-turbo", openai_api_key=OPENAI_API_KEY)
    return ConversationalRetrievalChain.from_llm(
        llm=llm, retriever=retriever, return_source_documents=False
    )

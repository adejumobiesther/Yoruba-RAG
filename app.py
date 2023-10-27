from langchain.document_loaders import TextLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.embeddings import SentenceTransformerEmbeddings
from langchain.vectorstores import Chroma
from langchain.chat_models import ChatOpenAI
from langchain.chains.question_answering import load_qa_chain
from langchain.chains import RetrievalQA
import os
import openai

def question_db(query):
    loader = TextLoader('yoruba_rag.txt', encoding="utf-8")
    documents = loader.load()

    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=100, separators=".")
    docs = text_splitter.split_documents(documents)
    embeddings = HuggingFaceEmbeddings(model_name='sentence-transformers/LaBSE')
    db = Chroma.from_documents(docs, embeddings)
    retriever = db.as_retriever()
    docs = retriever.get_relevant_documents(query)
    llm = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0, openai_api_key=openai.api_key)
    qa_chain = load_qa_chain(llm, chain_type="stuff")
    qa = RetrievalQA(combine_documents_chain=qa_chain,
                     retriever=retriever)
    result = qa.run(query)
    return result

if __name__ == "__main__":
    # make a gradio interface
    import gradio as gr

    outputs = gr.outputs.Textbox()

    app = gr.Interface(fn=question_db, inputs='text', outputs=outputs,description="This is a question answering model regarding the yoruba language and culture").launch()

















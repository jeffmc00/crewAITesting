#from langchain_openai import OpenAIEmbeddings
import os
from langchain.embeddings import OpenAIEmbeddings
os.environ["OPENAI_PROXY"] = "http://192.168.0.107:8000"
os.environ["OPENAI_API_KEY"] = ""

embeddings = OpenAIEmbeddings()

text = "This is a test document."

query_result = embeddings.embed_query(text)

query_result[:5]
from langchain_community.embeddings import HuggingFaceInstructEmbeddings

embeddings = HuggingFaceInstructEmbeddings(
    query_instruction="Represent the query for retrieval: "
)



text = "This is a test document."

query_result = embeddings.embed_query(text)
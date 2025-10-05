import os
import pprint

from dotenv import load_dotenv
import langchain_experimental.text_splitter
from langchain_huggingface import HuggingFaceEndpointEmbeddings

# Load token from .env
load_dotenv()
hf_token = os.getenv("HUGGINGFACEHUB_API_TOKEN")

# Use Hugging Face Inference API
embeddings = HuggingFaceEndpointEmbeddings(
    model="sentence-transformers/all-MiniLM-L6-v2",
    huggingfacehub_api_token=hf_token
)

text_splitter = langchain_experimental.text_splitter.SemanticChunker(
    embeddings,breakpoint_threshold_type="standard_deviation",
    breakpoint_threshold_amount=1
)



sample = """
 Farmers were working hard in the fields, preparing the soil and planting seeds for the next season. The sun was bright, and the air smelled of earth and fresh grass. The Indian Premier League (IPL) is the biggest cricket league in the world. People all over the world watch the matches and cheer for their favourite teams.
 
 
Terrorism is a big danger to peace and safety. It causes harm to people and creates fear in cities and villages. When such attacks happen, they leave behind pain and sadness. To fight terrorism, we need strong laws, alert security forces, and support from people who care about peace and safety."""
docs = text_splitter.create_documents([sample])

pprint.pprint(docs,width=200)






# from langchain_experimental.text_splitter import SemanticChunker
# from langchain_openai.embeddings import OpenAIEmbeddings
# from dotenv import load_dotenv
#
# load_dotenv()
#
# text_splitter = SemanticChunker(
#     OpenAIEmbeddings(), breakpoint_threshold_type="standard_deviation",
#     breakpoint_threshold_amount=3
# )
#
# sample = """
# Farmers were working hard in the fields, preparing the soil and planting seeds for the next season. The sun was bright, and the air smelled of earth and fresh grass. The Indian Premier League (IPL) is the biggest cricket league in the world. People all over the world watch the matches and cheer for their favourite teams.
#
#
# Terrorism is a big danger to peace and safety. It causes harm to people and creates fear in cities and villages. When such attacks happen, they leave behind pain and sadness. To fight terrorism, we need strong laws, alert security forces, and support from people who care about peace and safety.
# """
#
# docs = text_splitter.create_documents([sample])
# print(len(docs))
# print(docs)
#

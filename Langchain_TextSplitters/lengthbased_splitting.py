from langchain.text_splitter import CharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader
import pprint

loader = PyPDFLoader('dl-curriculum.pdf')

docs = loader.load()

spilter = CharacterTextSplitter(
    chunk_size=300,
    chunk_overlap=0
)

result = spilter.split_documents(docs)

pprint.pprint(result,width=120)

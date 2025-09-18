from langchain_community.document_loaders import WebBaseLoader
from sqlalchemy.orm import lazyload

api = 'https://en.wikipedia.org/wiki/Lists_of_rivers'

loader = WebBaseLoader(api)
docs = loader.load()
print(docs[0].page_content)

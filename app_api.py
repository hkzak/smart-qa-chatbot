from fastapi import FastAPI
from haystack.document_stores.faiss import FAISSDocumentStore
from pydantic import BaseModel

from haystack.utils import convert_files_to_dicts, fetch_archive_from_http, clean_wiki_text
from haystack.nodes import Seq2SeqGenerator
from haystack.nodes import EmbeddingRetriever

from haystack.nodes import EmbeddingRetriever

document_store = FAISSDocumentStore.load("haystack_test_faiss")

retriever = EmbeddingRetriever(document_store=document_store,
                                   embedding_model="yjernite/retribert-base-uncased",
                                   model_format="retribert")

generator = Seq2SeqGenerator(model_name_or_path="yjernite/bart_eli5")


class Item(BaseModel):
    query: str


app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Chatbot application is up and running!"}

@app.post("/askQuestion/")
async def create_item(item: Item):
    query = item.query
    from haystack.pipelines import GenerativeQAPipeline
    pipe = GenerativeQAPipeline(generator, retriever)

    result = pipe.run(query=query, params={"Retriever": {"top_k": 1}})
    print(f"Answer: {result['answers'][0]}")

    return {"Answer": result['answers'][0]}
 
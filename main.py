import logging
from fastapi import FastAPI
import inngest
import inngest.fast_api
from dotenv import load_dotenv
import uuid
import os
import datetime
from custom_types import RAQQueryResult, RAGSearchResult, RAGChunkAndSrc, RAGUpsertResults
from dataclasses import load_and_chunk_pdf, embed_texts
from vector_db import QdrantStorage
from sqlalchemy.ext import serializer

load_dotenv()

inngest_client = inngest.Inngest(
    app_id='rag_app',
    logger= logging.getLogger("uvicorn"),
    is_production= False,
    serializer = inngest.PydanticSerializer()
)

@inngest_client.create_function(
    fn_id="RAG: Ingest PDF",
    trigger=inngest.TriggerEvent(event="rag/ingest_pdf")
)

async def rag_ingest_pdf(ctx: inngest.Context):
    def _load(ctx: inngest.Context) -> RAGChunkAndSrc:
        pass

    def _upsert(chunks_and_src: RAGChunkAndSrc) -> RAGUpsertResults:
        pass
app = FastAPI()

inngest.fast_api.serve(app, inngest_client, functions=[rag_ingest_pdf])
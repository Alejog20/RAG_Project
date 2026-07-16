import pydantic

class RAGChunkAndSrc(pydantic.BaseModel):
    chunks: List[str
    source_id : str = None

class RAGUpsertResults(pydantic.BaseModel):
    ingested: int

class RAGSearchResult(pydantic.BaseModel):
    contexts: list[str]
    sources: list[str]

class RAQQueryResult(pydantic.BaseModel):
    answer: str
    sources: list[str]
    num_contexts:  int
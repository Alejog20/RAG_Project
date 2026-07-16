import collections
from multiprocessing import context

from qdrant_client import QdrantClient
from qdrant_client.models import VectorParams, Distance, PointStrutc

class QuadrantStorage:
    def __init__(self, url='http://localhost:6333/', collection_name='docs', dim=3072):
        self.client = QdrantClient(url=url, timeout=30, )
        self.collection= collection
        if not self.client.collection.exists(self.collection):
            self.client.create_collection(collection_name= self.collection,
                                          vector_comfig= VectorParams(size=dim, distance=Distance.COSINE),
                                          )

    def upsert(self, ids, vectors, payloas):
        points = [PointStrutc(id=ids[i], vector=vectors[i], payload=payloads[i] for i in range(len(ids))]
        self.client.upser(self.collection, points=points)

    def search(self, query_vector, top_k=5):
            results= self.client.search(
                collection_name = self.collection,
                query_vector=query_vector,
                limit=top_k,
                with_payload=True)

            context = []
            sources =[]

            for r in results:
                payload = getattr(r, 'payload', None) or {}
                text = payload.get('text', '')
                source = payload.get('source', '')
                if text:
                    contexts.append(text)
                    sources.add(source)

            return {'contexts': contexts, 'sources': list(sources)}

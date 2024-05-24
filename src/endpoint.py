from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Dict

import sys
sys.path.append('')

from src.backend.SQL_bd import PostGresDB
from src.backend.llms_to_search import LLM_Searcher

app = FastAPI()

# Configuração do CORS para permitir todos os domínios
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Permite todos os domínios
    allow_credentials=True,
    allow_methods=["*"],  # Permite todos os métodos (GET, POST, etc.)
    allow_headers=["*"],  # Permite todos os cabeçalhos
)

llm_searcher = LLM_Searcher()
bd_sql = PostGresDB()

# Request model for /search endpoint
class SearchRequest(BaseModel):
    query: str

# Request model for /get_tags endpoint
class GetTagsRequest(BaseModel):
    id: str

@app.post("/search")
def search(search_request: SearchRequest) -> Dict[str, float]:
    query = search_request.query
    results = llm_searcher.run_query(query)
    return results

@app.get("/get_all_resources")
def get_all_resources():
    bd_sql.connect()
    data = bd_sql.get_resource_data()
    print(data)
    bd_sql.close()
    return [{'id': x[1], 'title': x[3], 'tags': x[2]} for x in data]
    
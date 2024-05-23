import os
from dotenv import load_dotenv
from langchain_openai import AzureOpenAIEmbeddings, OpenAIEmbeddings

class Embedding:
    """Wrapper class for embedding model"""
    def __init__(self):
        load_dotenv()
        self._embedding = None
        
    @property
    def azure_openai(self):
        azure_endpoint = os.getenv('ENDPOINT')
        azure_embedding = os.getenv('EMBEDDING')
        azure_openai_key = os.getenv('OPENAI_KEY')
        
        assert azure_endpoint is not None, "Azure endpoint not provided."
        assert azure_embedding is not None, "Azure embedding text-embedding-ada-002 not provided."
        assert azure_openai_key is not None, "Azure OpenAI key not provided."
        
        if self._embedding is None:
            self._embedding = AzureOpenAIEmbeddings(
                azure_endpoint=azure_endpoint,
                azure_deployment=azure_embedding,
                api_key=azure_openai_key
            )
        return self._embedding
    
    @property
    def openai(self, model='text-embedding-ada-002'):
        openai_key = os.getenv('OPENAI_KEY')
        
        assert openai_key is not None, "OpenAI key not provided."
        
        if self._embedding is None:
            self._embedding = OpenAIEmbeddings(
                api_key=openai_key,
                model=model
            )
        return self._embedding
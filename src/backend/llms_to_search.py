import sys
sys.path.append('')
from src.backend.embeddings.embed_datasets import DatasetEmbedding

class LLM_Searcher:

    def __init__(self):
        self.embed_DB = DatasetEmbedding()
        
    def run_query(self, query: str):
        # if self._checker(query) == 'NO':
        #     return "No relevance"
        dataset_dict = {}
        list_similar = self.embed_DB.get_similar(query, k=100)
        print(list_similar)
        for similar in list_similar:
            filename = similar[0].metadata['vc_id']
            if filename in dataset_dict:
                if similar[1] < dataset_dict[filename]:
                    dataset_dict[filename] = similar[1]
            else:
                dataset_dict[filename] = similar[1]                
        
        return dataset_dict
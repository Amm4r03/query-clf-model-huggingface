class EnsembleModel():
    def __init__(self, models : list):
        self.models = models
    
    def predict(self, query : str, verbose : bool = False) -> str :
        # if isinstance(query, str):
        #     query = [query]
        res = []
        if verbose:
            print("currently available models : ", self.models)
        for model in self.models:
            prediction = model.predict(query)
            if verbose:
                print(prediction)
            res.append(prediction[0])
        
        if verbose:
            print(res.count("RAG"))
            print(res.count("SQL"))
            print(res.count(0), res.count(1))
        
        if res.count("RAG") == 0 and res.count("SQL") == 0:
            return "RAG" if res.count(1) > res.count(0) else "SQL"
        return "RAG" if res.count("RAG") > res.count("SQL") else "SQL"

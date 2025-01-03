# imports for running the model
from sklearn.svm import SVC
from sklearn.linear_model import LogisticRegression
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics import classification_report

# custom import
from ensembleModel import EnsembleModel

# imports for running model
import joblib
import os

def get_file_names(path : str, verbose : bool = False) -> list[str]:
    files = os.listdir(path)
    if verbose:
        print(files)
    return files

def load_models(filepath : str, verbose : bool = False) -> list :
    models_list = get_file_names(filepath)
    loaded_models = []
    for m in models_list:
        # loaded_models.append(joblib.load(f"{filepath}\\{m}"))
        # trying new method to allow running on any OS
        loaded_models.append(joblib.load(os.path.join(filepath, m)))
    print(f"successfully loaded a total of {len(models_list)} models")
    if verbose:
        print(loaded_models)
    return loaded_models

import streamlit as sl
from classification_model import load_models
from ensembleModel import EnsembleModel

clf = EnsembleModel(load_models("models", False))

sl.title("Query Classifier")
sl.write("classifies a query as either an SQL based or a RAG based query")
user_query = sl.text_input("Enter your Query : ")
if user_query:
    pred_label = clf.predict([user_query])
    sl.write(f"Predicted label {pred_label}")
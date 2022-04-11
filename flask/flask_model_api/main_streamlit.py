from copyreg import pickle
from flask import Flask, request
import streamlit as st
import pickle
from sklearn.linear_model import LogisticRegression

pickled_model_file = open("pickle_iris_model.pkl", "rb")
classifier = pickle.load(pickled_model_file)

def predict_flower():

    try :
        st.title("Model Deployment")
        sw = st.text_input("Sepal_width")
        sl = st.text_input("Sepal_length")
        pw = st.text_input("Petal_width")
        pl = st.text_input("Petal_length")


        result = classifier.predict([[sw,sl,pw,pl]])
        
        if st.button("Print output"):
            st.success(result)
    except Exception as e :
        return f" Error occuredd with message : {e}"

if __name__=="__main__":
    predict_flower()
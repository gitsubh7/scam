import numpy as np
import pickle
import pandas as pd
import streamlit as st
from PIL import Image

pickle_in = open("classifier.pkl","rb")
classifier=pickle.load(pickle_in)


def welcome():
    return "Welcome HABABY"


def predict_note_authentication(variance,skewness,curtosis,entropy):
    prediction=classifier.predict([[variance,skewness,curtosis,entropy]])
    print(prediction)
    return prediction


def main():
    st.title("HABABY AUTHENTICATION")
    html_temp = """
    <div style="background-color:tomato;padding:10px">
    <h2 style="color:white;text-align:center;">Streamlit Bank Authenticator ML App </h2>
    </div>
    """
    st.markdown(html_temp,unsafe_allow_html=True)
    variance=st.text_input("VARIANCE","hababy type kro")
    skewness=st.text_input("skewness","hababy type kro")
    curtosis=st.text_input("curtosis","hababy type kro")
    entropy=st.text_input("entropy","hababy type kro")
    result=""
    if st.button("PREDICT"):
        result=predict_note_authentication(variance,skewness,curtosis,entropy)
    st.success("THE OUTPUT IS {}".format(result))






if __name__=='main':
    main()
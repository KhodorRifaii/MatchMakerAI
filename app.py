import streamlit as st
import pickle
import pandas as pd


with open("matchmaker_model.pkl", "rb") as f:
    model = pickle.load(f)

st.set_page_config(page_title="MatchMakerAI", page_icon="❤️")

st.title("❤️ MatchMakerAI")
st.write("Predict relationship status from profile information")

essay = st.text_area("Profile Essay", height=200)
age = st.slider("Age", 18, 70, 25)

if st.button("Predict"):
    input_df = pd.DataFrame({
        "essay": [essay],
        "age": [age]
    })

    prediction = model.predict(input_df)[0]
    probability = model.predict_proba(input_df).max()

    if prediction == "single":
        st.success(f"💙 Prediction: SINGLE ({probability:.2%})")
    else:
        st.error(f"❤️ Prediction: NOT SINGLE ({probability:.2%})")

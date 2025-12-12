import streamlit as st
import joblib
import pandas as pd


model = joblib.load("matchmaker_model.pkl")

st.set_page_config(page_title="MatchMakerAI", page_icon="❤️")

st.title("❤️ MatchMakerAI")
st.write("Predict relationship status from profile information")

essay = st.text_area("Profile Essay", height=200)
age = st.slider("Age", 18, 70, 25)
height = st.slider("Height (cm)", 140, 210, 170)

if st.button("Predict"):
    input_df = pd.DataFrame({
        "essays": [essay],
        "age": [age],
        "height": [height]
    })

    prediction = model.predict(input_df)[0]
    probability = model.predict_proba(input_df).max()

    if prediction == "single":
        st.success(f"💙 Prediction: SINGLE ({probability:.2%})")
    else:
        st.error(f"❤️ Prediction: NOT SINGLE ({probability:.2%})")

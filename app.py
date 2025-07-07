
import streamlit as st
import pickle
import pandas as pd

st.title("Football Match Predictor")

teams = ["Arsenal", "Chelsea", "Liverpool", "Manchester City", "Manchester United", "Tottenham"]
home_team = st.selectbox("Home Team", teams)
away_team = st.selectbox("Away Team", [t for t in teams if t != home_team])

if st.button("Predict Result"):
    import random
    prediction = random.choice(["Home Win", "Draw", "Away Win"])
    st.success(f"Predicted Result: {prediction}")

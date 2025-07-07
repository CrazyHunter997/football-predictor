import streamlit as st
import pickle

teams = ["Arsenal", "Chelsea", "Liverpool", "Man City", "Man United", "Spurs"]

with open("model.pkl", "rb") as f:
    model = pickle.load(f)

st.title("⚽ Football Predictor")
st.subheader("Premier League - Wersja 1")

team_1 = st.selectbox("Wybierz Drużynę Gospodarzy", teams)
team_2 = st.selectbox("Wybierz Drużynę Gości", [t for t in teams if t != team_1])

if st.button("🔮 Przewiduj wynik"):
    team_1_id = teams.index(team_1)
    team_2_id = teams.index(team_2)

    prediction = model.predict([[team_1_id, team_2_id]])[0]

    if prediction == 1:
        st.success(f"🏆 {team_1} wygra mecz!")
    elif prediction == -1:
        st.success(f"🏆 {team_2} wygra mecz!")
    else:
        st.info("🤝 Przewidywany remis")

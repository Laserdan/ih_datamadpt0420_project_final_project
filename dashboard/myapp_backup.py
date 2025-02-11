import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from joblib import load
test=1
st.write("""
# Predicting CS:GO FTW

""")

team_dict = {'Counter-Terrorists': 1, 'Terrorists': 0}
yes_no_dict = {'YES': 1, 'NO': 0}
round_type_dic = {'PISTOL_ROUND': 0, 'ECO': 1, 'MEDIUM': 2, 'FULL': 3}
round_type_dic_decode = {0: 'PISTOL_ROUND', 1: 'ECO', 2: 'MEDIUM', 3: 'FULL'}

map_played = st.selectbox('Select Map', ('de_cache', 'de_dust2', 'de_inferno', 'de_mirage', 'de_nuke', 'de_overpass', 'de_train'))

team = st.selectbox('Select your team', ('Counter-Terrorists', 'Terrorists'))

def user_input_features():
    col1, col2 = st.beta_columns(2)

    round = col1.number_input('Round', value=1)
    winner = team_dict[col1.selectbox('Who win the round?', ('Counter-Terrorists', 'Terrorists'))]
    bomb_planted = yes_no_dict[col1.selectbox('Was the bomb planted?', ('YES', 'NO'))]
    round_type = round_type_dic[col1.selectbox('Select enemy\'s round type', ('PISTOL_ROUND', 'ECO', 'MEDIUM', 'FULL'))]


    ct_alive = col2.number_input('CT players alive previous round', value=0, min_value=0, max_value=5)
    t_alive = col2.number_input('T players alive previous round', value=0, min_value=0, max_value=5)
    ct_cons_wins = col2.number_input('CT consecutive wins', value=0, min_value=0)
    t_cons_wins = col2.number_input('T consecutive wins', value=0, min_value=0)

    data = {'file': 0,
            'round': round,
            'ct_alive': ct_alive,
            't_alive': t_alive,
            'ct_winner': winner,
            'bomb_planted': bomb_planted,
            'ct_cons_wins': ct_cons_wins,
            't_cons_wins': t_cons_wins,
            'round_type': round_type,
            'de_cache': 0, 'de_cbble': 0, 'de_dust2': 0, 'de_inferno': 0,
            'de_mirage': 0, 'de_nuke': 0, 'de_overpass': 0, 'de_train': 0}
    features = pd.DataFrame(data, index=[0])
    return features

input_df = user_input_features()
input_df.loc[0, map_played] = 1

if team == 'Counter-Terrorists':
    enemy_team = 'Terrorist'
    model = load('../models/db_t_nxt_rnd_type.joblib')
elif team == 'Terrorists':
    enemy_team = 'Counter-Terrorist'
    model = load('../models/db_ct_nxt_rnd_type.joblib')

prediction_encoded = model.predict(input_df)[0]
pred_proba = model.predict_proba(input_df)[0][:-1]
pred_proba_df = pd.DataFrame(pred_proba).T
pred_proba_df.columns = ['PISTOL_ROUND', 'ECO', 'MEDIUM', 'FULL']

st.write(f'Next round type of {enemy_team} team will be...')

st.write(round_type_dic_decode[prediction_encoded])
st.bar_chart(pred_proba_df.iloc[0])








# st.markdown( <style>round_type_dic_decode[prediction_encoded] {text-align: center;}</style>, unsafe_allow_html=True)

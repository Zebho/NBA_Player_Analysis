import streamlit as st
import requests

st.markdown('''
NBA Prediction
''')

'''
Here's a machine learning model that predicts whether a player will still be around in the next 5 years. Please enter the following player characteristics:
- GP : Games Played
- MIN : MinutesPlayed
- PTS : PointsPerGame
- FGM : FieldGoalsMade
- FGA : FieldGoalAttempts
- FG% : FieldGoalPercent
- 3P Made : 3PointMade
- ЗРА : 3PointAttempts
- 3Р% : 3PointAttempts
- FTM : FreeThrowMade
- FTA : FreeThrowAttempts
- FT% : FreeThrowPercent
- OREB : OffensiveRebounds
- DREB : DefensiveRebounds
- REB : Rebounds
- AST : Assists
- STL : Steals
- BLK : Blocks
- TOV : Turnovers
'''
#All our inputs from the user searching the nba result
GP = st.number_input("Insert a GP", value=0.5, placeholder="GP...")
MIN = st.number_input("Insert a MIN", value=0.5, placeholder="MIN...")
PTS = st.number_input("Insert a PTS", value=0.5, placeholder="PTS...")
FGM = st.number_input("Insert a FGM", value=0.5, placeholder="FGM...")
FGA = st.number_input("Insert a FGA", value=0.5, placeholder="FGA...")
FGp = st.number_input("Insert a FG%", value=0.5, placeholder="FG%...")
troisP_Made = st.number_input("Insert a 3P_Made", value=0.5, placeholder="3P_Made...")
troisPA = st.number_input("Insert a 3PA", value=0.5, placeholder="3PA...")
troisPp = st.number_input("Insert a 3P%", value=0.5, placeholder="3P%...")
FTM = st.number_input("Insert a FTM", value=0.5, placeholder="FTM...")
FTA = st.number_input("Insert a FTA", value=0.5, placeholder="FTA...")
FTp = st.number_input("Insert a FT%", value=0.5, placeholder="FT%...")
OREB = st.number_input("Insert a OREB", value=0.5, placeholder="OREB...")
DREB = st.number_input("Insert a DREB", value=0.5, placeholder="DREB...")
REB = st.number_input("Insert a REB", value=0.5, placeholder="REB...")
AST = st.number_input("Insert a AST", value=0.5, placeholder="AST...")
STL = st.number_input("Insert a STL", value=0.5, placeholder="STL...")
BLK = st.number_input("Insert a BLK", value=0.5, placeholder="BLK...")
TOV = st.number_input("Insert a TOV", value=0.5, placeholder="TOV...")

## Once we have these, let's call our API in order to retrieve a prediction for the nba
url = 'https://nba-prediction-mp-data-t4wdntazfq-ew.a.run.app/prediction'

params_player = {'GP': GP,
          'MIN'        : MIN,
    'PTS'        : PTS,
    'FGM'        : FGM,
    'FGA'        : FGA,
    'FGp'        : FGp,
    'troisPM'    : troisP_Made,
    'troisPA'        : troisPA,
    'troisPp'        : troisPp,
    'FTM'        : FTM,
    'FTA'        : FTA,
    'FTp'        : FTp,
    'OREB'       : OREB,
    'DREB'       : DREB,
    'REB'        : REB,
    'AST'        : AST,
    'STL'        : STL,
    'BLK'        : BLK,
    'TOV'        : TOV}

#We ask the API to use the model
response = requests.get(url,
    params=params_player,
).json()

if response['Prédiction'] == 1 :
    st.markdown('''
    Ce joueur de NBA a du talent, et il faut le garder !
    ''')
else :
    st.markdown('''
    Ce joueur de NBA risque de ne pas jouer plus de 5 ans.
    ''')

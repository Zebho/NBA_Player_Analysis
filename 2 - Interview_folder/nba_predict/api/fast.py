import pandas as pd
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import MinMaxScaler
from pickle import load

from nba_predict.api.test_precision import custom_predict

app = FastAPI()

app.state.model = load(open('nba_predict/model_reglog_opti.pkl', 'rb'))
app.state.scaler = load(open('nba_predict/scaler_opti.pkl', 'rb'))


# Allowing all middleware is optional, but good practice for dev purposes
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)

@app.get("/prediction") # Je donne en valeur d'entrée un joueur au hasard
def predict(
        GP   = 0.563380,
        MIN  = 0.092593,
        PTS  = 0.065455,
        FGM  = 0.070707,
        FGA  = 0.063158,
        FGp  = 0.545090,
        troisPM = 0.000000,
        troisPA  = 0.000000,
        troisPp  = 0.500000,
        FTM  = 0.051948,
        FTA  = 0.049020,
        FTp  = 0.714000,
        OREB = 0.150943,
        DREB = 0.095745,
        REB  = 0.117647,
        AST  = 0.028302,
        STL  = 0.080000,
        BLK  = 0.076923,
        TOV  = 0.093023,
        ):
    """
    Input : l'ensemble des valeurs nécessaire à la prédiction d'un joueur
    OutPut : la prédiction (O ou 1) si le joueur est intéressant sur les 5 ans ou non
    """
    #Transforation en DF des valeurs en entrée
    X_pred = pd.DataFrame(dict(locals(), index=[0])).set_index('index')

    #Modification des colonnes afin d'avoir les même noms que les colonnes du modèle
    X_pred.columns = ['GP', 'MIN', 'PTS', 'FGM', 'FGA', 'FG%', '3P Made', '3PA', '3P%', 'FTM','FTA', 'FT%', 'OREB', 'DREB', 'REB', 'AST', 'STL', 'BLK', 'TOV']

    #Tests si le modèle et le scaler ont bien été chargés
    assert app.state.model is not None
    assert app.state.scaler is not None

    #On preprocesse les valeurs du joueur à l'aide du scaler ayant servi à transformer l'ensemble du dataset
    X_processed = app.state.scaler.transform(X_pred)
    X_processed = pd.DataFrame(X_processed, columns=X_pred.columns)
    #On prédit si le joueur est intéressant dans les 5 ans, avec la précision à 90%
    y_pred = custom_predict(X_processed,app.state.model)
    return {'Prédiction' : int(y_pred) }


@app.get("/")
def root(): #Valeur de la racine pour valider le fonctionnement de l'API
    return{'greeting': 'Helloworld'}

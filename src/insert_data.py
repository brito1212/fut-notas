import pandas as pd
import psycopg2 as psy
from model import Jogador
from app_settings import app, db

app.app_context()

def insert_csv(path):
    data = pd.read_csv(path, encoding='latin-1')
    jogadores = data.to_dict("records")
    for jogador in jogadores:
        jogador_insert = Jogador(**jogador)
        jogador_insert.calcular_nota()
        db.session.add(jogador_insert)
        db.session.commit()

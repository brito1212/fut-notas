import pandas as pd
import psycopg2 as psy

def insert_csv(path):
    data = pd.read_csv(path, encoding='latin-1')
    
    conn = psy.connect(database = "Futnotas", host = "localhost", user = "postgres", password = "1234", port = "5432")
    cur = conn.cursor()
    if(conn.status==1):
        for index, row in data.iterrows():
            if(index!=0):
                cur.execute("""
                            INSERT INTO Jogadores 
                            (nome, clube, rodada, gols, assists, passescertos, passeserrados, passesimportantes, 
                            chutesnogol, chutesprafora, chutesbloqueados, driblescertos, dribleserrados, driblessofridos, 
                            duelosganhos, duelosperdidos, posseperdida, faltascometidas, faltassofridas, interceptacoes, 
                            desarmes, nota) 
                            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
                            """,tuple(row[0].split(';')))
        conn.commit()
        cur.close()
        conn.close()
        return True
    
insert_csv(r'c:\Users\Felipe\Downloads\dados.csv')
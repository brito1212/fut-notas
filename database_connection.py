import psycopg2 as psy

def init():
    conn = psy.connect(database = "Futnotas", host = "localhost", user = "postgres", password = "1234", port = "5432")
    cur = conn.cursor()
    
    if(conn.status==1):
        cur.execute("""
                    CREATE TABLE IF NOT EXISTS Jogadores (
                        id SERIAL PRIMARY KEY,
                        nome VARCHAR(50),  
                        clube VARCHAR(50),
                        rodada SMALLINT,
                        gols SMALLINT,
                        assists SMALLINT,
                        passescertos SMALLINT,
                        passeserrados SMALLINT,
                        passesimportantes SMALLINT,
                        chutesnogol SMALLINT,
                        chutesprafora SMALLINT,
                        chutesbloqueados SMALLINT,
                        driblescertos SMALLINT,
                        dribleserrados SMALLINT,
                        driblessofridos SMALLINT,
                        duelosganhos SMALLINT,
                        duelosperdidos SMALLINT,
                        posseperdida SMALLINT,
                        faltascometidas SMALLINT,
                        faltassofridas SMALLINT,
                        interceptacoes SMALLINT,
                        desarmes SMALLINT,
                        nota FLOAT              
                    );
                    """)
        conn.commit()
        cur.close()
        conn.close()
        return True
    else:
        cur.close()
        conn.close()
        return False
    
init()
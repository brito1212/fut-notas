from app_settings import db


class Jogador(db.Model):
    __tablename__ = "jogadores"
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(50), unique=True, nullable=False)
    clube = db.Column(db.String(50), unique=True, nullable=False)
    rodada = db.Column(db.Integer, default=0)
    gols = db.Column(db.Integer, default=0)
    assists = db.Column(db.Integer, default=0)
    passescertos = db.Column(db.Integer, default=0)
    passeserrados = db.Column(db.Integer, default=0)
    passesimportantes = db.Column(db.Integer, default=0)
    chutesnogol = db.Column(db.Integer, default=0)
    chutesprafora = db.Column(db.Integer, default=0)
    chutesbloqueados = db.Column(db.Integer, default=0)
    driblescertos = db.Column(db.Integer, default=0)
    dribleserrados = db.Column(db.Integer, default=0)
    driblessofridos = db.Column(db.Integer, default=0)
    duelosganhos = db.Column(db.Integer, default=0)
    duelosperdidos = db.Column(db.Integer, default=0)
    posseperdida = db.Column(db.Integer, default=0)
    faltascometidas = db.Column(db.Integer, default=0)
    faltassofridas = db.Column(db.Integer, default=0)
    interceptacoes = db.Column(db.Integer, default=0)
    desarmes = db.Column(db.Integer, default=0)
    nota = db.Column(db.Integer, default=0)

    def calcular_nota(self):
        base = 6
        weights = {
            'gols': 0.75,
            'assists': 0.5,
            'passescertos': 0.02,
            'passeserrados': -0.04,
            'passesimportantes': 0.2,
            'chutesnogol': 0.05,
            'chutesprafora': -0.05,
            'chutesbloqueados': 0.05,
            'driblescertos': 0.1,
            'dribleserrados': -0.05,
            'driblessofridos': -0.1,
            'duelosganhos': 0.05,
            'duelosperdidos': -0.05,
            'posseperdida': -0.02,
            'faltascometidas': -0.15,
            'faltassofridas': 0.05,
            'interceptacoes': 0.1,
            'desarmes': 0.1
        }

        nota = base

        for key, value in weights.items():
            nota += round(getattr(self, key) * value,2)

        if nota > 10.0:
            nota = 10.0
        elif nota < 0.0:
            nota = 0.0
        self.nota = round(nota, 2)
        return nota

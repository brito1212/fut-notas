from app import db


class Jogador(db.Model):
    __tablename__ = "jogadores"
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(50), unique=True, nullable=False)
    gols = db.Column(db.Integer, default=0)
    assists = db.Column(db.Integer, default=0)
    passescertos = db.Column(db.Integer, default=0)
    passeserrados = db.Column(db.Integer, default=0)
    passesimportantes = db.Column(db.Integer, default=0)
    chutesnogol = db.Column(db.Integer, default=0)
    chutesprafora = db.Column(db.Integer, default=0)
    chutesbloqueados = db.Column(db.Integer, default=0)
    dribleserrados = db.Column(db.Integer, default=0)
    duelosganhos = db.Column(db.Integer, default=0)
    duelosperdidos = db.Column(db.Integer, default=0)
    posseperdida = db.Column(db.Integer, default=0)
    faltascometidas = db.Column(db.Integer, default=0)
    faltassofridas = db.Column(db.Integer, default=0)
    interceptacoes = db.Column(db.Integer, default=0)
    desarmes = db.Column(db.Integer, default=0)
    nota = db.Column(db.Integer, default=0)

    def calcular_nota(self):
        nota = (self.gols * 3 + self.assists * 2 + self.passescertos) / 6
        self.nota = nota
        return nota

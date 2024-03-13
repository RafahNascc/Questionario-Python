#Importa o banco de dados
from app import db

# Define o modelo de dados
class Dados(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    responsavel = db.Column(db.String(100), nullable=False)
    data = db.Column(db.String(100), nullable=False)
    serial = db.Column(db.String(100), nullable=False)
    status = db.Column(db.String(100), nullable=False)
    identificação = db.Column(db.String(100), nullable=False)
    aspecto = db.Column(db.String(100), nullable=False)
    memoria = db.Column(db.String(100), nullable=False)
    montagem_direcao = db.Column(db.String(100), nullable=False)
    identificação_direcao = db.Column(db.String(100), nullable=False)
    aspecto_direcao = db.Column(db.String(100), nullable=False)
    montagem_tracao = db.Column(db.String(100), nullable=False)
    freio_tracao = db.Column(db.String(100), nullable=False)
    identificação_tracao = db.Column(db.String(100), nullable=False)
    aspecto_tracao = db.Column(db.String(100), nullable=False)
    montagem_sensores = db.Column(db.String(100), nullable=False)
    identificação_sensores = db.Column(db.String(100), nullable=False)
    aspecto_sensores = db.Column(db.String(100), nullable=False)
    montagem_engate = db.Column(db.String(100), nullable=False)
    hidráulico_engate = db.Column(db.String(100), nullable=False)
    identificação_engate = db.Column(db.String(100), nullable=False)
    aspecto_engate = db.Column(db.String(100), nullable=False)
    montagem_baterias = db.Column(db.String(100), nullable=False)
    identificação_baterias = db.Column(db.String(100), nullable=False)
    aspecto_baterias = db.Column(db.String(100), nullable=False)
    montagem_botoeira = db.Column(db.String(100), nullable=False)
    identificação_botoeira = db.Column(db.String(100), nullable=False)
    aspecto_botoeira = db.Column(db.String(100), nullable=False)
    montagem_tampas = db.Column(db.String(100), nullable=False)
    raspadores_tampas = db.Column(db.String(100), nullable=False)
    aspecto_tampas = db.Column(db.String(100), nullable=False)
    teste_tampas = db.Column(db.String(100), nullable=False)
    torqueamento_tampas = db.Column(db.String(100), nullable=False)
    pintura_equipaamento = db.Column(db.String(100), nullable=False)
    adesivos_equipamento = db.Column(db.String(100), nullable=False)
    joystick_equipamento = db.Column(db.String(100), nullable=False)
    comentario1 = db.Column(db.String(100), nullable=True)
    comentario2 = db.Column(db.String(100), nullable=True)
    comentario3 = db.Column(db.String(100), nullable=True)
    comentario4 = db.Column(db.String(100), nullable=True)
    comentario5 = db.Column(db.String(100), nullable=True)
    comentario6 = db.Column(db.String(100), nullable=True)
    comentario7 = db.Column(db.String(100), nullable=True)
    comentario8 = db.Column(db.String(100), nullable=True)
    comentario9 = db.Column(db.String(100), nullable=True)
    comentario10 = db.Column(db.String(100), nullable=True)
    comentario11 = db.Column(db.String(100), nullable=True)
    comentario12 = db.Column(db.String(100), nullable=True)
    comentario13 = db.Column(db.String(100), nullable=True)
    comentario14 = db.Column(db.String(100), nullable=True)
    comentario15 = db.Column(db.String(100), nullable=True)
    comentario16 = db.Column(db.String(100), nullable=True)
    comentario17 = db.Column(db.String(100), nullable=True)
    comentario18 = db.Column(db.String(100), nullable=True)
    comentario19 = db.Column(db.String(100), nullable=True)
    comentario20 = db.Column(db.String(100), nullable=True)
    comentario21 = db.Column(db.String(100), nullable=True)
    comentario22 = db.Column(db.String(100), nullable=True)
    comentario23 = db.Column(db.String(100), nullable=True)
    comentario24 = db.Column(db.String(100), nullable=True)
    comentario25 = db.Column(db.String(100), nullable=True)
    comentario26 = db.Column(db.String(100), nullable=True)
    comentario27 = db.Column(db.String(100), nullable=True)
    comentario28 = db.Column(db.String(100), nullable=True)
    comentario29 = db.Column(db.String(100), nullable=True)
    comentario30 = db.Column(db.String(100), nullable=True)
    comentario31 = db.Column(db.String(100), nullable=True)
    comentario32 = db.Column(db.String(100), nullable=True)




    #Construtor com os parametros
    def __init__(self, responsavel, data, serial, status, identificação, aspecto, memoria, montagem_direcao,identificação_direcao,
                 aspecto_direcao, montagem_tracao, freio_tracao, identificação_tracao, aspecto_tracao, montagem_sensores, identificação_sensores, aspecto_sensores, montagem_engate, hidráulico_engate, identificação_engate,
                 aspecto_engate, montagem_baterias, identificação_baterias, aspecto_baterias, montagem_botoeira, identificação_botoeira, aspecto_botoeira, montagem_tampas, raspadores_tampas, aspecto_tampas, teste_tampas, torqueamento_tampas, pintura_equipaamento, adesivos_equipamento, joystick_equipamento, comentario1,
                 comentario2, comentario3, comentario4, comentario5, comentario6, comentario7, comentario8, comentario9, comentario10, comentario11, comentario12, comentario13, comentario14, comentario15, comentario16, comentario17, comentario18, comentario19, comentario20, comentario21, comentario22, comentario23, comentario24, comentario25, comentario26, comentario27, comentario28, comentario29, comentario30, comentario31, comentario32):
        
        self.responsavel = responsavel
        self.data = data
        self.serial = serial
        self.status = status
        self.identificação = identificação
        self.aspecto = aspecto
        self.memoria = memoria
        self.montagem_direcao = montagem_direcao
        self.identificação_direcao = identificação_direcao
        self.aspecto_direcao = aspecto_direcao
        self.montagem_tracao = montagem_tracao
        self.freio_tracao = freio_tracao
        self.identificação_tracao = identificação_tracao
        self.aspecto_tracao = aspecto_tracao
        self.montagem_sensores = montagem_sensores
        self.identificação_sensores = identificação_sensores
        self.aspecto_sensores = aspecto_sensores
        self.montagem_engate = montagem_engate
        self.hidráulico_engate = hidráulico_engate
        self.identificação_engate = identificação_engate
        self.aspecto_engate = aspecto_engate
        self.montagem_baterias = montagem_baterias
        self.identificação_baterias = identificação_baterias
        self.aspecto_baterias = aspecto_baterias
        self.montagem_botoeira = montagem_botoeira
        self.identificação_botoeira = identificação_botoeira
        self.aspecto_botoeira = aspecto_botoeira
        self.montagem_tampas = montagem_tampas
        self.raspadores_tampas = raspadores_tampas
        self.aspecto_tampas = aspecto_tampas
        self.teste_tampas = teste_tampas
        self.torqueamento_tampas = torqueamento_tampas
        self.pintura_equipaamento = pintura_equipaamento
        self.adesivos_equipamento = adesivos_equipamento
        self.joystick_equipamento = joystick_equipamento
        self.comentario1 = comentario1
        self.comentario2 = comentario2
        self.comentario3 = comentario3
        self.comentario4 = comentario4
        self.comentario5 = comentario5
        self.comentario6 = comentario6
        self.comentario7 = comentario7
        self.comentario8 = comentario8
        self.comentario9 = comentario9
        self.comentario10 = comentario10
        self.comentario11 = comentario11
        self.comentario12 = comentario12
        self.comentario13 = comentario13
        self.comentario14 = comentario14
        self.comentario15 = comentario15
        self.comentario16 = comentario16
        self.comentario17 = comentario17
        self.comentario18 = comentario18
        self.comentario19 = comentario19
        self.comentario20 = comentario20
        self.comentario21 = comentario21
        self.comentario22 = comentario22
        self.comentario23 = comentario23
        self.comentario24 = comentario24
        self.comentario25 = comentario25
        self.comentario26 = comentario26
        self.comentario27 = comentario27
        self.comentario28 = comentario28
        self.comentario29 = comentario29
        self.comentario30 = comentario30
        self.comentario31 = comentario31
        self.comentario32 = comentario32

        
#Importa as bibliotecas
from flask import render_template, request, redirect, url_for, jsonify
from app import app, db
from models import Dados
from login_manager import verificar_login

# Rota da página inicial (login)
@app.route('/')
def home():
    return render_template('login.html')

# Rota para verificar o login
@app.route('/verificar_login', methods=['POST'])
def verificar_login_route():
    data = request.get_json()
    username = data['username']
    password = data['password']

    if verificar_login(username, password):
        return jsonify({"success": True})
    else:
        return jsonify({"success": False})

# Rota para a página principal (após o login)
@app.route('/home')
def pagina_home():
    return render_template('home.html')
# ===================================================================================================================================

def enviar_dados():
    if request.method == 'POST':
        # Valide os dados do formulário
        if not request.form['responsavel']:
            return jsonify({"error": "O campo responsável é obrigatório."})
        if not request.form['data']:
            return jsonify({"error": "O campo data é obrigatório."})
        if not request.form['serial']:
            return jsonify({"error": "O campo serial é obrigatório."})
        if not request.form['status']:
            return jsonify({"error": "O campo status é obrigatório."})
        if not request.form['identificação']:
            return jsonify({"error": "O campo identificação é obrigatório."})
        if not request.form['aspecto']:
            return jsonify({"error": "O campo aspecto é obrigatório."})
        if not request.form['memoria']:
            return jsonify({"error": "O campo memoria é obrigatório."})
        if not request.form['montagem_direcao']:
            return jsonify({"error": "O campo montagem_direcao é obrigatório."})
        if not request.form['identificação_direcao']:
            return jsonify({"error": "O campo identificação_direcao é obrigatório."})
        if not request.form['aspecto_direcao']:
            return jsonify({"error": "O campo aspecto_direcao é obrigatório."})       
        if not request.form['montagem_tracao']:
            return jsonify({"error": "O campo montagem_tracao é obrigatório."}) 
        if not request.form['freio_tracao']:
            return jsonify({"error": "O campo freio_tracao é obrigatório."}) 
        if not request.form['identificação_tracao']:
            return jsonify({"error": "O campo identificação_tracao é obrigatório."})  
        if not request.form['aspecto_tracao']:
            return jsonify({"error": "O campo aspecto_tracao é obrigatório."}) 
        if not request.form['montagem_sensores']:
            return jsonify({"error": "O campo montagem_sensores é obrigatório."})
        if not request.form['identificação_sensores']:
            return jsonify({"error": "O campo identificação_sensores é obrigatório."})   
        if not request.form['aspecto_sensores']:
            return jsonify({"error": "O campo aspecto_sensores é obrigatório."})  
        if not request.form['montagem_engate']:
            return jsonify({"error": "O campo montagem_engate é obrigatório."})  
        if not request.form['hidráulico_engate']:
            return jsonify({"error": "O campo hidráulico_engate é obrigatório."})  
        if not request.form['identificação_engate']:
            return jsonify({"error": "O campo identificação_engate é obrigatório."})
        if not request.form['aspecto_engate']:
            return jsonify({"error": "O campo aspecto_engate é obrigatório."})
        if not request.form['montagem_baterias']:
            return jsonify({"error": "O campo montagem_baterias é obrigatório."})  
        if not request.form['identificação_baterias']:
            return jsonify({"error": "O campo identificação_baterias é obrigatório."})  
        if not request.form['aspecto_baterias']:
            return jsonify({"error": "O campo aspecto_baterias é obrigatório."}) 
        if not request.form['montagem_botoeira']:
            return jsonify({"error": "O campo montagem_botoeira é obrigatório."})  
        if not request.form['identificação_botoeira']:
            return jsonify({"error": "O campo identificação_botoeira é obrigatório."})                              
        if not request.form['aspecto_botoeira']:
            return jsonify({"error": "O campo aspecto_botoeira é obrigatório."})
        if not request.form['montagem_tampas']:
            return jsonify({"error": "O campo montagem_tampas é obrigatório."})
        if not request.form['raspadores_tampas']:
            return jsonify({"error": "O campo raspadores_tampas é obrigatório."})
        if not request.form['aspecto_tampas']:
            return jsonify({"error": "O campo aspecto_tampas é obrigatório."})
        if not request.form['teste_tampas']:
            return jsonify({"error": "O campo teste_tampas é obrigatório."})
        if not request.form['torqueamento_tampas']:
            return jsonify({"error": "O campo torqueamento_tampas é obrigatório."})
        if not request.form['pintura_equipaamento']:
            return jsonify({"error": "O campo pintura_equipaamento é obrigatório."})
        if not request.form['adesivos_equipamento']:
            return jsonify({"error": "O campo adesivos_equipamento é obrigatório."})
        if not request.form['joystick_equipamento']:
            return jsonify({"error": "O campo joystick_equipamento é obrigatório."})
        
        
        # Crie uma instância dos dados
        novo_dado = Dados(responsavel=request.form['responsavel'], data=request.form['data'], serial=request.form['serial'],
                        status=request.form['status'], identificação=request.form['identificação'], aspecto=request.form['aspecto'],
                        memoria=request.form['memoria'], montagem_direcao=request.form['montagem_direcao'],
                        identificação_direcao=request.form['identificação_direcao'], aspecto_direcao=request.form['aspecto_direcao'],
                        montagem_tracao=request.form['montagem_tracao'], freio_tracao = request.form['freio_tracao'], identificação_tracao = request.form['identificação_tracao'], 
                        aspecto_tracao=request.form['aspecto_tracao'], montagem_sensores=request.form['montagem_sensores'], identificação_sensores = request.form['identificação_sensores'],
                        aspecto_sensores = request.form['aspecto_sensores'], montagem_engate = request.form['montagem_engate'], hidráulico_engate = request.form['hidráulico_engate'],
                        identificação_engate = request.form_data_parser_class['identificação_engate'], aspecto_engate = request.form['aspecto_engate'], montagem_baterias = request.form['montagem_baterias'],
                        identificação_baterias = request.form['identificação_baterias'], aspecto_baterias = request.form['aspecto_baterias'], montagem_botoeira = request.form['montagem_botoeira'], identificação_botoeira = request.form['identificação_botoeira'], aspecto_botoeira = request.form['aspecto_botoeira'],
                        montagem_tampas = request.form['montagem_tampas'], raspadores_tampas = request.form['raspadores_tampas'], aspecto_tampas = request.form['aspecto_tampas'], teste_tampas = request.form['teste_tampas'], torqueamento_tampas = request.form['torqueamento_tampas'], pintura_equipaamento = request.form['pintura_equipaamento'], adesivos_equipamento = request.form['adesivos_equipamento'], joystick_equipamento = request.form['joystick_equipamento'],
                        comentario1 = request.form['comentario1'],
                        comentario2 = request.form['comentario2'],
                        comentario3 = request.form['comentario3'],
                        comentario4 = request.form['comentario4'],
                        comentario5 = request.form['comentario5'],
                        comentario6 = request.form['comentario6'],
                        comentario7 = request.form['comentario7'],
                        comentario8 = request.form['comentario8'],
                        comentario9 = request.form['comentario9'],
                        comentario10 = request.form['comentario10'],
                        comentario11 = request.form['comentario11'],
                        comentario12 = request.form['comentario12'],
                        comentario13 = request.form['comentario13'],
                        comentario14 = request.form['comentario14'],
                        comentario15 = request.form['comentario15'],
                        comentario16 = request.form['comentario16'],
                        comentario17 = request.form['comentario17'],
                        comentario18 = request.form['comentario18'],
                        comentario19 = request.form['comentario19'],
                        comentario20 = request.form['comentario20'],
                        comentario21 = request.form['comentario21'],
                        comentario22 = request.form['comentario22'],
                        comentario23 = request.form['comentario23'],
                        comentario24 = request.form['comentario24'],
                        comentario25= request.form['comentario25'],
                        comentario26 = request.form['comentario26'],
                        comentario27 = request.form['comentario27'],
                        comentario28 = request.form['comentario28'],
                        comentario29 = request.form['comentario29'],
                        comentario30 = request.form['comentario30'],
                        comentario31 = request.form['comentario31'],
                        comentario32 = request.form['comentario32'])

        # Adicione e salve a instância no banco de dados
        db.session.add(novo_dado)
        db.session.commit()

        # Retorne um JSON com a mensagem de sucesso
        return jsonify({"success": "Dados enviados com sucesso."})

    # Retorne um JSON com a mensagem de erro
    return jsonify({"error": "Erro ao enviar dados."})

@app.route('/submit', methods=['POST'])
def submit():
    # Obtenha os dados do formulário
    responsavel = request.form['responsavel']
    data = request.form['data']
    serial = request.form['serial']
    status = request.form['status']
    identificação = request.form['identificação']
    aspecto = request.form['aspecto']
    memoria = request.form['memoria']
    montagem_direcao = request.form['montagem_direcao']
    identificação_direcao = request.form['identificação_direcao']
    aspecto_direcao = request.form['aspecto_direcao']
    montagem_tracao = request.form['montagem_tracao']
    freio_tracao = request.form['freio_tracao']
    identificação_tracao = request.form['identificação_tracao']
    aspecto_tracao = request.form['aspecto_tracao']
    montagem_sensores = request.form['montagem_sensores']
    identificação_sensores = request.form['identificação_sensores']
    aspecto_sensores = request.form['aspecto_sensores']
    montagem_engate = request.form['montagem_engate']
    hidráulico_engate = request.form['hidráulico_engate']
    identificação_engate = request.form['identificação_engate']
    aspecto_engate = request.form['aspecto_engate']
    montagem_baterias = request.form['montagem_baterias']
    identificação_baterias = request.form['identificação_baterias']
    aspecto_baterias = request.form['aspecto_baterias']
    montagem_botoeira = request.form['montagem_botoeira']
    identificação_botoeira = request.form['identificação_botoeira']
    aspecto_botoeira = request.form['aspecto_botoeira']
    montagem_tampas = request.form['montagem_tampas']
    raspadores_tampas = request.form['raspadores_tampas']
    aspecto_tampas = request.form['aspecto_tampas']
    teste_tampas = request.form['teste_tampas']
    torqueamento_tampas = request.form['torqueamento_tampas']
    pintura_equipaamento = request.form['pintura_equipaamento']
    adesivos_equipamento = request.form['adesivos_equipamento']
    joystick_equipamento = request.form['joystick_equipamento']
    comentario1 = request.form['comentario1']
    comentario2 = request.form['comentario2']
    comentario3 = request.form['comentario3']
    comentario4 = request.form['comentario4']
    comentario5 = request.form['comentario5']
    comentario6 = request.form['comentario6']
    comentario7 = request.form['comentario7']
    comentario8 = request.form['comentario8']
    comentario9 = request.form['comentario9']
    comentario10 = request.form['comentario10']
    comentario11 = request.form['comentario11']
    comentario12 = request.form['comentario12']
    comentario13 = request.form['comentario13']
    comentario14 = request.form['comentario14']
    comentario15 = request.form['comentario15']
    comentario16 = request.form['comentario16']
    comentario17 = request.form['comentario17']
    comentario18 = request.form['comentario18']
    comentario19 = request.form['comentario19']
    comentario20 = request.form['comentario20']
    comentario21 = request.form['comentario21']
    comentario22 = request.form['comentario22']
    comentario23 = request.form['comentario23']
    comentario24 = request.form['comentario24']
    comentario25 = request.form['comentario25']
    comentario26 = request.form['comentario26']
    comentario27 = request.form['comentario27']
    comentario28 = request.form['comentario28']
    comentario29 = request.form['comentario29']
    comentario30 = request.form['comentario30']
    comentario31 = request.form['comentario31']
    comentario32 = request.form['comentario32']

    # Crie uma instância dos dados
    novo_dado = Dados(responsavel=responsavel, data=data, serial=serial, status=status, identificação=identificação,
                    aspecto=aspecto, memoria=memoria, montagem_direcao=montagem_direcao, identificação_direcao=identificação_direcao,
                    aspecto_direcao=aspecto_direcao, montagem_tracao=montagem_tracao, freio_tracao=freio_tracao, identificação_tracao=identificação_tracao,
                    aspecto_tracao=aspecto_tracao, montagem_sensores = montagem_sensores, identificação_sensores = identificação_sensores, aspecto_sensores = aspecto_sensores, montagem_engate = montagem_engate, hidráulico_engate = hidráulico_engate,
                    identificação_engate = identificação_engate, aspecto_engate = aspecto_engate, montagem_baterias = montagem_baterias, identificação_baterias = identificação_baterias, aspecto_baterias = aspecto_baterias, montagem_botoeira=montagem_botoeira, identificação_botoeira=identificação_botoeira, aspecto_botoeira=aspecto_botoeira,
                    montagem_tampas=montagem_tampas, raspadores_tampas = raspadores_tampas, aspecto_tampas = aspecto_tampas, teste_tampas = teste_tampas, torqueamento_tampas = torqueamento_tampas, pintura_equipaamento = pintura_equipaamento, adesivos_equipamento = adesivos_equipamento, joystick_equipamento = joystick_equipamento,
                    comentario1 = comentario1, 
                    comentario2=comentario2,  
                    comentario3= comentario3,  
                    comentario4= comentario4,  
                    comentario5= comentario5,  
                    comentario6= comentario6,  
                    comentario7= comentario7,  
                    comentario8= comentario8,  
                    comentario9= comentario9,  
                    comentario10= comentario10,  
                    comentario11= comentario11,  
                    comentario12= comentario12, 
                    comentario13= comentario13, 
                    comentario14= comentario14,
                    comentario15=comentario15, 
                    comentario16=comentario16,
                    comentario17=comentario17,
                    comentario18=comentario18,
                    comentario19=comentario19,
                    comentario20=comentario20,
                    comentario21=comentario21,
                    comentario22=comentario22,
                    comentario23=comentario23,
                    comentario24=comentario24,
                    comentario25=comentario25,
                    comentario26=comentario26,
                    comentario27=comentario27, 
                    comentario28=comentario28, 
                    comentario29=comentario29, 
                    comentario30=comentario30, 
                    comentario31=comentario31, 
                    comentario32=comentario32)

    # Adicione e salve a instância no banco de dados
    db.session.add(novo_dado)
    db.session.commit()

    # Redirecione o usuário para uma página de sucesso ou qualquer outra página desejada
    return redirect(url_for('home'))


# login_manager.py
from flask import jsonify

# Rota da página inicial (login)
login_correto = "adm"
senha_correta = "adm"

def verificar_login(username, password):
    if username == login_correto and password == senha_correta:
        return True
    else:
        return False

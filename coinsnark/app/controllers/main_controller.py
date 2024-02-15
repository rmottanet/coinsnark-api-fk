from flask import Blueprint

# Definindo o blueprint
main_bp = Blueprint('main', __name__)

# Rota principal
@main_bp.route('/')
def index():
    return 'Coin Snark API API <br> <a href="https://rmottanet.gitbook.io/coinsnark">Documentação</a>'

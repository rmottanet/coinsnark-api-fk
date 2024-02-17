from flask import Blueprint, render_template

# Definindo o blueprint
main_bp = Blueprint('main', __name__)

# Rota principal
@main_bp.route('/')
def index():
    return render_template('index.html')

from flask import Flask, render_template

from modules.catalogo import catalogo_bp
from modules.favoritos import favoritos_bp
from modules.informacoes import informacoes_bp
from modules.recomendacoes import recomendacoes_bp

def create_app():
    """Cria e configura a aplicação Flask."""
    app = Flask(__name__)

    # Registro dos módulos
    app.register_blueprint(catalogo_bp)
    app.register_blueprint(favoritos_bp)
    app.register_blueprint(informacoes_bp)
    app.register_blueprint(recomendacoes_bp)

    @app.route("/")
    def pagina_inicial():
        return render_template("index.html")
    return app

app = create_app()

if __name__ == "__main__":
    app.run(debug=True)
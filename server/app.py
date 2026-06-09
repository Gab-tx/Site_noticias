from flask import Flask
from flask_cors import CORS
from routes.admin import admin_bp
from routes.categoria import categoria_bp
from routes.imagem import imagem_bp
from routes.noticia import noticia_bp

app = Flask(__name__)

CORS(app)

app.register_blueprint(noticia_bp)
app.register_blueprint(categoria_bp)
app.register_blueprint(imagem_bp)
app.register_blueprint(admin_bp)



if __name__=="__main__":
    app.run(debug=True)
from flask import Flask, url_for, jsonify
app = Flask(__name__)

@app.route('/')
def api_root():
    return 'Bienvenido'

@app.route('/articulos')
def api_articles():
    return 'lista de ' + url_for('api_articles')

@app.route('/articulos/<int:articuloId>')
def api_article(articuloId):
    return 'Ingresaste el id: ' + articuloId

if __name__ == '__main__':
    app.run()
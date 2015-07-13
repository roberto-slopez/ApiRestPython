Vamos a comenzar por hacer una aplicación completa que responde a las peticiones de root /, /artículos y /artículos/:id

```python
from flask import Flask, url_for
app = Flask(__name__)

@app.route('/')
def api_root():
    return 'Bienvenido'

@app.route('/articles')
def api_articles():
    return 'List of ' + url_for('api_articles')

@app.route('/articles/<articleid>')
def api_article(articleid):
    return 'You are reading ' + articleid

if __name__ == '__main__':
    app.run()
```

Usando curl:
<pre>
curl http://127.0.0.1:5000/
</pre>

Las respuestas serán estas, respectivamente.

<pre>
GET /
Bienvenido

GET /articles
lista de /articles

GET /articles/123
Id enviado es: 123
</pre>

Las rutas pueden usar diferentes convertidores entero, punto flotante, etc. mas tipos [aquí](http://flask.pocoo.org/docs/api/#url-route-registrations)

<pre>
@app.route('/articles/<articleid>')
</pre>

Ejemplo: 

<pre>
@app.route('/articles/<int:articleid>')
@app.route('/articles/<float:articleid>')
@app.route('/articles/<path:articleid>')
</pre>

El default es string.

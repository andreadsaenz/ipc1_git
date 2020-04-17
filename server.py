from flask import Flask, render_template

app = Flask(__name__)

@app.route("/hello")
def hello():
    return "Hola mundo"

@app.route("/saludo")
@app.route("/saludo/<nombre>")
def saludo(nombre=None):
    return render_template('index.html', nombre=nombre)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)
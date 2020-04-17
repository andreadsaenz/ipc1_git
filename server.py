from flask import Flask, render_template

app = Flask(__name__)

@app.route("/hello")
def hello():
    return "Hola mundo"


@app.route("/saludo")
@app.route("/saludo/<nombre>")
def saludo(nombre=None):
    return render_template('index.html', nombre=nombre)


@app.route("/factorial/<valor>")
def fact(valor):
    iv = int(valor)
    resultado = factorial(iv)
    return render_template("factorial.html", valor=valor, resultado=resultado)


def factorial(num):
    if num <= 0:
        return 1
    else:
        return num * factorial(num - 1)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)
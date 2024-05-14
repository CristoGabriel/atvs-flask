from flask import Flask, render_template, request, redirect, url_for

class Camisetas:
    def __init__(self, cor, tamanho, marca):
        self.cor = cor
        self.tamanho = tamanho
        self.marca = marca
camiseta1 = Camisetas('Verde','G','Lacoste')
lista = [camiseta1]

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('lista.html', titulo='Camisetas', camisetas=lista)

@app.route('/novo')
def novo():
    return render_template('novo.html', titulo='Cadastro de Camisetas')

@app.route('/criar', methods=['POST',])
def criar():
    cor = request. form['cor']
    tamanho = request. form['tamanho']
    marca = request. form['marca']
    camiseta = Camisetas(cor, tamanho, marca)
    lista.append(camiseta)
    return redirect(url_for('index'))

app.run(debug=True)
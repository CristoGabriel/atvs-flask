from flask import Flask, render_template, request, redirect, url_for, session, flash

class Camisetas:
    def __init__(self, cor, tamanho, marca):
        self.cor = cor
        self.tamanho = tamanho
        self.marca = marca
camiseta1 = Camisetas('Verde','G','Lacoste')
lista = [camiseta1]

app = Flask(__name__)
app.secret_key = 'teste123'

class Usuarios:
    def __init__(self, login, senha):
        self.login = login
        self.senha = senha
usuario1 = Usuarios("aaa", "111")
usuario2 = Usuarios("bbb", "222")
usuario3 = Usuarios("ccc", "333")

usuarios = {
    usuario1.login : usuario1,
    usuario2.login : usuario2,
    usuario3.login : usuario3,
}

@app.route('/login')
def login():
    proxima = request.args.get('proxima')
    return render_template('login.html', proxima=proxima)


@app.route('/')
def index():
    return render_template('lista.html', titulo='Camisetas', camisetas=lista)

@app.route('/autenticar', methods=['POST'])
def autenticar():
    usuario = request.form.get('usuario')
    senha = request.form.get('senha')
    if usuario in usuarios:
        usuario_obj = usuarios[usuario]
        if senha == usuario_obj.senha:
            session['usuarioLogado'] = usuario_obj.login
            flash(usuario_obj.login + ' logado com sucesso!')
            proximaPagina = request.form.get('proxima')
            if proximaPagina:
                return redirect(proximaPagina)
            else:
                return redirect(url_for('index'))
        else:
            flash('Senha incorreta.')
    else:
        flash('Usuário não encontrado.')
    return redirect(url_for('login'))

@app.route('/novo')
def novo():
    if 'usuarioLogado' not in session or session['usuarioLogado'] == None:
        return redirect(url_for('login', proxima=url_for('novo')))
    return render_template('novo.html', titulo='Cadastro de um novo time')

@app.route('/criar', methods=['POST',])
def criar():
    cor = request. form['cor']
    tamanho = request. form['tamanho']
    marca = request. form['marca']
    camiseta = Camisetas(cor, tamanho, marca)
    lista.append(camiseta)
    return redirect(url_for('index'))

@app.route('/logout')
def logout():
    session['usuarioLogado'] = None
    flash('Logout efetuado com sucesso!')
    return redirect(url_for('index'))

app.run(debug=True)
from flask import Flask, render_template, url_for, request, redirect

app = Flask(__name__)

@app.route('/', defaults={'qtd':1})
@app.route('/<int:qtd>')
def index(qtd):
    return render_template('index.html', qtd=qtd)


if __name__ == '__main__':
    app.run()
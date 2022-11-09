from app import app
from flask import Flask, render_template


@app.route('/')
def main_pesquisa():
    return render_template('cadastro_pesquisa.html')

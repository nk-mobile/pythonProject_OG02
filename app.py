# -*- coding: utf-8 -*-
""" для запуска приложения notepad.exe на Flask сайте для Windows сервера
"""
import os
from flask import Flask, render_template, redirect

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/start', methods=['POST'])
def start_notepad():
    # Запуск bat файла, который запускает notepad.exe
    os.system('notepad.bat')
    # Перенаправление на страницу благодарности
    return redirect('/thanks', 303)

@app.route('/thanks')
def thanks():
    return render_template('thanks.html')

if __name__ == '__main__':
    app.run(debug=True)
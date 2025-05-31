# app.py
from flask import Flask
from data_init import fam

app = Flask(__name__)


@app.route("/")
def home():
    return f"Привіт, {fam.name}! Сумарний дохід: {fam.balance()} грн"

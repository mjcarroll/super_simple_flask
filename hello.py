from flask import Flask
import pandas as pd

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

@app.route('/launches/<int:year>')
def show_launches(year):
    df = pd.read_csv('./launches.csv')
    return str(df[df['Date'] == year])

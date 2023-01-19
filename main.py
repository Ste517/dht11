from flask import Flask, render_template, request
import requests
import json
import os

with open("tokens.json", "r") as f:
    key_file = json.load(f)

KEY=key_file["openweather"]
city_id=key_file["openweatherid"]
units="metric"

# Crea l'URL per richiedere i dati meteorologici
weather_url = f'http://api.openweathermap.org/data/2.5/weather?id={city_id}&appid={KEY}&units={units}'

app = Flask(__name__)
app._static_folder = os.path.abspath("templates/static/")

temp = None
hum = None

# crea una funzione che prenda le richieste di tipo post e ne salvi i dati
@app.route('/', methods=['POST'])
def my_form_post():
    reqtemp = request.form['temp']
    reqhum = request.form['hum']
    global temp
    global hum
    temp, hum = reqtemp, reqhum
    temp = float(temp.replace("'",""))
    hum = int(float(hum.replace("'","")))
    return request.form

@app.route('/')
def index():
    # Effettua la richiesta e ottieni i dati
    response = requests.get(weather_url)
    
    # Converte i dati in formato JSON
    data = response.json()

    # Estrai la temperatura e l'umidità dai dati
    predtemp = data['main']['temp']
    predhum = data['main']['humidity']

    # Passare i valori alla pagina HTML
    return render_template('index.html', temp=temp, hum=hum, predtemp=predtemp, predhum=predhum)

if __name__ == '__main__':
    app.run(debug=False)
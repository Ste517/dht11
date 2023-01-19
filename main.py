from flask import Flask, render_template, request
import requests
import json

# Inserisci la tua chiave API qui
api_key = 'YOUR_API_KEY'

# Inserisci l'ID della città per la quale vuoi ottenere i dati meteorologici
city_id = 'YOUR_CITY_ID'

# Crea l'URL per richiedere i dati meteorologici
weather_url = f'http://api.openweathermap.org/data/2.5/weather?id={city_id}&appid={api_key}'

# Effettua la richiesta e ottieni i dati
response = requests.get(weather_url)

# Converte i dati in formato JSON
data = response.json()

# Estrai la temperatura e l'umidità dai dati
temperature = data['main']['temp']
humidity = data['main']['humidity']

app = Flask(__name__)


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
    return request.form

@app.route('/')
def index():
    # Passare i valori alla pagina HTML
    return render_template('index.html', temp=temp, hum=hum)

if __name__ == '__main__':
    app.run(debug=False)
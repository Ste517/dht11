from flask import Flask, render_template
import serial

app = Flask(__name__)

@app.route('/')
def index():

    ser = serial.Serial('COM6', 9600)

    # Leggere i dati dalla seriale
    data = ser.readline().decode().strip()

    # Chiudere la connessione seriale
    ser.close()

    # Dividere i dati in valori di temperatura e umidità
    temp, hum = data.split("\t")

    # Passare i valori alla pagina HTML
    return render_template('index.html', temp=temp, hum=hum)

if __name__ == '__main__':
    app.run(debug=False)
from flask import Flask, render_template, request

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
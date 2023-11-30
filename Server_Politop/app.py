from flask import  Flask, render_template,jsonify, request
import os

from Server_Politop.


app = Flask(__name__)

def current_user():
    return current_user

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    try:
        #Ottieni il file dalla richiesta
        upload_file = request.files["file"]


        #Salva il file nella cartella 'uploads'
        if not os.path.exists('Server_Politop/uploads'):
            print("La cartella non esiste")
        else:
            upload_file.save(os.path.join('Server_Politop/uploads', upload_file.filename))

        

        #Restituisci una risposta JSON
        return jsonify({"success": True})
    except Exception as e:
        return jsonify({"Errore": str(e)})
    
if __name__ == '__main__': 
    app.run(debug=True)
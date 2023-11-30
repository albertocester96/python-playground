from flask import  Flask, render_template,jsonify, request
import os

from esegui_file import communication


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
        upload_file_path = os.path.join('Server_Politop/uploads', upload_file.filename)
        upload_file.save(upload_file_path)

        result= communication(upload_file_path)
        
        #Restituisci una risposta JSON
        return jsonify(result)
    
    except Exception as e:
        return jsonify({"Errore": str(e)})
    
if __name__ == '__main__': 
    app.run(debug=True)
from flask import  Flask, render_template,jsonify, request
import os

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

        #Verifica autorizzazioni utente
        if not current_user.can_upload_files():
            raise Exception("L'utente non ha le autorizzazioni necessarie")

        #Salva il file nella cartella 'uploads'
        upload_file.save(os.path.join('uploads', upload_file.filename))

        #Restituisci una risposta JSON
        return jsonify({"success": True})
    except Exception as e:
        return jsonify({"Errore": str(e)})
    
if __name__ == '__main__': 
    app.run(debug=True)
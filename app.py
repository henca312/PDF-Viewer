from flask import Flask, render_template, send_from_directory
import os

app = Flask(__name__)

# Ordner, in dem die PDFs gespeichert werden
PDF_FOLDER = os.path.join('static', 'pdfs')

@app.route('/')
def index():
    # Listet alle PDF-Dateien im PDF-Ordner auf
    pdf_files = os.listdir(PDF_FOLDER)

    # Variable zur Steuerung welche PDFS angezeigt werden sollen / Dieser Muss aus AZURE AI Search heraus erstellt werden
    PDF_LIST =  ['1.pdf','2.pdf']

    # Iteration auf alle PDF Files und nehme nur die auch in PDF_LIST stehen
    pdf_files = [f for f in pdf_files if f.endswith('.pdf') and f in PDF_LIST]
    
    return render_template('index.html', pdf_files=pdf_files)

@app.route('/pdf/<filename>')
def pdf_view(filename):
    # Sendet die PDF-Datei an den Client für die Anzeige im Web
    return send_from_directory(PDF_FOLDER, filename)

if __name__ == '__main__':
    app.run(debug=True)

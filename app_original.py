from flask import Flask, render_template, request, redirect, url_for, flash
import os
from test_addqrcodes_final import add_qr_codes_to_a3

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Needed for flash messages

UPLOAD_FOLDER = 'uploads/'
OUTPUT_FOLDER = 'outputs/'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(OUTPUT_FOLDER, exist_ok=True)

@app.route('/')
def index():
    return render_template('index_original.html')

@app.route('/generate_pdf', methods=['POST'])
def generate_pdf():
    inputfiles = request.form['inputfolder']  # Get the list of uploaded files
    outputfolder = request.form['outputfolder']
    titlepage = request.form['titlepage']
    outputfile = request.form['outputfile']

    # Ensure output file ends with .pdf
    if not outputfile.endswith('.pdf'):
        outputfile += '.pdf'

    try:

        # Debugging: Print paths
        #print(f"Input files: {inputfolder_paths}")
        print(f"Output folder: {outputfolder}")
        print(f"Output file: {outputfile}")
        print(f"Input file: {inputfiles}")

        # Call your add_qr_codes_to_a3 function
        add_qr_codes_to_a3(inputfiles, outputfolder, titlepage, outputfile)
        message = f"PDF {outputfile} created successfully!"
    except Exception as e:
        message = f"Error: {str(e)}"

    return render_template('index_original.html', message=message)


if __name__ == '__main__':
    app.run(debug=True)

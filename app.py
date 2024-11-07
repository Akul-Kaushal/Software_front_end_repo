from flask import Flask, render_template, request, jsonify
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from flask_pymongo import PyMongo
import os
from dotenv import load_dotenv
import rag_script as rg


load_dotenv()

app = Flask(__name__)

# Set up the Google Sheets API credentials
scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/spreadsheets", "https://www.googleapis.com/auth/drive.file", "https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name(r"C:\Users\lalpa\Documents\soft_fl\flasktest101-c9059b332632.json", scope)
client = gspread.authorize(creds)

# Route to render the input form
@app.route('/')
def index():
    return render_template('index.html')

# Route to handle form submission
@app.route('/submit', methods=['POST'])
def submit():
    user_data = request.form['data']
    print("Available Spreadsheets:")
    for spreadsheet in client.openall():
        print(spreadsheet.title)

    try:
        sheet = client.open("flask_test_101").sheet1 
        sheet.append_row([user_data])
        return 'Data submitted successfully!'
    except gspread.SpreadsheetNotFound:
        return 'Error: Spreadsheet not found. Please check the name and permissions.'


@app.route('/upload', methods=['POST'])
def upload_file():
    if 'pdf_file' not in request.files:
        return "No file part in the request"
    
    file = request.files['pdf_file']
    if file.filename == '':
        return "No file selected"

    # Process the PDF file
    embedding_model = rg.embedding_model

    text = rg.extract_text_from_pdf(file)
    chunks = rg.get_text_chunks(text)
    embedding = rg.create_embedding(chunks,embedding_model=embedding_model)
    return embedding  # Or handle as needed




# setting up MongoDb configration
# app.config["MONGO_URI"] = os.getenv("MONGODB_URI")
# print("Mongo URI:", os.getenv("MONGODB_URI"))
# mongo = PyMongo(app)
# if mongo.db is None:
#     print("Failed to connect to MongoDB")  # Debug line for connection status
# else:
#     print("Connected to MongoDB")
# @app.route('/upload',methods=['POST'])
# def upload_file():
#     if 'pdfFile' not in request.files:
#         return jsonify({"error": "No file part"}), 400

#     file = request.files['pdfFile']

#     if file.filename == '':
#         return jsonify({"error": "No selected file"}), 400

#     if not file.filename.endswith('.pdf'):
#         return jsonify({"error": "Only PDF files are allowed"}), 400

#     # Store the PDF file in MongoDB
#     mongo.db.files.insert_one({
#         "filename": file.filename,
#         "contentType": file.content_type,
#         "data": file.read()
#     })

if __name__ == '__main__':
    app.run(debug=True)
from flask import Flask, render_template, request, jsonify
import gspread
from oauth2client.service_account import ServiceAccountCredentials

from flask_pymongo import PyMongo
import os
from dotenv import load_dotenv
import test_rag as tst


load_dotenv()

app = Flask(__name__)

# Set up the Google Sheets API credentials
def authenticate_google_sheets():
    scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/spreadsheets", "https://www.googleapis.com/auth/drive.file", "https://www.googleapis.com/auth/drive"]
    creds = ServiceAccountCredentials.from_json_keyfile_name(r"C:\Users\lalpa\Documents\soft_fl\flasktest101-c9059b332632.json", scope)
    client = gspread.authorize(creds)
    return client

file_path = None
flag = 0

@app.route('/')
def root():
    return render_template('main.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/index')
def index():
    return render_template('index.html')

# Route to handle form submission
@app.route('/submit', methods=['POST'])
def submit():
    # Extract data from form
    name = request.form['name']
    email = request.form['email']
    message = request.form['message']

    # Authenticate Google Sheets client
    client = authenticate_google_sheets()

    try:
        # Open the Google Sheets spreadsheet
        sheet = client.open("flask_test_101").sheet1  # Replace with your actual spreadsheet name
        
        # Append the extracted data as a new row
        sheet.append_row([name, email, message])
        print("Data Submitted Successful")
        return render_template('contact.html')
    except gspread.SpreadsheetNotFound:
        return 'Error: Spreadsheet not found. Please check the name and permissions.'


@app.route("/upload", methods=["POST"])
def upload():
    global file_path, flag
    upload_status = None
    if "pdf_file" in request.files:
        uploaded_file = request.files["pdf_file"]
        if uploaded_file.filename != "":
            # Save the file (adjust path as needed)
            uploaded_file.save(f"static/uploads/{uploaded_file.filename}")
            upload_status = f"File '{uploaded_file.filename}' uploaded successfully!"
            file_path = f"static/uploads/{uploaded_file.filename}"  
            flag = 1
        else:
            upload_status = "No file selected!"
    return render_template("index.html", upload_status=upload_status, bot_response=None)

# Chat route
@app.route("/chat", methods=["POST"])
def chat():
    global file_path, flag
    user_message = request.form.get("message")
    # response = f"You asked: {user_message}"

    # Define the file path
    if flag == 0:
        file_path = r'C:/Users/lalpa/Documents/soft_fl/static/uploads/test_file.pdf'

    response = tst.input(file_path,user_message)
    return response




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
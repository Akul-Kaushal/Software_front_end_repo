from flask import Flask, render_template, request
import gspread
from oauth2client.service_account import ServiceAccountCredentials

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

if __name__ == '__main__':
    app.run(debug=True)




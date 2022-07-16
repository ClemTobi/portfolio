from lib2to3.pgen2.token import NEWLINE
from flask import Flask, redirect, render_template, request
import os
from flask import send_from_directory
import csv

app = Flask(__name__)


@app.route("/")
def my_home():
    return render_template('index.html')


# @app.route('/favicon.ico')
# def favicon():
#     return send_from_directory(os.path.join(app.root_path, './static/assets'),
#                                'favicon.png', mimetype='image/vnd.microsoft.icon')


@app.route("/<string:page_name>")
def home(page_name):
    return render_template(page_name)


def write_to_file(data):
    with open('database.txt', mode='a') as data_storage:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        file = data_storage.write(f'\n{email}, {subject}, {message}')


def write_to_csv(data):
    with open('database.csv', newline='', mode='a') as data_storage:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        # fieldnames = ['email', 'subject', 'message']
        # writer = csv.DictWriter(data_storage, fieldnames=fieldnames)
        # writer.writeheader()

        csv_writer = csv.writer(
            data_storage, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)

        csv_writer.writerow([email, subject, message])


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        data = request.form.to_dict()
        print(data)
        # write_to_file(data)
        write_to_csv(data)
        return redirect('/thank you.html')
    else:
        return 'something went wrong'

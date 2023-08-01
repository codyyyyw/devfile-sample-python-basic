from flask import Flask
import requests
import os

app = Flask(__name__)

@app.route('/')
def hello():
    response = requests.get("https://api.open-notify.org/this-api-doesnt-exist")
    print(response.status_code)
    return "Hello World!"

if __name__ == '__main__':
    port = os.environ.get('FLASK_PORT') or 8080
    port = int(port)

    app.run(port=port,host='0.0.0.0')

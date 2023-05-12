from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def start():
    return "AMBOT Started Successfully"

os.system("python3 -m AMBOT")
app.run(port=5000)

# IMPORTS

## MODULES
import json
from flask import Flask, request


app = Flask(__name__)


@app.route("/", methods=['GET'])
def index():
    return "Webservice"

  
if __name__ == "__main__":
    app.run("0.0.0.0", debug=True, port=5000)

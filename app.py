from flask import Flask, render_template,request
import os
import numpy as np
from PIL import Image
import mediapipe as mp
from werkzeug.utils import secure_filename
app = Flask(__name__)

p = int(os.environ.get("PORT", 5000))

@app.route("/", methods=['POST',"GET"])
def upload_image():
    return render_template("index.html")
app.run(debug=True, port=p, host='0.0.0.0')


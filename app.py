from flask import Flask, render_template,request
import os
import numpy as np
import mediapipe
from PIL import Image
from werkzeug.utils import secure_filename
app = Flask(__name__)


@app.route("/", methods=['POST',"GET"])
def upload_image():
    return render_template("index.html")


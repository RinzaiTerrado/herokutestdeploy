from flask import Flask, render_template,request

app = Flask(__name__)



@app.route("/", methods=['POST',"GET"])
def upload_image():
    return render_template("index.html")


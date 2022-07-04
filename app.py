from flask import Flask, render_template,request

app = Flask(__name__)


port = int(os.environ.get('PORT', 5000))

@app.route("/", methods=['POST',"GET"])
def upload_image():
    return render_template("index.html")

app.run(host='0.0.0.0', port=port, debug=True)

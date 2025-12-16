import sys
import os

# Add project root to Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from flask import Flask, render_template, request
from common.preprocessing import predict_yield

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    if request.method == "POST":
        result = predict_yield(
            request.form["region"],
            request.form["soil"],
            request.form["crop"],
            request.form["weather"],
            float(request.form["rainfall"]),
            float(request.form["temperature"]),
            'fertilizer' in request.form,
            'irrigation' in request.form,
            int(request.form["days"])
        )
    return render_template("index.html", result=result)

app.run(debug=True)

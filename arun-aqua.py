from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/contact", methods=["POST"])
def contact():
    name = request.form.get("name")
    phone = request.form.get("phone")
    message = request.form.get("message")

    return f"Thank you {name}! We received your inquiry: {message}"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

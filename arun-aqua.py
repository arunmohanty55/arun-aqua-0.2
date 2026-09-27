from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact", methods=["POST"])
def contact():
    name = request.form.get("name")
    phone = request.form.get("phone")
    message = request.form.get("message")

    return f"""
    <h2>Thank you, {name}!</h2>
    <p>Phone: {phone}</p>
    <p>We received your inquiry:</p>
    <p>{message}</p>
    <a href="/">Back to Home</a>
    """


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

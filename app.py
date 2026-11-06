from flask import Flask, render_template

app = Flask(__name__)

CUSTOM_TEXT = "Seriously Francy, this isn't that hard, you dick"

@app.route("/")
def home():
    return render_template("index.html", text=CUSTOM_TEXT)

if __name__ == "__main__":
    app.run(debug=True)
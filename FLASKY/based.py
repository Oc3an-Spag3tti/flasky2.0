from flask import *

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('my_index.html')

@app.route("/shop")
def unboxing():
    return render_template("unbox.html")

@app.route("/register")
def registration():
    return render_template("registration.html")


if __name__ == "__main__":
    app.run(debug=True)
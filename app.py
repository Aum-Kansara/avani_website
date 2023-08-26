from flask import Flask,render_template

app=Flask(__name__)


@app.route("/")
def index():
    return "Avani's Website"

@app.route("/about")
def about():
    return "This is about page"

@app.route("/services")
def services():
    return "This is Services"


@app.route("/industrySector")
def industySector():
    return "Industry Sector"


@app.route("/pub")
def publication():
    return "This is Publication"

@app.route("/enquiry")
def enquiry():
    return "This is For enquiry"

@app.route("/contact")
def contact():
    return "This is contact page"


app.run(debug=True)
from flask import Flask, render_template, request, redirect, session, url_for
from utils.auth import register_user, authenticate, load_users
from utils.health_data import generate_angles, brain_activity, mobility_score, fall_risk

app = Flask(__name__)
app.secret_key = "fallvision_secret_key"

def login_required(route_function):
    def wrapper(*args, **kwargs):
        if "user" not in session:
            return redirect(url_for("login"))
        return route_function(*args, **kwargs)
    wrapper.__name__ = route_function.__name__
    return wrapper

@app.route("/")
def landing():
    return render_template("landing.html")

@app.route("/signup", methods=["GET", "POST"])
def signup():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        if register_user(username, password):
            return redirect(url_for("login"))
    return render_template("signup.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        if authenticate(username, password):
            session["user"] = username
            return redirect(url_for("dashboard"))
    return render_template("login.html")

@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("landing"))

@app.route("/dashboard")
@login_required
def dashboard():
    angles = generate_angles()
    brain = brain_activity()
    score = mobility_score(angles, brain)
    risk = fall_risk(score)
    return render_template("dashboard.html",
                           angles=angles,
                           brain=brain,
                           score=score,
                           risk=risk,
                           user=session["user"],
                           role=load_users()[session["user"]]["role"])

@app.route("/detection")
@login_required
def detection():
    return render_template("detection.html", user=session["user"])

@app.route("/past-records")
@login_required
def past_records():
    return render_template("past_records.html", user=session["user"])

@app.route("/emergency")
@login_required
def emergency():
    return render_template("emergency.html", user=session["user"])

@app.route("/trends")
@login_required
def trends():
    return render_template("trends.html", user=session["user"])

@app.route("/faq")
def faq():
    return render_template("faq.html")

@app.route("/support", methods=["GET", "POST"])
def support():
    message_sent = False

    if request.method == "POST":
        name = request.form["name"]
        email = request.form["email"]
        message = request.form["message"]

        # For demo: just print in terminal
        print("New Support Request:")
        print("Name:", name)
        print("Email:", email)
        print("Message:", message)

        message_sent = True

    return render_template("support.html", message_sent=message_sent)

@app.route("/resources")
def resources():
    return render_template("resources.html")

if __name__ == "__main__":
    app.run(debug=True)
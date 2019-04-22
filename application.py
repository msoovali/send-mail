import os
import smtplib
from flask import Flask, render_template, request
app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/send", methods=["POST"])
def sendMail():
    sender = "testdevmail97@gmail.com"
    recipient = request.form.get("email")
    subject = request.form.get("subject")
    content = request.form.get("content")
    state = True
    if not recipient or not content:
        state = False
    else:
        message = 'Subject: {}\n\n{}'.format(subject, content)
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(sender, os.getenv("PASSWORD"))
        server.sendmail(sender, recipient, message)
        server.quit()
    return render_template("state.html", state=state)

from flask import (Flask, render_template, redirect, request, flash, session)
import os



app = Flask(__name__)
app.secret_key = os.environ['SECRET_KEY']



@app.route("/")
def home():
  """ Display homepage """

  return render_template("home.html")


if __name__ == "__main__":
  app.run(debug=True)



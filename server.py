from flask import (Flask, render_template, redirect, request, flash, session)
import os



app = Flask(__name__)
app.secret_key = os.environ['SECRET_KEY']

# hard-coded for now, add database later
COLORS = ['black', 'blue', 'brown', 'green', 'orange', 'pink', 'purple', 'red', 'white', 'yellow']


@app.route("/")
def home():
  """ Display homepage """

  return render_template("home.html")


@app.route("/build_lesson")
def customize():
  """ Build a personal lesson based on users' inputs """
  category = request.args.get("category")
  num_words = request.args.get("num_words")
  level = request.args.get("level")

  
  return render_template("colors.html", colors=COLORS)
  




if __name__ == "__main__":
  app.run(debug=True)



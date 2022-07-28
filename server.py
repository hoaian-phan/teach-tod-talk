from flask import (Flask, render_template, redirect, request, flash, session, jsonify)
from random import sample
import os



app = Flask(__name__)
app.secret_key = os.environ['SECRET_KEY']

# hard-coded for now, add database later
COLORS = {
  "easy": ['black', 'blue', 'brown', 'green', 'orange', 'pink', 'purple', 'red', 'white', 'yellow'],
  "medium": ['grey', 'silver', 'gold', 'navy', 'chocolate', 'tan', 'aqua', 'tomato', 'violet', 'teal'],
  "advanced": ['olive', 'maroon', 'snow', 'magenta', 'salmon', 'coral', 'lime', 'orchid', 'khaki', 'cyan', 'plum', 'turquoise', 'beige', 'indigo'],
}

@app.route("/")
def home():
  """ Display homepage """

  return render_template("home.html")


@app.route("/build_lesson")
def customize():
  """ Build a personal lesson based on users' inputs """
  category = request.args.get("category")
  num_words = int(request.args.get("num_words"))
  level = request.args.get("level")

  # Colors:
  color_list = []
  if category == 'colors':
    if level == 'easy':
      color_list = sample(COLORS['easy'], num_words)
    elif level == 'medium':
      easy_num = num_words // 2
      medium_num = num_words - easy_num
      color_list = sample(COLORS['easy'], easy_num)
      color_list.extend(sample(COLORS['medium'], medium_num))
    else:
      easy_num = medium_num = num_words // 3
      advanced_num = num_words - (easy_num + medium_num)
      color_list = sample(COLORS['easy'], easy_num)
      color_list.extend(sample(COLORS['medium'], medium_num))
      color_list.extend(sample(COLORS['advanced'], advanced_num))
    print(color_list)

    # Return jsonify if the request is for json, else render html template
    if request.headers['Accept'] == 'application/json':
      return jsonify({"status": "success", "colors": color_list})
  
    return render_template("colors.html", colors=color_list)
  




if __name__ == "__main__":
  app.run(debug=True)



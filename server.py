from flask import (Flask, render_template, redirect, request, flash, session, jsonify)
from random import sample
import os



app = Flask(__name__)
app.secret_key = os.environ['SECRET_KEY']

# hard-coded for now, add database later
CATEGORIES = {
  "colors": { "easy": ['black', 'blue', 'brown', 'green', 'orange', 'pink', 'purple', 'red', 'white', 'yellow'],
              "medium": ['grey', 'silver', 'gold', 'navy', 'chocolate', 'tan', 'aqua', 'tomato', 'violet', 'teal'],
              "advanced": ['olive', 'maroon', 'snow', 'magenta', 'salmon', 'coral', 'lime', 'orchid', 'khaki', 'cyan', 'plum', 'turquoise', 'beige', 'indigo'],
            },
  "animals": {"easy": ['dog', 'cat', 'cow', 'chicken', 'duck', 'sheep', 'pig', 'fish', 'bird', 'horse'],
              "medium": ['lion', 'brea', 'tiger', 'goat', 'monkey', 'deer', 'mouse', 'dolphin', 'crab', 'frog'],
              "advanced": ['zebra', 'shark', 'rabbit', 'shrimp', 'bee', 'butterfly', 'lobster', 'caterpillar', 'octopus', 'elephant', 'pigeon', 'donkey', 'turkey', 'squirrel', 'panda', 'giraffe']
            },
}
# COLORS = {
#   "easy": ['black', 'blue', 'brown', 'green', 'orange', 'pink', 'purple', 'red', 'white', 'yellow'],
#   "medium": ['grey', 'silver', 'gold', 'navy', 'chocolate', 'tan', 'aqua', 'tomato', 'violet', 'teal'],
#   "advanced": ['olive', 'maroon', 'snow', 'magenta', 'salmon', 'coral', 'lime', 'orchid', 'khaki', 'cyan', 'plum', 'turquoise', 'beige', 'indigo'],
# }

# ANIMALS = {
#   "easy": ['dog', 'cat', 'cow', 'chicken', 'duck', 'sheep', 'pig', 'fish', 'bird', 'horse'],
#   "medium": ['lion', 'brea', 'tiger', 'goat', 'monkey', 'deer', 'mouse', 'dolphin', 'crab', 'frog'],
#   "advanced": ['zebra', 'shark', 'rabbit', 'shrimp', 'bee', 'butterfly', 'lobster', 'caterpillar', 'octopus', 'elephant', 'pigeon', 'donkey', 'turkey', 'squirrel', 'panda', 'giraffe']
# }

@app.route("/")
def home():
  """ Display homepage """

  return render_template("home.html")

def generate_list(category, num_words, level):
  lst = []
  if level == 'easy':
    lst = sample(CATEGORIES[category]['easy'], num_words)
  elif level == 'medium':
    easy_num = num_words // 2
    medium_num = num_words - easy_num
    lst = sample(CATEGORIES[category]['easy'], easy_num)
    lst.extend(sample(CATEGORIES[category]['medium'], medium_num))
  else:
    easy_num = medium_num = num_words // 3
    advanced_num = num_words - (easy_num + medium_num)
    lst = sample(CATEGORIES[category]['easy'], easy_num)
    lst.extend(sample(CATEGORIES[category]['medium'], medium_num))
    lst.extend(sample(CATEGORIES[category]['advanced'], advanced_num))
  print(lst)
  return lst

@app.route("/build_lesson")
def customize():
  """ Build a personal lesson based on users' inputs """
  category = request.args.get("category")
  num_words = int(request.args.get("num_words"))
  level = request.args.get("level")

  # Colors:
  if category == 'colors':
    color_list = generate_list(category=category, num_words=num_words, level=level)

    # Return jsonify if the request is for json, else render html template
    if request.headers['Accept'] == 'application/json':
      return jsonify({"status": "success", "colors": color_list})

    return render_template("colors.html", colors=color_list)

  # Animals
  elif category == 'animals':
    animal_list = generate_list(category=category, num_words=num_words, level=level)

    return render_template("animals.html", animals=animal_list)

  




if __name__ == "__main__":
  app.run(debug=True)



from flask import (Flask, render_template, redirect, request, flash, session, jsonify)
from random import sample
import os



app = Flask(__name__)
app.secret_key = os.environ['SECRET_KEY']

# hard-coded for now, add database later
CATEGORIES = {
  "colors": { 
    "easy": ['black', 'blue', 'brown', 'green', 'orange', 'pink', 'purple', 'red', 'white', 'yellow'],
    "medium": ['grey', 'silver', 'gold', 'navy', 'chocolate', 'tan', 'aqua', 'tomato', 'violet', 'teal'],
    "advanced": ['olive', 'maroon', 'magenta', 'salmon', 'coral', 'lime', 'orchid', 'khaki', 'cyan', 'plum', 'turquoise', 'beige', 'indigo'],
  },
  
  "animals": {
    "easy": [
      {'dog': '/static/image/dog.jpg'},
      {'cat': '/static/image/cat.jpg'},
      {'cow': '/static/image/cow.jpg'}, 
      {'chicken': '/static/image/chicken.jpg'},
      {'duck': '/static/image/duck.jpg'}, 
      {'sheep': '/static/image/sheep.jpg'}, 
      {'pig': '/static/image/pig.jpg'},
      {'fish': '/static/image/fish.jpg'}, 
      {'bird': '/static/image/bird.jpg'}, 
      {'horse': '/static/image/horse.jpg'}
    ],
    "medium": [
      {'lion': '/static/image/lion.jpg'},
      {'bear': '/static/image/bear.jpg'},
      {'tiger': '/static/image/tiger.jpg'},
      {'turtle': '/static/image/turtle.jpg'},
      {'monkey': '/static/image/monkey.jpg'},
      {'deer': '/static/image/deer.jpg'},
      {'mouse': '/static/image/mouse.jpg'},
      {'dolphin': '/static/image/dolphin.jpg'},
      {'crab': '/static/image/crab.jpg'},
      {'frog': '/static/image/frog.jpg'}
    ],
    "advanced": [ 
      {'zebra': '/static/image/zebra.jpg'},
      {'shark': '/static/image/shark.jpg'},
      {'rabbit': '/static/image/rabbit.jpg'},
      {'shrimp': '/static/image/shrimp.jpg'},
      {'bee': '/static/image/bee.jpg'},
      {'butterfly': '/static/image/butterfly.jpg'},
      {'lobster': '/static/image/lobster.jpg'},
      {'caterpillar': '/static/image/caterpillar.jpg'},
      {'octopus': '/static/image/octopus.jpg'},
      {'elephant': '/static/image/elephant.jpg'},
      {'pigeon': '/static/image/pigeon.jpg'},
      {'donkey': '/static/image/donkey.jpg'},
      {'turkey': '/static/image/turkey.jpg'},
      {'squirrel': '/static/image/squirrel.jpg'},
      {'panda': '/static/image/panda.jpg'},
      {'giraffe': '/static/image/giraffe.jpg'}
    ]
  }
}

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
    print(animal_list)

    return render_template("animals.html", animals=animal_list)

  




if __name__ == "__main__":
  app.run(debug=True)



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
      {'rabbit': '/static/image/rabbit.jpg'},
      {'mouse': '/static/image/mouse.jpg'},
      {'dolphin': '/static/image/dolphin.jpg'},
      {'crab': '/static/image/crab.jpg'},
      {'frog': '/static/image/frog.jpg'}
    ],
    "advanced": [ 
      {'zebra': '/static/image/zebra.jpg'},
      {'shark': '/static/image/shark.jpg'},
      {'koala': '/static/image/koala.jpg'},
      {'shrimp': '/static/image/shrimp.jpg'},
      {'snake': '/static/image/snake.jpg'},
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
  },

  "fruits": {
    "easy": [
      {'apple': '/static/image/apple.jpg'},
      {'banana': '/static/image/banana.jpg'},
      {'pear': '/static/image/pear.jpg'}, 
      {'grape': '/static/image/grape.jpg'},
      {'strawberry': '/static/image/strawberry.jpg'}, 
      {'orange': '/static/image/orange.jpg'}, 
      {'lemon': '/static/image/lemon.jpg'},
      {'mango': '/static/image/mango.jpg'}, 
      {'kiwi': '/static/image/kiwi.jpg'}, 
      {'cherry': '/static/image/cherry.jpg'}
    ],
    "medium": [
      {'fig': '/static/image/fig.jpg'},
      {'coconut': '/static/image/coconut.jpg'},
      {'peach': '/static/image/peach.jpg'},
      {'blueberry': '/static/image/blueberry.jpg'},
      {'avocado': '/static/image/avocado.jpg'},
      {'date': '/static/image/date.jpg'},
      {'plum': '/static/image/mouse.jpg'},
      {'papaya': '/static/image/papaya.jpg'},
      {'watermelon': '/static/image/watermelon.jpg'},
      {'pineapple': '/static/image/pineapple.jpg'}
    ],
    "advanced": [ 
      {'raspberry': '/static/image/raspberry.jpg'},
      {'longan': '/static/image/longan.jpg'},
      {'apricot': '/static/image/apricot.jpg'},
      {'honeydew': '/static/image/honeydew.jpg'},
      {'mangosteen': '/static/image/mangosteen.jpg'},
      {'dragonfruit': '/static/image/dragonfruit.jpg'},
      {'nectarine': '/static/image/nectarine.jpg'},
      {'cantaloupe': '/static/image/cantaloupe.jpg'},
      {'durian': '/static/image/durian.jpg'},
      {'grapefruit': '/static/image/grapefruit.jpg'},
      {'guava': '/static/image/guava.jpg'},
      {'jackfruit': '/static/image/jackfruit.jpg'},
      {'lychee': '/static/image/lychee.jpg'},
      {'pomegranate': '/static/image/pomegranate.jpg'},
      {'tangerine': '/static/image/tangerine.jpg'},
    ]
  }
}


# Function to generate a word list for a lesson plan
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
  if category == 'colors':
    color_list = generate_list(category=category, num_words=num_words, level=level)

    return render_template("colors.html", colors=color_list)

  # Animals and Fruits
  elif category == 'animals' or category == 'fruits':
    word_list = generate_list(category=category, num_words=num_words, level=level)

    return render_template("words.html", words=word_list)

  # Error handling
  else:
    flash("Please choose a category")
    return redirect("/")


  




if __name__ == "__main__":
  app.run(debug=True)



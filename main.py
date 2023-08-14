import os
import random
from flask import Flask, render_template

app = Flask(__name__)

cat_photos = [
    'cat1.jpeg',
    'cat2.jpeg',
    'cat3.jpeg',
    'cat4.jpeg',
    'cat5.jpeg'
]

@app.route('/')
def index():
    serve_cats = os.environ.get('SERVE_CATS')
    if serve_cats:
        random_cat_photo = random.choice(cat_photos)
        return render_template('index.html', cat_photo=random_cat_photo)
    else:
        return "SERVE_CATS variable not set"

if __name__ == '__main__':
    app.run()

import sqlite3
import time
from datetime import datetime  
from flask import Flask, request, jsonify


app = Flask(__name__)

#palceholder for testing
posts = [
    {
        "id": 2,
        "title": "Blog Post 2 Tit:le",
        "contents": "<p>This is another blog post</p>",
        "timeStamp": "2022-01-31T16:19:27.149989",
        "categoryId": 1,
    },
    {
        "id": 1,
        "title": "Blog Post Title 1",
        "contents": "<p>This is a blog post</p>",
        "timeStamp": "2022-01-31T16:19:27.149945",
        "categoryId": 2,
    }
]
categories = [
    {
        "id": 1,
        "name": "General"
    },
    {
        "id": 2,
        "name": "Technology"
    },
    {
        "id": 3,
        "name": "Random"
    }
]

@app.get("/posts")
def get_all_posts():
    return jsonify(posts)

    posts.append()
@app.get("/posts/<int:post_id>")
def get_post(post_id):
    result = []
    for p in posts:
        if p['id'] == post_id:
            return p

@app.get("/categories")
def get_categories():
    return jsonify(categories)

@app.post("/posts")
def create_post():
    new_post = request.get_json()
    time_stamp = time.time()
    date_time = datetime.fromtimestamp(time_stamp)
    new_post["timestamp"]=date_time
    # add id? not in spec
    #print(new_post)
    return jsonify(new_post)

@app.put("/posts/<int:post_id>")
def update_post(post_id):
    update = request.get_json()

    return(updated_post)

@app.delete("/posts")
def delete_all_posts:
    return

@app.delete("/posts/<int:post_id>")
def delete_post():
    return

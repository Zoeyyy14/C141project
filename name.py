from flask import Flask,jsonify,request
import csv

all_articles=[]

with open('articles.csv',encoding="utf8")as f:
    reader=csv.reader(f)
    data=list(reader)
    all_articles=data[1:]

liked_articles=[]
not_liked_articles=[]
did_not_watch=[]

app=Flask(__name__)

@app.route("/get-article")
def get_article():
    return jsonify({
        "data":all_articles[0],
        "status":"success"
    }),

@app.route("/liked-articles", methods=["POST"])
def liked_article():
    all_articles = all_articles[1:]
    movie = all_articles[0]
    liked_articles.append(movie)
    return jsonify({
        "status":"success"
    }),

@app.route("/unliked-articles",methods=["POST"])
def unliked_article():
    article=all_articles[0]
    all_articles=all_articles[1:]
    not_liked_articles.append(article)
    return jsonify({
        "status":"success"
    }),

@app.route("/did-not-watch",methods=["POST"])
def did_not_watch():
    article=all_articles[0]
    all_articles=all_articles[1:]
    did_not_watch.append(article)
    return jsonify({
        "status":"success"
    }),

if __name__ == "__main__":
    app.run()
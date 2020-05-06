import json

from flask import Flask
import pymongo

app = Flask(__name__)


@app.route("/")
def index_page():
  return "This is a website about FullThrottle"

@app.route("/about")
def about_page():
  return "This is a website about FullThrottle"


@app.route("/users")
def users_data():
      myclient = pymongo.MongoClient("mongodb+srv://priyanka:0Pbkc5kZNoD9JPa7@cluster0-csn6y.mongodb.net/test?retryWrites=true&w=majority")
      print("Connection established")
      mydb = myclient["test"]
      collection = mydb["users"]
      documents = collection.find()
      print("Fetched the data")
      response = []
      for document in documents:
          document['_id'] = str(document['_id'])
          response.append(document)
      print("returning the data")
      return json.dumps(response)

@app.errorhandler(404)
def page_not_found(e):
    return  "The Page you are searching for couldn't be found"

if __name__ == '__main__':
    app.run(port=8140,debug=True,host='0.0.0.0')
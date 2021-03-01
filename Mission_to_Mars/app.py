from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import scrape_mission_to_mars

# Create an instance of Flask
app = Flask(__name__)

mongo = PyMongo(app, uri="mongodb://localhost:27017/mission_mars")

# Route to render index.html template using data from Mongo
@app.route("/")
def home():

    # Find one record of data from the mongo database
    destination_data = mongo.db.collection.find_one()
    print(destination_data)
    # Return template and data
    return render_template("index.html", vacation = destination_data)

# Route that will trigger the scrape function
@app.route("/scrape")
def scrape():
    print('\n\nScrap was called!')
    # Run the scrape function
    mars_data = scrape_mission_to_mars.scrape_info()

    # Update the Mongo database using update and upsert = True
    mongo.db.collection.update({}, mars_data, upsert = True)

    # Redirect back to home page
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)
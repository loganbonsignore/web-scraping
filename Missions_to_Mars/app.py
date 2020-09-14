from flask import Flask, jsonify, render_template
import scrape_mars
import pymongo
import random
from numpy import arange

app = Flask(__name__)
client = pymongo.MongoClient("mongodb://localhost:27017")
db = client.mars_db.mission_to_mars

@app.route("/")
def mars_data():
    scrape_mars.scrape()                      
    mars_data = db.find().sort([("_id", -1)]).limit(1)[0]
                  
    return render_template("index.html", news_titles=mars_data["news_titles"][0], \
        news_paragraphs=mars_data["news_paragraphs"][0], \
        featured_image_url=mars_data["featured_image_url"], \
        table=mars_data["mars_facts_table_html"], \
        hemisphere_list=mars_data["hemisphere_list"] 
    )
                        

if __name__ == "__main__":
    app.run(debug=True)
# import necessary libraries
from flask import Flask, render_template

# create instance of Flask app
app = Flask(__name__)


# create route that renders index.html template
@app.route("/")
def index():
    
    movie_list = [{"name":"Mighty Ducks","url":"https://www.imdb.com/title/tt0104868/?ref_=nv_sr_srsg_3"},
     {"name":"Space Jam","url":"https://www.imdb.com/title/tt0104868/?ref_=nv_sr_srsg_3"}, 
     {"name":"Clerks","url":"https://www.imdb.com/title/tt0104868/?ref_=nv_sr_srsg_3"},
      {"name":"Batman","url":"https://www.imdb.com/title/tt0104868/?ref_=nv_sr_srsg_3"},
       {"name":"Avengers","url":"https://www.imdb.com/title/tt0104868/?ref_=nv_sr_srsg_3"},
       
       ]
    
    
    return render_template("index.html", list=movie_list )


if __name__ == "__main__":
    app.run(debug=True)

"""
~ Name: x
~ Class: x
~ Date: x
~ Description:  x
"""


"""
import(s)
"""
# import flask
from flask import Flask, render_template, request, url_for, redirect

# import bootstrap
from flask_bootstrap import Bootstrap5

# import the pillow image stuff
from PIL import Image

# import requests for API usage
####  need to install requests to import "pip install requests" ####
import requests

# import random for random number generation
import random


"""
functions
"""
# main program
def main():

    # create Flask instance
    app = Flask(__name__)

    # create Boostrap instance
    bootstrap = Bootstrap5(app)


    # function for generating random number
    def rando():
     
     return random.randint(0, 29)
    

    # route - default
    # (home page)
    @app.route('/')
    def home():

        # render a basic HTML template for the home page
        return render_template("home.html")

    # route - test
    # (test page for checking nav bar
    @app.route('/test')
    def test():

        # render a test page for linking check
        return render_template("test.html")


    # route - api
    # opens page for selecting api image
    @app.route('/apipage', methods=('GET', 'POST'))
    def apipage():
        random_id = rando()

        if request.method == "POST":
            random_id = request.form['random_id']
            return redirect(url_for("editHome", random_id=random_id))

        return render_template("apipage.html", random_id=random_id)
    
    @app.route('/editHome')
    def editHome():
        random_id = request.args.get('random_id')

        return render_template("editHome.html", random_id=random_id)



    # start the Flask server
    app.run(debug=True)


"""
program start here
"""
if __name__ == "__main__":
    main()

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
from flask import Flask, render_template

# import bootstrap
from flask_bootstrap import Bootstrap5

# import the pillow image stuff
from PIL import Image


"""
functions
"""
# main program
def main():

    # create Flask instance
    app = Flask(__name__)

    # create Boostrap instance
    bootstrap = Bootstrap5(app)

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

    # start the Flask server
    app.run(debug=True)


"""
program start here
"""
if __name__ == "__main__":
    main()

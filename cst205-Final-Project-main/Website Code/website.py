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

# import shututil for downloading image
import shutil
import os


"""
functions
"""
# main program
def main():

    # create Flask instance
    app = Flask(__name__)

    #create upload folder
    app.config['UPLOAD_FOLDER'] = 'static/uploads'

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

    # route - upload
    # opens page for uploading local image
    @app.route('/upload', methods=['GET', 'POST'])
    def upload():
        if request.method == 'POST':
            if 'file' not in request.files:
                return "No file part"
            
            file = request.files['file']
            if file.filename == '':
                return "No selected file"
            
            if file:
                filename = file.filename
                filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
                file.save(filepath)

                return redirect(url_for('editHome', filename=filename, uploaded="true"))

        return render_template("upload.html")
    # route - api
    # opens page for selecting api image
    @app.route('/apipage', methods=('GET', 'POST'))
    def apipage():
        random_id = rando()
        if request.method == "POST":
            random_id = request.form['random_id']

            image_url = f"https://picsum.photos/id/{random_id}/800/600.jpg"
            filename = f"api_{random_id}.jpg"
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            response = requests.get(image_url, stream=True)
            with open(filepath, 'wb') as out_file:
                shutil.copyfileobj(response.raw, out_file)

            return redirect(url_for("editHome", filename=filename, downloaded = "true"))

        return render_template("apipage.html", random_id=random_id)
    # route - edit
    # opens page for editing image
    @app.route('/editHome', methods=['GET', 'POST'])
    def editHome():
        filename = request.args.get('filename')
        downloaded = request.args.get('downloaded') == "true"
        uploaded = request.args.get('uploaded') == "true"
        image_path = os.path.join(app.config['UPLOAD_FOLDER'], filename) if filename else None

        if request.method == 'POST':
            action = request.form.get('action')
            width = int(request.form.get('width', 0))
            height = int(request.form.get('height', 0))

            if image_path and os.path.exists(image_path):
                img = Image.open(image_path)

                if action == 'resize' and width > 0 and height > 0:
                    img = img.resize((width, height))
                elif action == 'crop':
                    img = img.crop((0, 0, width, height))

                edited_path = os.path.join('static/edited', filename)
                img.save(edited_path)

                return render_template("editHome.html", image_path=f"edited/{filename}", edited=True, downloaded=False)


        return render_template("editHome.html", image_path=f"uploads/{filename}" if filename else None, downloaded = downloaded, edited = False, uploaded=uploaded)



    # start the Flask server
    app.run(debug=True)


"""
program start here
"""
if __name__ == "__main__":
    main()

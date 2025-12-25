from flask import Flask, render_template, request
import uuid 
from werkzeug.utils import secure_filename
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

UPLOAD_FOLDER = os.path.join(BASE_DIR, 'user_uploads')

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/create", methods=["GET", "POST"])
def create():
    myid=uuid.uuid1()
    if request.method == "POST":
        print(request.files.keys())
        received_uuid = request.form.get(uuid)
        description = request.form.get("text")
        input_files = []
        for key, values in request.files.items():
            print(key, values)

            file = request.files[key]
            if file:
                filename = secure_filename(file.filename)
                if not os.path.exists(os.path.join(app.config['UPLOAD_FOLDER'], str(myid))):
                    os.makedirs(os.path.join(app.config['UPLOAD_FOLDER'], str(myid)), exist_ok=True)
                    file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
                    input_files.append(file.filename)
            #capturing the description 
            with open(os.path.join(app.config['UPLOAD_FOLDER'], str(myid), 'description.txt'), 'w') as f:
                f.write(description)

        for file in input_files:
            with open(os.path.join(app.config['UPLOAD_FOLDER'], received_uuid, "input.txt"), 'a') as f:
                f.write(f"file'{file}'\nduration 1\n")
                
    
    return render_template("create.html", myid=myid)

@app.route("/gallery")
def gallery():
    reels = os.listdir("static/reels")
    print(reels)
    return render_template("gallery.html", reels=reels)

app.run(debug=True)
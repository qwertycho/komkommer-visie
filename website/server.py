import os
from flask import Flask, flash, request, redirect, url_for
from flask import render_template
import PIL
from PIL import Image
import main2

UPLOAD_FOLDER = './uploads'
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}

secret_key = os.urandom(32)

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['secret_key'] = secret_key

# set static folder
app.static_folder = './uploads'

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


def schaal(filename):
    outputPath = "./uploads/predict"
    inputPath = "./uploads"

    newSize = 500
    maxSize = 500
    i = 0

    oldImage = PIL.Image.open(inputPath + "/" + filename)
    oldImage.thumbnail((500,500), PIL.Image.Resampling.LANCZOS)

    widthOfset = int((maxSize - oldImage.size[0]) / 2)
    heightOfset = int((maxSize - oldImage.size[1]) / 2)

    newImage = PIL.Image.new("RGB", (maxSize, maxSize), (255, 255, 255))
    newImage.paste(oldImage, (widthOfset, heightOfset))

    newImage.save(outputPath + "/" + filename)





@app.route('/predict',methods=['POST']) 
def upload_file():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # if user does not select file, browser also
        # submit an empty part without filename
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = file.filename
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            schaal(filename)
            return redirect('/predict?filename='+filename)
   

@app.route('/predict')
def predict():
    filename = request.args.get('filename')
    prediction = main2.predict(filename)
    return render_template('predict.html', filename=filename, prediction=prediction)

@app.route('/') 
def func(): 
        return render_template('index.html')



if __name__=='__main__': 
       app.debug=True 
       app.run() 



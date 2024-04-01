from flask import Flask, render_template, request, redirect, url_for
import os
from main import *
import os
from gradio_client import Client
import json

app = Flask(__name__)
UPLOAD_FOLDER = 'static/uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/')
def home():
    # Get list of uploaded files
    uploaded_files = os.listdir(app.config['UPLOAD_FOLDER'])
    # Render home template with uploaded files list
    return render_template('upload.html', uploaded_files=uploaded_files)

@app.route('/upload', methods=['GET', 'POST'])
def upload_image():
    if 'image' not in request.files:
        return redirect(request.url)
    image = request.files['image']
    if image.filename == '':
        return redirect(request.url)
    if image:
        filename = image.filename
        image.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        return redirect(url_for('home'))

@app.route('/images')
def display_images():
    images = os.listdir(app.config['UPLOAD_FOLDER'])
    return render_template('images.html', images=images)

@app.route('/clear')
def clear_uploads_folder():
    """
    Clears all files in the uploads folder.
    """
    uploaded_files = os.listdir(app.config['UPLOAD_FOLDER'])
    for file in uploaded_files:
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], file)
        if os.path.exists(file_path):
            os.remove(file_path)
    return redirect(url_for('home'))

@app.route('/generate')
def generate():
    """
    uploaded_files = os.listdir(app.config['UPLOAD_FOLDER'])   
    print(uploaded_files)
    client = Client("https://lambdalabs-image-mixer-demo.hf.space/")
    if len(uploaded_files) == 1:
        result = client.predict(
            "Image",	# str  in 'Input 0 type' Radio component
            "Image",	# str  in 'Input 1 type' Radio component
            "Image",	# str  in 'Input 2 type' Radio component
            "Image",	# str  in 'Input 3 type' Radio component
            "Image",	# str  in 'Input 4 type' Radio component
            "Howdy!",	# str  in 'Text or Image URL' Textbox component
            "Howdy!",	# str  in 'Text or Image URL' Textbox component
            "Howdy!",	# str  in 'Text or Image URL' Textbox component
            "Howdy!",	# str  in 'Text or Image URL' Textbox component
            "Howdy!",	# str  in 'Text or Image URL' Textbox component
            UPLOAD_FOLDER +"/"+ uploaded_files[0],	# str (filepath or URL to image) in 'Image' Image component
            "https://raw.githubusercontent.com/gradio-app/gradio/main/test/test_files/bus.png",	# str (filepath or URL to image) in 'Image' Image component
            "https://raw.githubusercontent.com/gradio-app/gradio/main/test/test_files/bus.png",	# str (filepath or URL to image) in 'Image' Image component
            "https://raw.githubusercontent.com/gradio-app/gradio/main/test/test_files/bus.png",	# str (filepath or URL to image) in 'Image' Image component
            "https://raw.githubusercontent.com/gradio-app/gradio/main/test/test_files/bus.png",	# str (filepath or URL to image) in 'Image' Image component
            1,	# int | float (numeric value between 0 and 5) in 'Strength' Slider component
            0,	# int | float (numeric value between 0 and 5) in 'Strength' Slider component
            0,	# int | float (numeric value between 0 and 5) in 'Strength' Slider component
            0,	# int | float (numeric value between 0 and 5) in 'Strength' Slider component
            0,	# int | float (numeric value between 0 and 5) in 'Strength' Slider component
            1,	# int | float (numeric value between 1 and 10) in 'CFG scale' Slider component
            1,	# int | float (numeric value between 1 and 1) in 'Num samples' Slider component
            0,	# int | float (numeric value between 0 and 10000) in 'Seed' Slider component
            10,	# int | float (numeric value between 10 and 100) in 'Steps' Slider component
            fn_index=5
        )
    
    if len(uploaded_files) ==2:
        result = client.predict(
            "Image",	# str  in 'Input 0 type' Radio component
            "Image",	# str  in 'Input 1 type' Radio component
            "Image",	# str  in 'Input 2 type' Radio component
            "Image",	# str  in 'Input 3 type' Radio component
            "Image",	# str  in 'Input 4 type' Radio component
            "Howdy!",	# str  in 'Text or Image URL' Textbox component
            "Howdy!",	# str  in 'Text or Image URL' Textbox component
            "Howdy!",	# str  in 'Text or Image URL' Textbox component
            "Howdy!",	# str  in 'Text or Image URL' Textbox component
            "Howdy!",	# str  in 'Text or Image URL' Textbox component
            UPLOAD_FOLDER +"/"+ uploaded_files[0],	# str (filepath or URL to image) in 'Image' Image component
            UPLOAD_FOLDER +"/"+uploaded_files[1],	# str (filepath or URL to image) in 'Image' Image component
            "https://raw.githubusercontent.com/gradio-app/gradio/main/test/test_files/bus.png",	# str (filepath or URL to image) in 'Image' Image component
            "https://raw.githubusercontent.com/gradio-app/gradio/main/test/test_files/bus.png",	# str (filepath or URL to image) in 'Image' Image component
            "https://raw.githubusercontent.com/gradio-app/gradio/main/test/test_files/bus.png",	# str (filepath or URL to image) in 'Image' Image component
            1,	# int | float (numeric value between 0 and 5) in 'Strength' Slider component
            1,	# int | float (numeric value between 0 and 5) in 'Strength' Slider component
            0,	# int | float (numeric value between 0 and 5) in 'Strength' Slider component
            0,	# int | float (numeric value between 0 and 5) in 'Strength' Slider component
            0,	# int | float (numeric value between 0 and 5) in 'Strength' Slider component
            1,	# int | float (numeric value between 1 and 10) in 'CFG scale' Slider component
            1,	# int | float (numeric value between 1 and 1) in 'Num samples' Slider component
            0,	# int | float (numeric value between 0 and 10000) in 'Seed' Slider component
            10,	# int | float (numeric value between 10 and 100) in 'Steps' Slider component
        )
    if len(uploaded_files) ==3: 
        result = client.predict(
            "Image",	# str  in 'Input 0 type' Radio component
            "Image",	# str  in 'Input 1 type' Radio component
            "Image",	# str  in 'Input 2 type' Radio component
            "Image",	# str  in 'Input 3 type' Radio component
            "Image",	# str  in 'Input 4 type' Radio component
            "Howdy!",	# str  in 'Text or Image URL' Textbox component
            "Howdy!",	# str  in 'Text or Image URL' Textbox component
            "Howdy!",	# str  in 'Text or Image URL' Textbox component
            "Howdy!",	# str  in 'Text or Image URL' Textbox component
            "Howdy!",	# str  in 'Text or Image URL' Textbox component
            UPLOAD_FOLDER +"/"+ uploaded_files[0],	# str (filepath or URL to image) in 'Image' Image component
            UPLOAD_FOLDER +"/"+ uploaded_files[1],	# str (filepath or URL to image) in 'Image' Image component
            UPLOAD_FOLDER +"/"+ uploaded_files[2],	# str (filepath or URL to image) in 'Image' Image component
            "https://raw.githubusercontent.com/gradio-app/gradio/main/test/test_files/bus.png",	# str (filepath or URL to image) in 'Image' Image component
            "https://raw.githubusercontent.com/gradio-app/gradio/main/test/test_files/bus.png",	# str (filepath or URL to image) in 'Image' Image component
            1,	# int | float (numeric value between 0 and 5) in 'Strength' Slider component
            1,	# int | float (numeric value between 0 and 5) in 'Strength' Slider component
            1,	# int | float (numeric value between 0 and 5) in 'Strength' Slider component
            0,	# int | float (numeric value between 0 and 5) in 'Strength' Slider component
            0,	# int | float (numeric value between 0 and 5) in 'Strength' Slider component
            1,	# int | float (numeric value between 1 and 10) in 'CFG scale' Slider component
            1,	# int | float (numeric value between 1 and 1) in 'Num samples' Slider component
            0,	# int | float (numeric value between 0 and 10000) in 'Seed' Slider component
            10,	# int | float (numeric value between 10 and 100) in 'Steps' Slider component
        )
    if len(uploaded_files) ==4:
        result = client.predict(
            "Image",	# str  in 'Input 0 type' Radio component
            "Image",	# str  in 'Input 1 type' Radio component
            "Image",	# str  in 'Input 2 type' Radio component
            "Image",	# str  in 'Input 3 type' Radio component
            "Image",	# str  in 'Input 4 type' Radio component
            "Howdy!",	# str  in 'Text or Image URL' Textbox component
            "Howdy!",	# str  in 'Text or Image URL' Textbox component
            "Howdy!",	# str  in 'Text or Image URL' Textbox component
            "Howdy!",	# str  in 'Text or Image URL' Textbox component
            "Howdy!",	# str  in 'Text or Image URL' Textbox component
            UPLOAD_FOLDER +"/"+ uploaded_files[0],	# str (filepath or URL to image) in 'Image' Image component
            UPLOAD_FOLDER +"/"+ uploaded_files[1],	# str (filepath or URL to image) in 'Image' Image component
            UPLOAD_FOLDER +"/"+ uploaded_files[2],	# str (filepath or URL to image) in 'Image' Image component
            UPLOAD_FOLDER +"/"+ uploaded_files[3],	# str (filepath or URL to image) in 'Image' Image component
            "https://raw.githubusercontent.com/gradio-app/gradio/main/test/test_files/bus.png",	# str (filepath or URL to image) in 'Image' Image component
            1,	# int | float (numeric value between 0 and 5) in 'Strength' Slider component
            1,	# int | float (numeric value between 0 and 5) in 'Strength' Slider component
            1,	# int | float (numeric value between 0 and 5) in 'Strength' Slider component
            1,	# int | float (numeric value between 0 and 5) in 'Strength' Slider component
            0,	# int | float (numeric value between 0 and 5) in 'Strength' Slider component
            1,	# int | float (numeric value between 1 and 10) in 'CFG scale' Slider component
            1,	# int | float (numeric value between 1 and 1) in 'Num samples' Slider component
            0,	# int | float (numeric value between 0 and 10000) in 'Seed' Slider component
            10,	# int | float (numeric value between 10 and 100) in 'Steps' Slider component
        )
    if len(uploaded_files) ==5:		
        result = client.predict(
            "Image",	# str  in 'Input 0 type' Radio component
            "Image",	# str  in 'Input 1 type' Radio component
            "Image",	# str  in 'Input 2 type' Radio component
            "Image",	# str  in 'Input 3 type' Radio component
            "Image",	# str  in 'Input 4 type' Radio component
            "Howdy!",	# str  in 'Text or Image URL' Textbox component
            "Howdy!",	# str  in 'Text or Image URL' Textbox component
            "Howdy!",	# str  in 'Text or Image URL' Textbox component
            "Howdy!",	# str  in 'Text or Image URL' Textbox component
            "Howdy!",	# str  in 'Text or Image URL' Textbox component
            UPLOAD_FOLDER +"/"+ uploaded_files[0],	# str (filepath or URL to image) in 'Image' Image component
            UPLOAD_FOLDER +"/"+ uploaded_files[1],	# str (filepath or URL to image) in 'Image' Image component
            UPLOAD_FOLDER +"/"+ uploaded_files[2],	# str (filepath or URL to image) in 'Image' Image component
            UPLOAD_FOLDER +"/"+ uploaded_files[3],	# str (filepath or URL to image) in 'Image' Image component
            UPLOAD_FOLDER +"/"+ uploaded_files[4],	# str (filepath or URL to image) in 'Image' Image component
            1,	# int | float (numeric value between 0 and 5) in 'Strength' Slider component
            1,	# int | float (numeric value between 0 and 5) in 'Strength' Slider component
            1,	# int | float (numeric value between 0 and 5) in 'Strength' Slider component
            1,	# int | float (numeric value between 0 and 5) in 'Strength' Slider component
            1,	# int | float (numeric value between 0 and 5) in 'Strength' Slider component
            1,	# int | float (numeric value between 1 and 10) in 'CFG scale' Slider component
            1,	# int | float (numeric value between 1 and 1) in 'Num samples' Slider component
            0,	# int | float (numeric value between 0 and 10000) in 'Seed' Slider component
            10,	# int | float (numeric value between 10 and 100) in 'Steps' Slider component
        )
			"""	
    #jsonpath = result+"/captions.json"
    #with open(jsonpath, 'r') as file:
    #    jsonfile = json.load(file)
    #for path in jsonfile:
    image_path = "/Users"+"/private/var/folders/_s/rlywhg8537vgn2r2p7zlc5fr0000gn/T/gradio/f9160ee6-ab2c-4b11-ab04-35c8f6d7c766/62462b6d5a07a3cbbb033ebe9bdc2a5cc688d6ff/image.png"
    return render_template('image.html', image_path=image_path)

if __name__ == '__main__':
    app.run(debug=True, port = 8000)

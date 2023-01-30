# import flask -> pip install flask
from flask import Flask, render_template, request

# import lib
import tensorflow as tf
from tensorflow import keras
from keras.models import load_model
from keras.preprocessing import image
import numpy as np

app = Flask(__name__)

#dictionary untuk label
dic = {0 : "ass", 1 : "breast", 2 : "female", 3 : "male", 4 : "neutral", 5 : "nudity", 6 : "toys"}

#load modelweights
model = load_model('API\weights00050-120922.h5')

#model memprediksi
model.make_predict_function()

#predict function
def predict_label(img_path):
    i = image.load_img(img_path, target_size=(224,224))
    i = image.img_to_array(i)/255.0
    i = i.reshape(1, 224,224,3)
    p = model.predict(i)
    new_p = np.argmax(p,axis=1)
    return dic[new_p[0]]


# main routes
@app.route("/", methods=['GET', 'POST'])
def main():
    return render_template("index.html")

# output routes
@app.route("/submit", methods=['GET', 'POST'])
def get_output():
    if request.method == 'POST':
        img = request.files['my_image']

        #store to folder .../static/
        img_path = "static/" + img.filename
        img.save(img_path)

        #predict gambarnya
        p = predict_label(img_path)

    return render_template("index.html", prediction = p, img_path = img_path)


if __name__ =='__main__':
    	#app.debug = True
	app.run(debug = True)
from flask import Flask, request, render_template
from flask_cors import cross_origin
import jsonify
import sklearn
import pickle
import pandas as pd

app = Flask(__name__)
model = pickle.load(open('fish_weight_prediction.pkl','rb'))


@app.route('/',methods=['GET'])
def home():
    return render_template('home.html')

@app.route('/predict', methods=['POST'])
def predict():
    if  request.method == 'POST':
        Vertical_length_in_cm = float(request.form['Vertical_Length_in_cm'])
        Diagonal_length_in_cm = float(request.form['Diagonal_length_in_cm'])
        Height_in_cm = float(request.form['Height_in_cm'])
        Diagonal_width_in_cm = float(request.form['Diagonal_width_in_cm'])

        Species = request.form['Species']
        if(Species=='Bream'):
            Bream = 1
            Parkki = 0
            Perch = 0
            Pike = 0
            Roach = 0
            Smelt = 0
            Whitefish = 0

        elif(Species=='Parkki'):
            Bream = 0
            Parkki = 1
            Perch = 0
            Pike = 0
            Roach = 0
            Smelt = 0
            Whitefish = 0

        elif(Species=='Perch'):
            Bream = 0
            Parkki = 0
            Perch = 1
            Pike = 0
            Roach = 0
            Smelt = 0
            Whitefish = 0

        elif(Species=='Pike'):
            Bream = 0
            Parkki = 0
            Perch = 0
            Pike = 1
            Roach = 0
            Smelt = 0
            Whitefish = 0

        elif(Species=='Roach'):
            Bream = 0
            Parkki = 0
            Perch = 0
            Pike = 0
            Roach = 1
            Smelt = 0
            Whitefish = 0

        elif(Species=='Smelt'):
            Bream = 0
            Parkki = 0
            Perch = 0
            Pike = 0
            Roach = 0
            Smelt = 1
            Whitefish = 0

        elif(Species=='Whitefish'):
            Bream = 0
            Parkki = 0
            Perch = 0
            Pike = 0
            Roach = 0
            Smelt = 0
            Whitefish = 1

        else:
            Bream = 0
            Parkki = 0
            Perch = 0
            Pike = 0
            Roach = 0
            Smelt = 0
            Whitefish = 0

        prediction = model.predict([[Vertical_length_in_cm,Diagonal_length_in_cm,Height_in_cm,
                          Diagonal_width_in_cm,Bream,Parkki,Perch,Pike,Roach,Smelt,Whitefish]])

        output=round(prediction[0],2)

        return render_template('home.html',prediction_text = 'The weight of the fish is {} grams'.format(output))

    return render_template('home.html')






if __name__ == '__main__':
    app.run(debug=True)

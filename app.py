#importing libraries
import pickle
import numpy
from flask import Flask, request, render_template

#Global Var
app = Flask(__name__)
loadedModel = pickle.load(open('wine.pkl','rb'))

#user defined func
@app.route('/',methods =['GET'])
def Home(): 
    return render_template('index.html')


@app.route('/prediction',methods= ['POST'])

def predict():
    Citric_Acid = float(request.form['Citric_Acid'])
    Fixed_Acidity = float(request.form["Fixed_Acidity"])
    Total_Sulfur_Dioxide = float(request.form["Total_Sulfur_Dioxide"])
    Volatile_Acidity = float(request.form["Volatile_Acidity"])

    Sulphates = float(request.form["Sulphates"])
    Alcohol = float(request.form["Alcohol"])
    Density = float(request.form["Density"])


    prediction = loadedModel.predict([[Fixed_Acidity, Volatile_Acidity, Citric_Acid, Total_Sulfur_Dioxide,Density, Sulphates, Alcohol]])

    if prediction == [0]:
        prediction = "Not Good"
    elif prediction == [1]:
        prediction = "Good"
    else:
        prediction = 'Not Sure'         

    return render_template('index.html', output = prediction)



#main function
if __name__ == '__main__':    
    app.run(debug=True)
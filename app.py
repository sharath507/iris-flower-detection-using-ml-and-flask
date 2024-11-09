from flask import Flask, render_template, request
import joblib
from sklearn.datasets import load_iris

iris = load_iris()


app = Flask(__name__)

# Load the trained model
model = joblib.load('model.joblib')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    sepal_length = float(request.form['sepal_length'])
    sepal_width = float(request.form['sepal_width'])
    petal_length = float(request.form['petal_length'])
    petal_width = float(request.form['petal_width'])

    # Make prediction
    prediction = model.predict([[sepal_length, sepal_width, petal_length, petal_width]])[0]
    flower_type = iris.target_names[prediction]
    
    return render_template('index.html', prediction=flower_type)

if __name__ == '__main__':
    app.run(host="0.0.0.0",port = "8000" ,debug=True)

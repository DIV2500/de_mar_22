from unittest import result
from flask import Flask, request
from flasgger import Swagger
import pickle
from sklearn.linear_model import LogisticRegression

app = Flask(__name__)  #constructor of flask --compulsory
Swagger(app)

pickled_model_file=open("pickle_iris_model.pkl","rb")
classifier=pickle.load(pickled_model_file)

@app.route('/')   #decorators
def home():
    return "welcome to iris classifier"

@app.route('/predict')
def predict_flower():

    """Predict the Iris flower category
    ---
    parameters:
        - name: Sepal_width
          in: query
          type: number
          required: true  
        - name: Sepal_length
          in: query
          type: number
          required: true 
        - name: Petal_width
          in: query
          type: number
          required: true 
        - name: Petal_length
          in: query
          type: number
          required: true 
    responses:
        200:
             description: The result is                  
    """

    sw=request.args.get('Sepal_width')
    sl=request.args.get('Sepal_length')
    pw=request.args.get('Petal_width')
    pl=request.args.get('Petal_length')  

    result=classifier.predict([[sw,sl,pw,pl]])

    return f"The prediction is that  the flower is {result}"

if __name__=="__main__":   #calling the constructor
    app.run()  #can put port 8000 inside run default 5000 ,host=0.0.0.0 see main2
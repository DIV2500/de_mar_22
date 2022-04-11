from flask import Flask, request
from flasgger import Swagger

app = Flask(__name__)  #constructor of flask --compulsory

@app.route('/')
def base_route():  #base path will give this message
    return "Welcome to Praxis"  

@app.route("/my_name/<name>")   #if add this in address get this message
def print_name(name):
    return f"Welcome to Praxis Happy learning {name} in Nagpur"

@app.route("/hello", methods=["GET","POST"])
def hello():
    try :
        stu_name = request.args.get("StudentName")   #arguments to be passed
        numb = request.args.get("RollNo")
        #return "Oops something went wrong", 400
        
        return f"Student name is {stu_name} and roll no is {numb}", 200 #new response code
         #http://192.168.1.35:8000/hello?StudentName=Anchal&RollNo=1
    except Exception as e :
        return f" Error occuredd with message : {e}", 401
     
if __name__=="__main__":   #calling the constructor
    app.run(host="0.0.0.0",port=8000,debug=True)   #can remove debug see in main
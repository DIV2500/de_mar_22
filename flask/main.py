from flask import Flask, request
from flasgger import Swagger

app = Flask(__name__)  #constructor of flask --compulsory
Swagger(app)

@app.route('/')
def base_route():  #base path will give this message
    return "Welcome to Praxis"  

@app.route("/my_name/<name>")  #if add this in address get this message
def print_name(name):
    return f"Welcome to Praxis Happy learning {name} in Nagpur"

@app.route("/hello", methods=["GET","POST"])  #get and post methods
# type this in link http://192.168.1.35:8000/hello?StudentName=Anchal&RollNo=1
def hello():
            #swagger defined format below to see gui in apidocs seeing two request as both GET AND POST in code
    """Lets try Swagger from flasgger
    ---
    parameters:
        - name: StudentName
          in: query
          type: string
          required: true  
        - name: RollNo
          in: query
          type: string
          required: true
    responses:
        200:
            description: The result is    
    """
    try :
        stu_name = request.args.get("StudentName")   #arguments to be passed
        numb = request.args.get("RollNo")
        #return "Oops something went wrong", 400
        
        return f"Student name is {stu_name} and roll no is {numb}", 201
    except Exception as e :
        return f" Error occuredd with message : {e}", 401

if __name__=="__main__":   #calling the constructor
    app.run()  #can put port 8000 inside run default 5000 ,host=0.0.0.0 see main2

#get link click on it to get result ,add---/apidocs to see swagger version
#127.0.0.1 local host
#with response codes get to know what happened with it
#here see 200 means OK
#CAN  COPY ADDRESS TO POSTMAN RUN IN GET AND SEE RESULT
##SEE NOTES !!! FOR EXPLANATION
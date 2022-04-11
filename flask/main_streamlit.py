from flask import Flask, request
import streamlit as st


def hello():
    try :
        st.title("learning streamlit")
        stu_name = st.text_input("StudentName")   
        numb = st.text_input("RollNo")
        result=f"Student name is {stu_name}and roll number is {numb}"
        if st.button("Print Output"):
            st.success(result)
    except Exception as e :
        return f" Error occuredd with message : {e}"

if __name__=="__main__":   #calling the constructor
    hello()  #can put port 8000 inside run default 5000 ,host=0.0.0.0 see main2

#get link click on it to get result ,add---/apidocs to see swagger version
#127.0.0.1 local host
#with response codes get to know what happened with it
#here see 200 means OK
#CAN  COPY ADDRESS TO POSTMAN RUN IN GET AND SEE RESULT
##SEE NOTES !!! FOR EXPLANATION
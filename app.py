from flask import Flask , render_template , request 
import json
import urllib.request

app = Flask(__name__)

@app.route('/' , methods = ['POST' , 'GET'])
def index():
    return render_template('weather.html' , data=[{'name':'New Delhi'} , {'name' : 'Mumbai'} , {'name' : 'Kolkata'} , {'name' : 'Bangalore'} , {'name' : 'Chennai'} , {'name' : 'Hyderabad'} , {'name' : 'Bhopal'}])


if __name__ == '__main__'
app.run(debug = True)

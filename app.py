from flask import Flask , render_template , request 
import json
import urllib.request

app = Flask(__name__)

@app.route('/' , methods = ['POST' , 'GET'])

def weather():
    if request.method == 'POST':
        city = request.form('city')
    else:
        city = 'Mumbai'

    api = "64e1b6ec71msh79f17be5fb5db5dp1ecd69jsnb974c96d020c"
    source = urllib.request.urlopen("https://community-open-weather-map.p.rapidapi.com/find")

    ##response = requests.request("GET", url, headers=headers, params=querystring)
        # converting JSON data to a dictionary 
    list_of_data = json.loads(source) 
  
    # data for variable list_of_data 
    data = { 
        "country_code": str(list_of_data['sys']['country']), 
        "coordinate": str(list_of_data['coord']['lon']) + ' ' 
                    + str(list_of_data['coord']['lat']), 
        "temp": str(list_of_data['main']['temp']) + 'k', 
        "pressure": str(list_of_data['main']['pressure']), 
        "humidity": str(list_of_data['main']['humidity']), 
    } 
    print(data) 
    return render_template('index.html', data = data) 
  
  
  
if __name__ == '__main__': 
    app.run(debug = True) 

  
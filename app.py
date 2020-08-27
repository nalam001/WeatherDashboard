import requests
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def weather_dashboard():
    return render_template("home.html")

@app.route('/results', methods=['POST'])
def return_results():
    zip_code = request.form['zipcode']
    data = get_weather_results(zip_code, "3c195f88f2b5332c421ae8dd55ae467e")
    temp = "{0:.2f}".format(data["main"]["temp"]) 
    weather = data["weather"][0]["main"] 
    location = data["name"] 
    return render_template('results.html', location=location, temp=temp, weather=weather)

def get_weather_results(zip_code, api_key):
    api_url = "http://api.openweathermap.org/data/2.5/weather?zip={}&units=imperial&appid={}".format(zip_code, api_key)
    r = requests.get(api_url)
    return r.json()

if (__name__) == '__main__': app.run()

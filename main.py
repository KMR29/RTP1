import requests
from flask import Flask, request,render_template

app = Flask(__name__,template_folder="templates")

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')
@app.route('/result',methods=['POST'])
def result():
    # Get the weather data from the OpenWeatherMap API
    api_key = '14e262c919b62b2c750cdff38051a239'
    city = request.form['city']
    print("city is",city)
    api_url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}'
    r = requests.get(api_url)
    weather_data = r.json()
    print("fetched bro",weather_data)
    weather = {
        'city': city,
        'temperature': round(weather_data['main']['temp']-273,2),
        'description': weather_data['weather'][0]['description'],
        'icon': weather_data['weather'][0]['icon'],
    }
    return render_template('weather.html',weather=weather)

if __name__ == '__main__':
    app.run()

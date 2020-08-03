from flask import Flask, render_template, request
import datetime
import requests
import json


app = Flask(__name__)





@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        woah_add = "https://api.covid19api.com/dayone/country/"
        countries = request.form['countries']
        url = woah_add + countries
        json_data = requests.get(url).json()
        wow = json_data[0]


        return render_template('covid_tracker.html', json_data=json_data, wow=wow)
    return render_template('index.html')


if __name__ == "__main__":
    app.run(debug=True)

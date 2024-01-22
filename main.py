from flask import Flask, request, render_template
import pickle
from xgboost import XGBClassifier

with open('model.pkl', 'rb') as f:
    model = pickle.load(f)

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    precipitation = float(request.form['precipitation'])
    temp_max = float(request.form['temp_max'])
    temp_min = float(request.form['temp_min'])
    wind= float(request.form['wind'])

    prediction = model.predict([[precipitation, temp_max, temp_min, wind]])[0]

    if prediction == 0:
        weather_type = 'Drizzle'
    elif prediction == 1:
        weather_type = 'Foggy'
    elif prediction == 2:
        weather_type = 'Rainy'
    elif prediction == 3:
        weather_type = 'Snowy'
    else:
        prediction = 'Sunny'
    return render_template('index.html', result=weather_type)

if __name__ == '__main__':
    app.run(debug=True)
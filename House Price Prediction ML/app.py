from flask import Flask, render_template, request
import sklearn
import pandas as pd
import pickle
app = Flask(__name__)
data = pd.read_csv('Cleaned_Data_Final.csv')
pipe = pickle.load(open("RidgeModel.pkl", 'rb'))


@app.route('/')
def index():
    
    locations = sorted(data.location.unique())
    return render_template('index.html', locations = locations)

@app.route('/predict', methods=['POST'])
def predict():
    location = request.form.get('location')
    bhk = request.form.get('bhk')
    bath = request.form.get('bath')
    sqft = request.form.get('tsqft')
    try:
        bhk = int(bhk)
        bath = int(bath)
        sqft = float(sqft)
    except (ValueError, TypeError):
        return "Invalid input. Please provide numeric values for BHK, bath, and square footage."
    print(location, bhk, bath, sqft)

    input_data = pd.DataFrame([[location, sqft, bath, bhk]], columns=['location', 'total_sqft', 'bath', 'bhk'])
    prediction = pipe.predict(input_data)[0] * 100000

    return str(round(prediction, 2))


if __name__ == "__main__":
    app.run(debug=True)
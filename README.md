# House-Price-Prediction
### Project Overview
House Price Prediction Web Application in Flask
The House Price Prediction project is a web-based application designed to estimate the price of residential properties based on various input features. Utilizing a Ridge regression model, this application provides users with a straightforward interface to input property details and obtain a predicted price.

### Key Features:
- User-Friendly Interface: A web form allows users to input details such as location, total square foot, number of bathrooms, and number of bedrooms.
- Accurate Predictions: The model, trained on a comprehensive dataset of Bengaluru housing prices, delivers predictions with notable accuracy.
- Real-Time Results: Once the user submits the form, the application immediately returns the predicted price of the property.
  
### Technical Details:
- Machine Learning Model: The project employs Ridge regression, a type of linear regression with L2 regularization, to predict house prices. The model was trained on a cleaned dataset, which was preprocessed to handle missing values, remove outliers, remove invalid data, and encode categorical features.
- Data Preprocessing: The dataset underwent significant preprocessing including feature engineering, outlier removal, invalid data removal, and conversion of categorical variables into numerical format using one-hot encoding.
- Web Application: Built using Flask, the application provides a clean interface for users to interact with the model. It integrates with a Python backend to process input data, perform predictions, and return results.

### How It Works:
- Input: Users enter property details into the web form.
- Processing: The input data is processed by the Flask application, which utilizes the trained Ridge regression model to generate predictions.
- Output: The predicted price is displayed to the user on the same page.
  
### Model Performance:
- Mean Absolute Error (MAE): 19.35
- Mean Squared Error (MSE): 1866.75
- R-squared (R2): 0.80


## Set Up and Instructions
1. Create a virtual environment to manage dependencies and avoid conflicts with other Python projects
2. Activate the virtual environment: venv\Scripts\activate
3. Start the Flask application by running: python app.py
4. Open a web browser you will see the user input form where you can enter house details.

## Libraries and Versions
This project uses the following libraries:

- Flask: 2.2.3 – A web framework for Python.
- NumPy: 1.26.4 – A library for numerical computations.
- Pandas: 1.3.4 – A library for data manipulation and analysis.
- scikit-learn: 0.24.2 – A library for machine learning.
- Matplotlib: 3.7.1 – A library for creating static, animated, and interactive visualizations.
- Seaborn: 0.12.2 – A statistical data visualization library based on Matplotlib.
- Plotly: 5.15.0 – A library for interactive plotting.

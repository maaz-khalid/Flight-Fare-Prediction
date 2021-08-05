# Flight Fare Prediction Web App deployed on Heroku

Model fitting is done using Random Forest.

Accuracy on test data is 80% and for train data it goes to 95%.

The deployed web app is live [here.](https://predict-fare-flight.herokuapp.com/)

The web app predicts the airfare between source and destination based on departure details, arrival details, number of stops and choice of airline.

Airlines included: Air Asia, Air India, GoAir, Indigo, Jet Airways, Spicejet and Vistara.

Cities included: Bangalore, Chennai, Delhi, Kolkata, Mumbai, Hyderabad, Cochin.

The web app was built in Python using the following libraries:
* streamlit
* pickle
* numpy
* datetime

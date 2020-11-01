from flask import Flask , render_template,request
import pickle
from sklearn.linear_model import LinearRegression
import numpy as np
app = Flask(__name__)
model = pickle.load(open('college.pkl', 'rb'))


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():

    int_features = [int(x) for x in request.form.values()]
    final_features = [np.array(int_features)]
    prediction = model.predict(final_features)

    output = prediction[0][0].round(2)

    return render_template('index.html', prediction_text='Chance of Getting Admission is  {}%'.format(output))

    
if __name__=='__main__':
    app.run(debug=True)
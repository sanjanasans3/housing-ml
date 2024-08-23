from distutils.log import debug
import pickle
from flask import Flask , render_template, request

app = Flask(__name__)
model = pickle.load(open('model.pkl','rb'))


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['GET','POST'])
def predict():
    # try:
        prediction = model.predict([[float(request.form.get('area'))]])
        output = round(prediction[0], 2)
        return render_template('index.html',prediction_text=f'Total price:{output}')
    # except:
    #     return render_template('index.html',prediction_text="Something went wrong")

if __name__ == '__main__':
    app.run(host="0.0.0.0",port=5000)
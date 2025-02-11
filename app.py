from flask import Flask, request, render_template
import pickle

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
    data=[]
    features = request.form["predict"]
    data.append(features)
    
    model = pickle.load(open('./phishing.pkl', 'rb'))
    result = model.predict(data)
    if result[0]=="bad":
        return render_template('index.html', prediction_text="This is a phising site")
    else:
        return render_template('index.html', prediction_text="This is not a phising site")


if __name__ == "__main__":
    app.run(debug=True)
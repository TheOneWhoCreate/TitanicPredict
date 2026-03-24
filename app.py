from flask import Flask, render_template, request
import pickle
import pandas as pd

app = Flask(__name__)

model = pickle.load(open("titanic_model.pkl", "rb"))

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])

def predict():
    Pclass = int(request.form["Pclass"])
    Sex = request.form["Sex"]
    Age = float(request.form["Age"])
    SibSp = int(request.form["SibSp"])
    Parch = int(request.form["Parch"])
    Fare = float(request.form["Fare"])
    Embarked = request.form["Embarked"]

    FamilySize = SibSp + Parch + 1
    isAlone = 1 if FamilySize == 1 else 0
    MotherChild = 1 if (Sex == "female" and Parch > 0) else 0

    data = pd.DataFrame({
        "Pclass":[Pclass],
        "Sex":[Sex],
        "Age":[Age],
        "SibSp":[SibSp],
        "Parch":[Parch],
        "Fare":[Fare],
        "Embarked":[Embarked],
        "FamilySize":[FamilySize],
        "isAlone":[isAlone],
        "MotherChild":[MotherChild]
    })

    probs = model.predict_proba(data)[0]
    prediction = probs.argmax()
    prob = probs[1]

    result = "Survived" if prediction == 1 else "Did Not Survive"

    return render_template(
        "index.html",
        result=result,
        probability=round(prob*100,2)
    )

if __name__ == "__main__":
    app.run(debug=True)
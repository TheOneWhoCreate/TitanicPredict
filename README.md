# 🚢 Titanic Survival Prediction Web App

A simple **Machine Learning web application** built using **Flask** that predicts whether a passenger would survive the Titanic disaster based on input features.

---

## 📌 Overview

This project uses a trained ML model (`titanic_model.pkl`) to predict survival probability based on passenger details such as:

* Passenger Class
* Gender
* Age
* Family details
* Fare
* Port of Embarkation

It also performs **feature engineering** before making predictions.

---

## ⚙️ Tech Stack

* **Backend:** Flask (Python)
* **Frontend:** HTML, CSS
* **ML Model:** Pickle (`.pkl`)
* **Data Processing:** Pandas

---

## 🚀 Features

* User-friendly web interface
* Real-time prediction
* Displays:

  * Survival result (Survived / Did Not Survive)
  * Survival probability (%)
* Custom feature engineering:

  * `FamilySize`
  * `isAlone`
  * `MotherChild`

---

## 🧠 Model Input Features

| Feature     | Description                       |
| ----------- | --------------------------------- |
| Pclass      | Passenger class (1–3)             |
| Sex         | Gender (male/female)              |
| Age         | Age of passenger                  |
| SibSp       | Number of siblings/spouses aboard |
| Parch       | Number of parents/children aboard |
| Fare        | Ticket fare                       |
| Embarked    | Port (S, C, Q)                    |
| FamilySize  | SibSp + Parch + 1                 |
| isAlone     | 1 if alone, else 0                |
| MotherChild | 1 if female with children         |

---

## 🖥️ How It Works

1. User fills out the form on the web page.
2. Data is sent to Flask backend (`/predict` route).
3. Feature engineering is applied.
4. Model predicts survival probability using:
5. Result is displayed on the webpage.

---

## ▶️ Running the Project

### 1. Clone the repository

```bash
git clone https://github.com/your-username/titanic-survival-predictor.git
cd titanic-survival-predictor
```

### 2. Install dependencies

```bash
pip install flask pandas
```

### 3. Run the app

```bash
python app.py
```

### 4. Open in browser

```
http://127.0.0.1:5000/
```

---

## 📸 UI Description

* Input form with passenger details
* Dropdowns for categorical inputs
* Result section showing:

  * Prediction
  * Probability score

---

## 📈 Output Example

```
Result: Survived
Survival Probability: 78.45%
```

---

## 🤝 Contributing

Feel free to fork this repo and improve the project!

---

## 📜 License

This project is open-source

---

## 💡 Author

**Atanu Rooj**

---


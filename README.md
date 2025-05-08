# 🔧 Fault Detection in Sensors

This project uses a Machine Learning model to detect **machine faults** using sensor data such as temperature, torque, and tool wear. Built as part of a research effort in **Applied AI for Predictive Maintenance**.

---

## 🚀 Demo (Streamlit App)

Run the app locally using:
streamlit run app.py

🧠 ML Model
Algorithm: Random Forest Classifier

Features Used:

Air temperature [K]

Process temperature [K]

Rotational speed [rpm]

Torque [Nm]

Tool wear [min]

Target: machine_failure (0 = No Failure, 1 = Failure)



🗂️ Project Structure

fault_detection_sensors/
├── app.py                     ← Streamlit frontend
├── fault_detection_model.pkl  ← Trained ML model
├── data/
│   └── machine_failure.csv    ← Dataset from Kaggle
├── requirements.txt           ← Python dependencies
└── README.md                  ← Project documentation

📦 Installation
Clone the repository or download it as ZIP.

Open a terminal inside the project folder.

(Optional) Create a virtual environment:

python -m venv venv
venv\Scripts\activate   # On Windows
Install dependencies:

pip install -r requirements.txt


📊 Dataset
Source: Kaggle – Machine Failure Dataset

Place the downloaded machine_failure.csv inside the data/ folder.

✅ Sample Prediction
The app lets you enter live sensor values and provides a prediction on whether the machine is likely to fail.

💾 Save & Load Model
The model is saved using:

joblib.dump(model, 'fault_detection_model.pkl')
It is then loaded inside the Streamlit app for real-time predictions.

📌 Requirements
Python 3.8+

Streamlit

Pandas

NumPy

Seaborn

Scikit-learn

Matplotlib

Joblib

(All listed in requirements.txt) 

check it in: http://localhost:8502/

👨‍🔬 Author
Name: Bhumika Shriwas

Focus: Applied AI for Predictive Maintenance

📃 License
This project is for educational and research purposes only. Commercial use is not permitted without prior approval.





# 🔧 Fault Detection in Sensors 

This project uses a Machine Learning model to detect **machine faults** using sensor data like temperature, torque, and tool wear. 


## 🚀 Demo (Streamlit App)

You can run the app locally using:

```bash
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
csharp
Copy
Edit
fault_detection_sensors/
├── app.py                     ← Streamlit frontend
├── fault_detection_model.pkl  ← Trained ML model
├── data/
│   └── machine_failure.csv    ← Dataset from Kaggle
├── requirements.txt           ← Python dependencies
└── README.md                  ← Project documentation
📦 Installation
Clone the repository or download it as ZIP.

Open a terminal in the project folder.

(Optional) Create a virtual environment:

bash
Copy
Edit
python -m venv venv
venv\Scripts\activate   # On Windows
Install dependencies:

bash
Copy
Edit
pip install -r requirements.txt
📊 Dataset
Source: Kaggle - Machine Failure Dataset

Place the downloaded machine_failure.csv inside the /data/ folder.

✅ Sample Prediction
The app allows you to input live sensor values and predicts whether the machine is likely to fail.

💾 Save & Load Model
The trained model is saved using:

python
Copy
Edit
joblib.dump(model, 'fault_detection_model.pkl')
And loaded in the Streamlit app to make real-time predictions.

📌 Requirements
Python 3.8+

Streamlit

Pandas

NumPy

Seaborn

Scikit-learn

Matplotlib

Joblib

(Full list in requirements.txt)

👨‍🔬 Author
Name: [Your Bhumika Shriwas]

Field: Applied AI for Predictive Maintenance

📃 License
This project is for educational and research purposes only. Commercial use is not permitted without prior approval.
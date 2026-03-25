# 🎫 AI Support Ticket Classification System

An end-to-end Machine Learning project that classifies customer support tickets and assigns priority levels using NLP techniques, with an interactive Streamlit dashboard.

---

## 🌐 Live Demo
👉 https://futureml02-main-nuhsyqsbdrw9djrxcsrptz.streamlit.app/

---

## 🚀 Features

- 🧠 NLP-based text preprocessing  
- 📂 Ticket classification (Billing, Technical, Delivery)  
- ⚡ Priority detection (High / Medium / Low)  
- 📊 Interactive dashboard with analytics  
- 📈 Timeline analysis of predictions  
- 🔴 Live ticket simulation  
- 📥 Downloadable reports  

---

## 🛠️ Tech Stack

- Python  
- Scikit-learn  
- NLTK  
- Streamlit  
- Pandas  
- Matplotlib  

---

## 📂 Project Structure

FUTURE_ML_02-MAIN/
│
├── dashboard/ # Streamlit app
├── src/ # ML logic (train, predict, preprocess)
├── data/ # Dataset
├── models/ # Trained model
├── config.py
├── requirements.txt


---

## ⚙️ How to Run Locally

```bash
# Clone repo
git clone https://github.com/HASHWIK/FUTURE_ML_02-MAIN.git

# Navigate
cd FUTURE_ML_02-MAIN

# Install dependencies
pip install -r requirements.txt

# Train model
python -m src.train

# Run app
streamlit run dashboard/app.py

## 📂 Project Structure

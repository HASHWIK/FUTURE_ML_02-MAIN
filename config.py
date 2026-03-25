import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

DATA_PATH = os.path.join(BASE_DIR, "data", "tickets.csv")
MODEL_PATH = os.path.join(BASE_DIR, "models", "ticket_model.pkl")
REPORT_PATH = os.path.join(BASE_DIR, "reports", "model_report.txt")
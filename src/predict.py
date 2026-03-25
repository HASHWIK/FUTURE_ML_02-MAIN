import joblib
import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from src.preprocess import clean_text
from config import MODEL_PATH

model = joblib.load(MODEL_PATH)

# Issue description logic
def get_issue_description(text):
    text = text.lower()

    if "payment" in text or "refund" in text or "charged" in text:
        return "💳 Payment-related issue"

    elif "login" in text or "password" in text:
        return "🔐 Authentication issue"

    elif "server" in text or "error" in text or "crash" in text:
        return "🖥️ Server/technical issue"

    elif "delivery" in text or "order" in text:
        return "📦 Delivery/order issue"

    else:
        return "ℹ️ General issue"

def predict_ticket(text):
    cleaned = clean_text(text)

    proba = model.predict_proba([cleaned])[0]
    confidence = round(max(proba) * 100, 2)

    category = model.predict([cleaned])[0]

    text_lower = text.lower()

    if any(w in text_lower for w in ["error", "failed", "crash", "not working"]):
        priority = "🔴 High"
    elif any(w in text_lower for w in ["late", "delay"]):
        priority = "🟠 Medium"
    else:
        priority = "🟢 Low"

    issue_desc = get_issue_description(text)

    return category, priority, cleaned, confidence, issue_desc
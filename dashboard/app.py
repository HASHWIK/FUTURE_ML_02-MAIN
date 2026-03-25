import streamlit as st
import sys
import os
import pandas as pd
import matplotlib.pyplot as plt
import time
import random

# -----------------------------
# FIX PATH
# -----------------------------
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from src.predict import predict_ticket

# -----------------------------
# PAGE CONFIG
# -----------------------------
st.set_page_config(page_title="AI Support Dashboard", layout="wide")

# -----------------------------
# 🎨 PREMIUM STYLE + HOVER
# -----------------------------
st.markdown("""
<style>
.stApp {
    background: linear-gradient(135deg, #0f172a, #020617);
    color: white;
}

/* Buttons */
div.stButton > button {
    background-color: #1f2937;
    color: white;
    border-radius: 10px;
    padding: 10px;
    transition: all 0.3s ease;
}

/* Hover effect */
div.stButton > button:hover {
    background-color: #3b82f6;
    transform: scale(1.05);
    box-shadow: 0px 0px 15px rgba(59,130,246,0.7);
}
</style>
""", unsafe_allow_html=True)

# =====================================================
# TITLE
# =====================================================
st.title("🎫 AI Support Ticket Dashboard")
st.markdown("Select a sample ticket to analyze")

# =====================================================
# SAMPLE TICKETS
# =====================================================
tickets = [
    "Payment failed but amount deducted",
    "App crashes on login",
    "Order not delivered",
    "Late delivery issue",
    "Unable to login account",
    "Refund not processed",
    "Server error during checkout"
]

selected_ticket = None
cols = st.columns(3)

for i, ticket in enumerate(tickets):
    if cols[i % 3].button(ticket):
        selected_ticket = ticket

# =====================================================
# ANALYSIS
# =====================================================
if selected_ticket:

    category, priority, cleaned, confidence, issue_desc = predict_ticket(selected_ticket)

    st.markdown("## 📌 Results")

    col1, col2, col3 = st.columns(3)
    col1.metric("📂 Category", category)
    col2.metric("⚡ Priority", priority)
    col3.metric("🎯 Confidence", f"{confidence}%")

    # -----------------------------
    # AI INSIGHT
    # -----------------------------
    st.markdown("## 🤖 AI Insight")

    st.info(f"""
    ✔ Ticket: {selected_ticket}  
    ✔ Category: {category}  
    ✔ Priority: {priority}  
    ✔ Issue Type: {issue_desc}  
    ✔ Cleaned Text: {cleaned}  
    """)

    # =====================================================
    # MULTI TICKET ANALYSIS
    # =====================================================
    st.markdown("## 📋 Ticket Monitoring")

    sample_data = [
        "Payment failed",
        "App crash",
        "Late delivery",
        "Refund issue",
        "Login error",
        "Server down"
    ]

    results = []
    for t in sample_data:
        c, p, _, conf, _ = predict_ticket(t)
        results.append({
            "Ticket": t,
            "Category": c,
            "Priority": p,
            "Confidence": conf
        })

    df = pd.DataFrame(results)

    st.dataframe(df, use_container_width=True)

    # -----------------------------
    # DOWNLOAD REPORT
    # -----------------------------
    st.download_button(
        "📥 Download Report",
        df.to_csv(index=False),
        "ticket_report.csv"
    )

    # =====================================================
    # 📊 ANALYTICS
    # =====================================================
    st.markdown("## 📊 Analytics")

    col1, col2 = st.columns(2)

    # Donut Chart
    with col1:
        fig, ax = plt.subplots()
        counts = df["Priority"].value_counts()
        ax.pie(counts, labels=counts.index, autopct='%1.1f%%')
        centre_circle = plt.Circle((0, 0), 0.70, fc='black')
        fig.gca().add_artist(centre_circle)
        st.pyplot(fig)

    # Bar Chart
    with col2:
        st.bar_chart(df["Category"].value_counts())

    # =====================================================
    # 📈 TIMELINE CHART
    # =====================================================
    st.markdown("## 📈 Ticket Timeline Analysis")

    timeline_df = df.copy()
    timeline_df["Time"] = pd.date_range(end=pd.Timestamp.now(), periods=len(df))
    timeline_df = timeline_df.sort_values("Time")

    st.line_chart(
        timeline_df.set_index("Time")["Confidence"]
    )

    # =====================================================
    # 🔴 LIVE STREAM
    # =====================================================
    st.markdown("## 🔴 Live Ticket Stream")

    placeholder = st.empty()

    for i in range(5):
        t = random.choice(sample_data)
        c, p, _, _, _ = predict_ticket(t)
        placeholder.write(f"🆕 {t} → {c} ({p})")
        time.sleep(1)

    # =====================================================
    # KPI
    # =====================================================
    st.markdown("## 🚀 System Overview")

    col1, col2, col3 = st.columns(3)
    col1.metric("Total Tickets", len(df))
    col2.metric("High Priority", (df["Priority"] == "🔴 High").sum())
    col3.metric("System Health", "Good")

# -----------------------------
# FOOTER
# -----------------------------
st.markdown("---")
st.markdown("💎 AI Dashboard | Interactive + Timeline Enabled | Task 2 ✅")
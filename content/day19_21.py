import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from diagrams import pipeline_flow

def render():
    st.title("🚀 Day 19-21: Practice Project")
    st.caption("Foundations · Topic 6 · Apply everything you've learned")

    st.markdown(
        '<div class="notebox"><b>Goal:</b> Combine Python, statistics, data cleaning, and ML concepts into one mini hands-on project.</div>',
        unsafe_allow_html=True
    )

    st.header("1. The Project Pipeline")
    st.write("Every real ML project follows this same journey, no matter how big or small:")

    st.graphviz_chart(
        pipeline_flow(
            ["Collect Data", "Clean Data", "Split Train/Test", "Train Model", "Check Accuracy", "Predict New Data"],
            colors=["#fecaca", "#fde68a", "#bae6fd", "#bbf7d0", "#ddd6fe", "#86efac"]
        )
    )

    st.markdown(
        '<div class="dashedbox">🏠 <b>Real-life framing:</b> Imagine you\'re a junior analyst at a real estate company. Your manager says: "Given a house\'s size and bedrooms, tell me what price we should list it at." This project walks through exactly how you\'d approach that.</div>',
        unsafe_allow_html=True
    )

    st.header("2. Step 1 — Collect Data")
    st.write("Here's a small sample dataset of houses already sold:")

    house_df = pd.DataFrame({
        "Size (sqft)": [800, 1000, 1200, 1500, 1800, 2000, 2400, 2800],
        "Bedrooms": [2, 2, 3, 3, 4, 4, 5, 5],
        "Price (₹ Lakhs)": [40, 48, 58, 70, 85, 92, 110, 125]
    })
    st.dataframe(house_df, use_container_width=True)

    st.header("3. Step 2 — Explore & Visualize")
    st.write("Before building any model, ALWAYS look at your data visually first.")

    fig, ax = plt.subplots(figsize=(6, 3.5))
    ax.scatter(house_df["Size (sqft)"], house_df["Price (₹ Lakhs)"], s=100, color="#3C6E8F", edgecolor="black")
    ax.set_xlabel("Size (sqft)")
    ax.set_ylabel("Price (₹ Lakhs)")
    ax.set_title("Bigger house → Higher price? Let's see the pattern")
    st.pyplot(fig)

    st.markdown(
        '<div class="notebox">📈 Notice the pattern: as size goes up, price goes up too — a straight-line-ish relationship. This tells us <b>Linear Regression</b> could work well here.</div>',
        unsafe_allow_html=True
    )

    st.header("4. Step 3 — Split Train/Test")
    st.write("""
    We NEVER test a model on the same data it learned from — that's like giving a student 
    the exam answers before the test and then being surprised they got 100%.

    So we split data into:
    - **Training set** (e.g., 80%) — model learns from this
    - **Testing set** (e.g., 20%) — model is tested on this, data it has NEVER seen
    """)

    train_pct = st.slider("Choose train/test split %", 50, 90, 80, step=10)
    n_total = len(house_df)
    n_train = int(n_total * train_pct / 100)
    n_test = n_total - n_train

    col1, col2 = st.columns(2)
    col1.metric("Training rows", n_train)
    col2.metric("Testing rows", n_test)

    st.header("5. Step 4 — Train a Simple Model")
    st.write("Here we build a basic linear regression formula using your data (behind the scenes, real ML libraries do this automatically):")

    # simple manual linear regression calc for teaching purposes
    x = house_df["Size (sqft)"].values
    y = house_df["Price (₹ Lakhs)"].values
    slope = np.polyfit(x, y, 1)[0]
    intercept = np.polyfit(x, y, 1)[1]

    st.code(f"Price = {slope:.4f} × Size + {intercept:.2f}", language="text")

    st.header("6. Step 5 — Predict New Data")
    st.write("Now let's use our trained formula to predict the price of a NEW house:")

    new_size = st.slider("Enter new house size (sqft)", 500, 3500, 1600, step=100)
    predicted_price = slope * new_size + intercept

    st.metric("Predicted Price", f"₹{predicted_price:.1f} Lakhs")

    fig2, ax2 = plt.subplots(figsize=(6, 3.5))
    ax2.scatter(x, y, s=100, color="#3C6E8F", edgecolor="black", label="Known houses")
    ax2.plot(x, slope*x + intercept, color="#C9553D", linewidth=2, label="Model's learned line")
    ax2.scatter([new_size], [predicted_price], s=200, color="#F2D062", edgecolor="black", marker="*", label="Your prediction")
    ax2.legend()
    ax2.set_xlabel("Size (sqft)")
    ax2.set_ylabel("Price (₹ Lakhs)")
    st.pyplot(fig2)

    st.header("7. Alternative Project — Email Classifier")
    st.write("If you'd rather practice classification instead of regression, try this:")

    email_samples = pd.DataFrame({
        "Email": ["Win free money now!", "Meeting rescheduled to 3pm", "URGENT: claim your prize", "Please review attached report"],
        "Actual Label": ["Spam", "Not Spam", "Spam", "Not Spam"]
    })
    st.dataframe(email_samples, use_container_width=True)
    st.write("Apply the same pipeline: collect → clean → split → train → test → predict — just with text data and a Classification model instead of Regression.")

    st.header("8. Beginner glossary recap")
    st.markdown("""
    - **Training set** — data the model learns from
    - **Testing set** — unseen data used to check if model actually learned
    - **Overfitting** — model memorizes training data but fails on new data (like memorizing answers without understanding)
    - **Model accuracy** — how often the model's predictions are correct
    """)

    st.header("📺 Tamil beginner-friendly resources")
    st.info("""
    Search these on YouTube:
    - **Bharathi Yuvan linear regression project Tamil**
    - **KTC machine learning project Tamil**
    """)

    st.header("✅ Module 1 Final Quiz (Mixed Review)")
    questions = [
        ("What's the difference between AI, ML and DL in one line?",
         "AI = smart machines in general, ML = learns from data, DL = ML using brain-like neural networks."),
        ("Which Python library is like 'Excel inside code'?", "pandas"),
        ("Predicting house price — Regression or Classification?", "Regression, because the output is a number."),
        ("Why do we split data into Train/Test before training?",
         "To check if the model actually learned the pattern, using data it has never seen before — not just memorized answers."),
        ("What happens if we skip data cleaning?",
         "The model may learn wrong patterns from messy/incorrect data — 'garbage in, garbage out.'"),
    ]
    for i, (q, a) in enumerate(questions, 1):
        with st.expander(f"Q{i}: {q}"):
            st.success(f"✅ {a}")

    st.success("🎉 **Congratulations! You've completed Phase 1: Foundations!**")
    st.info("📌 **Next phase:** Core Machine Learning — Regression, Classification, Ensemble Methods")

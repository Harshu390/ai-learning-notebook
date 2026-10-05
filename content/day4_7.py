import streamlit as st
import pandas as pd
from diagrams import bar_chart_example

def render():
    st.title("🐍 Day 4-7: Python Basics for AI (numpy & pandas)")
    st.caption("Foundations · Topic 2 · numpy & pandas for absolute beginners")

    st.markdown('<div class="notebox"><b>Goal:</b> Understand why AI uses Python, and what numpy/pandas actually do — zero coding background needed.</div>', unsafe_allow_html=True)

    st.header("1. Why Python for AI?")
    st.write("Python reads almost like plain English. That's why beginners AND experts love it.")

    st.markdown('<div class="dashedbox">💡 Think of Python as the <b>kitchen</b>. numpy and pandas are <b>appliances</b> — numpy is the blender (fast number crunching), pandas is the organized pantry shelf (neatly labeled data).</div>', unsafe_allow_html=True)

    st.header("2. What is numpy? (the super calculator)")
    st.write("**numpy** handles lists of numbers and does math on ALL of them at once — super fast.")
    st.markdown("**📦 Real-life example:** A shop has 1,000 items and wants to add 18% tax to every price.")

    col1, col2 = st.columns(2)
    with col1:
        st.markdown("**🐌 Without numpy**")
        st.write("Calculate each price one-by-one — slow and tiring")
        st.pyplot(bar_chart_example(["Item 1", "Item 2", "...", "Item 1000"], [1, 1, 1, 1],
                                     "Time (manual, one by one)", "Relative time", color="#fca5a5"))
    with col2:
        st.markdown("**⚡ With numpy**")
        st.write("ALL 1,000 prices updated in one instant step!")
        st.pyplot(bar_chart_example(["All 1000 items"], [1],
                                     "Time (numpy, all at once)", "Relative time", color="#86efac"))

    st.header("3. What is pandas? (the digital notebook)")
    st.write("**pandas** = Python's version of an Excel spreadsheet, but far more powerful.")
    st.markdown("**📦 Real-life example:** A teacher's notebook with student names, marks, and city:")

    sample_df = pd.DataFrame({
        "Name": ["Asha", "Ravi", "Meera", "Karthik"],
        "Marks": [88, 95, 76, 91],
        "City": ["Delhi", "Pune", "Chennai", "Madurai"]
    })
    st.dataframe(sample_df, use_container_width=True)
    st.caption("👆 This whole table is called a 'DataFrame' in pandas")

    st.write("**🎛️ Try it yourself — filter students live:**")
    min_marks = st.slider("Show students who scored above:", 0, 100, 80)
    filtered = sample_df[sample_df["Marks"] > min_marks]
    st.dataframe(filtered, use_container_width=True)
    st.caption("✨ That filter is pandas doing its job — instantly, with real logic!")

    st.header("4. numpy vs pandas — side by side")
    st.markdown("""
    | Feature | numpy 🧮 | pandas 📊 |
    |---|---|---|
    | Best for | Fast math on numbers | Organizing labeled data (tables) |
    | Looks like | A list/grid of plain numbers | An Excel sheet with column names |
    | Real job | Calculating, resizing images, stats | Cleaning, filtering, analyzing datasets |
    """)

    st.markdown('<div class="notebox">🤝 In real projects, you almost always use <b>both together</b> — pandas organizes the data, numpy works quietly underneath doing the math.</div>', unsafe_allow_html=True)

    st.header("5. Reading Real Data (CSV files)")
    st.write("Most real-world data comes as a **CSV** (Comma-Separated Values) file — a simple text version of a spreadsheet.")
    st.code("""Name,Marks,City
Asha,88,Delhi
Ravi,95,Pune""", language="text")
    st.write("pandas opens this instantly into a neat table you can search, sort, and analyze.")

    st.header("✅ Practice Questions")
    questions = [
        ("Which tool is best described as 'Excel inside Python'?", "pandas"),
        ("What does CSV stand for?", "Comma-Separated Values"),
        ("True/False: numpy and pandas are themselves AI models.",
         "False — they are data tools used to PREPARE data before training any AI model."),
        ("In a table, what's the difference between a row and a column?",
         "A row = one record (e.g., one student, read across). A column = one category of info (e.g., 'Marks', read down)."),
    ]
    for i, (q, a) in enumerate(questions, 1):
        with st.expander(f"Q{i}: {q}"):
            st.success(f"✅ {a}")

    st.info("📌 **Next topic:** Statistics & Probability Essentials")

import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from diagrams import cleaning_pipeline


def _messy_data():
    return pd.DataFrame({
        "Name":  ["Asha", "Ravi", "asha", "Meera", "Karthik", "Divya", "Ravi"],
        "Age":   ["25", "31", "25", None, "twenty-eight", "29", "31"],
        "City":  ["Chennai", "pune", "Chennai", "Delhi", "CHENNAI", None, "pune"],
        "Salary": [45000, 52000, 45000, 48000, 51000, 9999999, 52000],
    })


def render():
    st.title("🧹 Day 11-14: Data Cleaning & Visualization")
    st.caption("Foundations · Topic 4 · matplotlib & seaborn · the job you'll actually spend 70% of your time on")

    st.markdown('<div class="notebox"><b>Goal:</b> Learn to spot messy data, fix it step by step, '
                'and then pick the <b>right chart</b> to tell the story. '
                'Professionals spend more time here than on the AI model itself.</div>',
                unsafe_allow_html=True)

    # ---------------------------------------------------------
    st.header("1. Why cleaning comes before everything else")
    st.markdown('<div class="dashedbox">🍳 <b>Kitchen analogy:</b> No chef cooks with rotten vegetables and '
                'unwashed rice, no matter how expensive the stove is. Your AI model is the stove; '
                'your data is the ingredients. <b>Garbage in → garbage out.</b></div>', unsafe_allow_html=True)

    st.write("Here is the standard cleaning journey every data person follows:")
    st.graphviz_chart(cleaning_pipeline())

    # ---------------------------------------------------------
    st.header("2. Meet a messy dataset")
    st.write("This is an HR file from a small company. It looks fine at a glance — but it has **five different problems**. "
             "Can you spot them before scrolling?")

    df = _messy_data()
    st.dataframe(df, use_container_width=True)

    with st.expander("🔍 Reveal the 5 problems"):
        st.markdown("""
        1. **Duplicate rows** — Ravi (31, pune) appears twice. Asha appears twice with different capitalisation.
        2. **Missing values** — Meera has no Age, Divya has no City (shown as `None`).
        3. **Wrong data type** — Age is stored as *text* (`"25"`), so you cannot do maths on it.
        4. **Inconsistent text** — `Chennai`, `CHENNAI`, `pune`, `Delhi` — the computer treats these as different cities!
        5. **An outlier / typo** — one salary is ₹99,99,999. Almost certainly a data-entry mistake.
        """)

    # ---------------------------------------------------------
    st.header("3. 🎛️ Clean it, one step at a time")
    st.write("Pick a cleaning step below and see exactly what changes:")

    step = st.radio(
        "Choose a cleaning action:",
        ["0 — Original messy data",
         "1 — Standardise text (lowercase + trim)",
         "2 — Remove duplicate rows",
         "3 — Fix the Age column (text → number)",
         "4 — Fill missing values",
         "5 — Handle the outlier salary"],
        index=0)

    work = _messy_data()

    if step >= "1":
        work["Name"] = work["Name"].str.strip().str.title()
        work["City"] = work["City"].str.strip().str.title() if work["City"].notna().any() else work["City"]
    if step >= "2":
        work = work.drop_duplicates(subset=["Name", "Salary"]).reset_index(drop=True)
    if step >= "3":
        work["Age"] = pd.to_numeric(work["Age"], errors="coerce")
    if step >= "4":
        work["Age"] = work["Age"].fillna(work["Age"].median())
        work["City"] = work["City"].fillna("Unknown")
    if step >= "5":
        cap = work["Salary"].median() * 3
        work.loc[work["Salary"] > cap, "Salary"] = work["Salary"].median()

    st.dataframe(work, use_container_width=True)

    explanations = {
        "0": "👀 This is where every real project starts. Never assume data is clean.",
        "1": "✅ `Chennai`, `CHENNAI` and `chennai` are now ONE city. Text consistency first — otherwise duplicates hide from you.",
        "2": "✅ Duplicate rows removed. Duplicates make your model think some examples are twice as important as they really are.",
        "3": "✅ Age is now a real number. `'twenty-eight'` could not be converted, so it became empty (NaN) — that's fine, we fix it next.",
        "4": "✅ Missing ages filled with the **median** age; missing cities labelled `Unknown`. "
             "We used median (not mean) because it isn't dragged around by outliers — remember Day 8-10!",
        "5": "✅ The ₹99,99,999 typo was replaced with the median salary. "
             "One crazy value can ruin an entire model's predictions.",
    }
    st.markdown(f'<div class="notebox">{explanations[step[0]]}</div>', unsafe_allow_html=True)

    st.markdown("""
    **The 3 ways to handle missing values (choose based on situation):**
    | Method | When to use it | Risk |
    |---|---|---|
    | **Delete the row** | Only a tiny % of rows are missing | You lose data |
    | **Fill with mean/median** | Numbers like age, price, temperature | Reduces natural variety |
    | **Fill with "Unknown"** | Text/categories like city, gender | Creates a new category |
    """)

    # ---------------------------------------------------------
    st.header("4. Visualization — which chart for which job?")
    st.markdown('<div class="dashedbox">📰 <b>Real-life reason:</b> Your manager will never read 10,000 rows. '
                'But they will understand one good chart in 5 seconds. '
                'Choosing the wrong chart is like telling a story in the wrong language.</div>',
                unsafe_allow_html=True)

    goal = st.selectbox("What do you want to show?",
                        ["Compare categories (which city pays most?)",
                         "Show a trend over time (sales per month)",
                         "Show the shape/spread of one column (ages)",
                         "Show a relationship between two numbers (experience vs salary)",
                         "Show how strongly columns relate (correlation heatmap)"])

    rng = np.random.default_rng(42)
    fig, ax = plt.subplots(figsize=(6, 3.4))

    if goal.startswith("Compare"):
        ax.bar(["Chennai", "Pune", "Delhi", "Madurai"], [52, 61, 70, 44],
               color="#60a5fa", edgecolor="black")
        ax.set_ylabel("Avg salary (₹ thousands)")
        chart_name, why = "📊 **Bar Chart**", "Bars are easiest for the human eye to compare side by side."
    elif goal.startswith("Show a trend"):
        ax.plot(["Jan", "Feb", "Mar", "Apr", "May", "Jun"], [30, 34, 31, 42, 48, 55],
                marker="o", color="#16a34a", lw=2.5)
        ax.set_ylabel("Sales (lakhs)")
        chart_name, why = "📈 **Line Chart**", "Lines show movement and direction over time better than anything else."
    elif goal.startswith("Show the shape"):
        ax.hist(rng.normal(32, 7, 400), bins=18, color="#f59e0b", edgecolor="black")
        ax.set_xlabel("Age"); ax.set_ylabel("How many people")
        chart_name, why = "📶 **Histogram**", "Shows where most of your data sits — your bell curve from Day 8-10!"
    elif goal.startswith("Show a relationship"):
        x = rng.uniform(0, 15, 60); y = 25 + 3.2 * x + rng.normal(0, 6, 60)
        ax.scatter(x, y, color="#a855f7", s=55, edgecolor="black")
        ax.set_xlabel("Years of experience"); ax.set_ylabel("Salary (₹ thousands)")
        chart_name, why = "⚫ **Scatter Plot**", "Each dot is one person — instantly reveals if two things move together."
    else:
        data = pd.DataFrame({
            "Age": rng.normal(32, 6, 100),
            "Experience": rng.normal(8, 3, 100),
            "Salary": rng.normal(55, 12, 100),
        })
        data["Salary"] += data["Experience"] * 2.5
        plt.close(fig)
        fig, ax = plt.subplots(figsize=(4.6, 3.6))
        sns.heatmap(data.corr(), annot=True, cmap="YlGnBu", ax=ax, fmt=".2f")
        chart_name, why = "🔥 **Heatmap (seaborn)**", "Red/dark squares = strongly related columns. Great for picking useful features later."

    plt.tight_layout()
    st.pyplot(fig)
    st.markdown(f'<div class="notebox">Use a {chart_name} — {why}</div>', unsafe_allow_html=True)

    # ---------------------------------------------------------
    st.header("5. matplotlib vs seaborn — what's the difference?")
    st.markdown("""
    | | matplotlib 🔧 | seaborn 🎨 |
    |---|---|---|
    | Think of it as | The raw toolbox | A stylish shortcut built *on top of* matplotlib |
    | Control | Total control over every pixel | Less control, far less typing |
    | Looks | Plain by default | Beautiful by default |
    | Best for | Custom, exact charts | Quick statistical charts (heatmaps, distributions) |
    """)
    st.markdown('<div class="dashedbox">🚗 <b>Analogy:</b> matplotlib is driving a manual car — '
                'full control, more effort. seaborn is an automatic car — faster and smoother '
                'for normal journeys. Most people use <b>both</b>, depending on the trip.</div>',
                unsafe_allow_html=True)

    # ---------------------------------------------------------
    st.header("6. Chart mistakes that mislead people")
    st.markdown("""
    - 🥧 **Pie chart with 12 slices** → nobody can compare them. Use a bar chart instead.
    - 📏 **Y-axis not starting at zero** → makes a tiny 2% rise look like a huge jump (very common in news & ads).
    - 🌈 **Too many colours** → colour should mean something, not just decorate.
    - 🏷️ **No labels or units** → "Sales: 45" — 45 what? Rupees? Units? Thousands?
    """)

    # ---------------------------------------------------------
    st.header("📒 Glossary")
    st.markdown("""
    | Word | Plain English |
    |---|---|
    | **Missing value (NaN)** | An empty cell |
    | **Duplicate** | The same record appearing more than once |
    | **Outlier** | A value far outside the normal range (often a typo) |
    | **Data type** | Whether a column is text, number, or date |
    | **EDA** | *Exploratory Data Analysis* — looking around your data with charts before modelling |
    | **Histogram** | A chart showing how often each value range occurs |
    """)

    st.header("🔁 5-line recap")
    st.markdown("""
    1. Real data is always messy — cleaning comes before any AI  
    2. The 5 usual problems: duplicates, missing values, wrong types, inconsistent text, outliers  
    3. Fill missing numbers with the **median** (it resists outliers)  
    4. Pick your chart by your *goal*: compare→bar, trend→line, shape→histogram, relationship→scatter  
    5. matplotlib = full control; seaborn = beautiful shortcuts
    """)

    # ---------------------------------------------------------
    st.header("✅ Practice Session")
    questions = [
        ("Your dataset has 'Mumbai', 'mumbai', and ' Mumbai '. Why is this a serious problem?",
         "The computer treats all three as **different cities**, so your counts and groupings will be wrong. "
         "Fix it by trimming spaces and standardising capitalisation."),
        ("A column of 1,000 ages has 3 missing values. Should you delete those rows or fill them?",
         "Either is acceptable here, but deleting 3 out of 1,000 (0.3%) is perfectly safe and simplest. "
         "If 300 were missing, you would need to fill them instead."),
        ("Why fill missing salaries with the median instead of the mean?",
         "Because the mean gets dragged upward by a few very high salaries (Day 8-10!). "
         "The median gives a more typical, realistic value."),
        ("You want to show monthly website visitors for the last 2 years. Which chart?",
         "A **line chart** — it's time-based data, and lines show trend and direction best."),
        ("You want to check if study hours and exam marks are related. Which chart?",
         "A **scatter plot** — each dot is one student, and the overall pattern shows if they move together."),
        ("A news channel shows a bar chart where the Y-axis starts at 95 instead of 0, making a "
         "2% change look enormous. What is wrong?",
         "A **truncated Y-axis** — it exaggerates small differences and misleads the viewer. "
         "Bar charts should almost always start at zero."),
        ("True/False: Data cleaning is a small step you do quickly before the 'real' AI work.",
         "**False.** In real jobs, cleaning and preparing data is typically 60–80% of the total time."),
    ]
    for i, (q, a) in enumerate(questions, 1):
        with st.expander(f"Q{i}. {q}"):
            st.success(f"✅ {a}")

    st.subheader("✍️ Mini-task")
    st.markdown('<div class="dashedbox">Download any free CSV from Kaggle (try "Titanic" or "Netflix Movies"). '
                'In Google Colab, run just these three lines and write down what you notice:<br>'
                '<code>df.head()</code> · <code>df.info()</code> · <code>df.isnull().sum()</code><br>'
                'Which columns have missing values? Which columns have the wrong data type?</div>',
                unsafe_allow_html=True)

    with st.expander("📺 Watch this topic in Tamil"):
        st.markdown("""
        - [Bharathi Yuvan — Pandas data cleaning Tamil](https://www.youtube.com/results?search_query=Bharathi+Yuvan+pandas+data+cleaning+tamil)
        - [Karthikeyan's Tech Class — matplotlib seaborn Tamil](https://www.youtube.com/results?search_query=Karthikeyan+Tech+Class+matplotlib+seaborn+tamil)
        - [Data visualization in Tamil (beginner)](https://www.youtube.com/results?search_query=data+visualization+python+tamil+beginners)
        """)

    st.info("📌 **Next topic:** Intro to ML — Supervised vs Unsupervised, Regression & Classification")

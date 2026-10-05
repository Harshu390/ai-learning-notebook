import streamlit as st
import numpy as np
from diagrams import (mean_median_chart, bell_curve, spread_comparison,
                      correlation_scatter, coin_flip_convergence)


def render():
    st.title("📊 Day 8-10: Statistics & Probability Essentials")
    st.caption("Foundations · Topic 3 · the 'maths' behind AI — explained with salaries, buses and coins")

    st.markdown('<div class="notebox"><b>Goal:</b> Understand mean/median/mode, spread, the bell curve, '
                'probability and correlation — <b>without any formulas to memorise</b>. '
                'These 5 ideas appear in almost every ML model you will ever build.</div>',
                unsafe_allow_html=True)

    st.header("1. Why does AI need statistics at all?")
    st.write("Machine Learning is basically **finding patterns in numbers**. "
             "Statistics is the language we use to *describe* those numbers before the machine learns from them.")
    st.markdown('<div class="dashedbox">🩺 <b>Real-life analogy:</b> Before a doctor treats you, they first measure '
                'temperature, BP and pulse. Statistics is the AI engineer\'s way of taking the '
                '"vital signs" of a dataset before building anything.</div>', unsafe_allow_html=True)

    st.header("2. Mean, Median, Mode — the 3 'middle' numbers")
    st.markdown("""
    | Term | Plain meaning | How to find it |
    |---|---|---|
    | **Mean** | The average | Add everything up ÷ how many |
    | **Median** | The middle value | Line everyone up, pick the person in the centre |
    | **Mode** | The most common value | Whichever value repeats most often |
    """)

    st.subheader("🎛️ Try it: why the 'average salary' lies")
    st.write("A small company has 5 normal employees. Now drag the slider to set the **boss's salary** "
             "and watch what happens to the mean vs the median.")

    boss = st.slider("Boss's salary (₹ thousands/month)", 40, 2000, 60, step=20)
    salaries = [30, 34, 38, 42, 46, boss]
    labels = ["Asha", "Ravi", "Meera", "Karthik", "Divya", "BOSS"]
    st.pyplot(mean_median_chart(salaries, labels))

    mean_v, median_v = np.mean(salaries), np.median(salaries)
    c1, c2 = st.columns(2)
    c1.metric("Mean (average)", f"₹{mean_v:,.0f}k")
    c2.metric("Median (middle person)", f"₹{median_v:,.0f}k")

    if boss > 300:
        st.warning(f"⚠️ The mean says the 'average' employee earns ₹{mean_v:,.0f}k — but **5 out of 6 people "
                   f"earn far less than that!** The median (₹{median_v:,.0f}k) describes reality much better.")
    else:
        st.info("👆 Now push the boss's salary up to ₹2000k and watch the red Mean line fly away from reality.")

    st.markdown('<div class="notebox">🧠 <b>Rule of thumb:</b> When your data has a few extreme values '
                '(salaries, house prices, website visits) → trust the <b>median</b>. '
                'When data is evenly spread (exam marks, heights) → the <b>mean</b> is fine.</div>',
                unsafe_allow_html=True)

    st.header("3. Spread — two things can have the same average and still be totally different")
    st.write("**Spread** (also called *standard deviation*) tells you how much the numbers **jump around** the average.")

    st.markdown('<div class="dashedbox">🚌 <b>Real-life example:</b> Two bus routes to your office. '
                'Both take <b>30 minutes on average</b>.<br>'
                '• <b>Bus A</b> is always 28–32 min → small spread → you can plan your life around it.<br>'
                '• <b>Bus B</b> is sometimes 12 min, sometimes 55 min → huge spread → you will miss meetings.<br>'
                'Same average. Completely different experience!</div>', unsafe_allow_html=True)

    st.pyplot(spread_comparison())

    st.markdown("""
    - **Small spread** = consistent, predictable, trustworthy
    - **Large spread** = unpredictable, risky, hard to make promises about
    """)
    st.markdown('<div class="notebox">📌 In ML, a model with high spread in its errors is '
                '<b>unreliable</b> even if its average error looks good — exactly like Bus B.</div>',
                unsafe_allow_html=True)

    st.header("4. The Bell Curve (Normal Distribution)")
    st.write("When you measure lots of natural things — human height, exam marks, shoe sizes — "
             "you almost always get this **bell shape**: most people near the middle, very few at the extremes.")

    avg = st.slider("Class average mark", 40, 90, 70)
    sd = st.slider("How spread out the class is", 2, 25, 10)
    st.pyplot(bell_curve(avg, sd, title=f"Exam marks: average {avg}, spread {sd}"))

    st.markdown(f"""
    Reading this chart in plain English:
    - The tall middle = **most students scored around {avg}**
    - The yellow area = roughly **68 out of every 100 students** scored between **{avg-sd} and {avg+sd}**
    - The thin tails = a *few* students scored very low or very high
    """)
    st.markdown('<div class="dashedbox">👟 <b>Real-life example:</b> A shoe shop stocks mostly size 8–9 '
                '(the fat middle of the bell) and only one or two pairs of size 5 or size 13 '
                '(the thin tails). That stocking decision IS a bell curve in action.</div>',
                unsafe_allow_html=True)

    st.header("5. Probability — the language of 'how likely?'")
    st.write("**Probability = the chance something happens**, written from 0 (never) to 1 (always), "
             "or as 0% to 100%.")

    st.markdown("""
    | Everyday sentence | Probability |
    |---|---|
    | "The sun will rise tomorrow" | 1.0 (100%) |
    | "A fair coin lands heads" | 0.5 (50%) |
    | "I roll a 6 on a dice" | 1/6 ≈ 0.17 (17%) |
    | "A pig will fly past my window" | 0.0 (0%) |
    """)

    st.subheader("🎛️ Try it: the Law of Large Numbers")
    st.write("We know a coin *should* land heads 50% of the time. But with only a few flips, "
             "you can easily get 70% heads by luck. Drag the slider to flip more coins:")

    flips = st.slider("Number of coin flips", 10, 2000, 50, step=10)
    st.pyplot(coin_flip_convergence(flips))
    st.markdown('<div class="notebox">🎯 <b>Why this matters for AI:</b> This is exactly why you cannot judge '
                'a model on 10 test examples. More data → results settle down to the truth. '
                'Small data → random luck fools you.</div>', unsafe_allow_html=True)

    st.markdown('<div class="dashedbox">🌧️ <b>Real-life example:</b> When your weather app says '
                '"70% chance of rain", it means: <i>out of 100 past days that looked exactly like today, '
                'it rained on 70 of them.</i> That is literally how ML prediction works.</div>',
                unsafe_allow_html=True)

    st.header("6. Correlation ≠ Causation (the most famous trap)")
    st.write("**Correlation** = two things move together. **Causation** = one thing actually *causes* the other. "
             "They are NOT the same, and confusing them is the #1 beginner mistake.")

    strength = st.select_slider("Move the slider to change how strongly the two move together:",
                                options=[0.1, 0.3, 0.5, 0.7, 0.9], value=0.9)
    st.pyplot(correlation_scatter(strength))

    st.markdown('<div class="dashedbox">🍦 <b>The classic example:</b> Ice cream sales and swimming accidents '
                'rise and fall together almost perfectly. Does ice cream cause drowning? <b>No!</b> '
                'A hidden third factor — <b>hot summer weather</b> — causes both. '
                'That hidden factor is called a <i>confounding variable</i>.</div>', unsafe_allow_html=True)

    st.markdown("""
    More real traps you will see in the news:
    - 🏘️ *"Houses near good schools cost more"* → the school doesn't cause the price; **rich areas** cause both.
    - 💪 *"People who take vitamins live longer"* → vitamins may not cause it; **people who can afford vitamins also eat better and see doctors**.
    """)

    st.header("📒 Glossary — the 8 words to remember")
    st.markdown("""
    | Word | Plain English |
    |---|---|
    | **Mean** | Average |
    | **Median** | Middle value |
    | **Mode** | Most repeated value |
    | **Outlier** | A weirdly extreme value (the boss's salary) |
    | **Spread / Std Dev** | How much numbers jump around the average |
    | **Distribution** | The overall shape of your data |
    | **Probability** | Chance of something happening (0 to 1) |
    | **Correlation** | Two things moving together (NOT proof of cause) |
    """)

    st.header("🔁 5-line recap")
    st.markdown("""
    1. Mean = average, Median = middle, Mode = most common
    2. Outliers wreck the mean → use the median for salaries, prices, etc.
    3. Same average + different spread = completely different reality (Bus A vs Bus B)
    4. Natural data usually forms a bell curve: crowded middle, thin tails
    5. Correlation is a *hint*, never *proof* — look for the hidden third factor
    """)

    st.header("✅ Practice Session")
    questions = [
        ("Scores are 60, 70, 80, 90, 100. What is the mean?",
         "80 — because 60+70+80+90+100 = 400, and 400 ÷ 5 = 80."),
        ("In a village, 9 people earn ₹20k and 1 person earns ₹5,00,000. "
         "Which better describes a typical villager — mean or median?",
         "The **median** (₹20k). The mean would be about ₹68k, which describes nobody in that village."),
        ("Two delivery boys both average 25 minutes. Boy A ranges 24–26 min, Boy B ranges 5–60 min. "
         "Who would you hire for a hospital delivery, and what statistical word explains it?",
         "Boy A — because of **lower spread (standard deviation)**. Reliability matters more than the average."),
        ("Your app says '30% chance of rain'. Does that mean it will not rain?",
         "No! It means that in 3 out of 10 similar past situations it rained. A 30% event still happens quite often."),
        ("Shops that sell more umbrellas also report more flu cases. Does buying umbrellas cause flu?",
         "No — this is **correlation, not causation**. The hidden factor is the **rainy/cold season**, which drives both."),
        ("You flip a coin 8 times and get 6 heads. Is the coin unfair?",
         "Probably not — with so few flips, luck dominates. Flip it 1,000 times and it will settle near 50% "
         "(the Law of Large Numbers)."),
    ]
    for i, (q, a) in enumerate(questions, 1):
        with st.expander(f"Q{i}. {q}"):
            st.success(f"✅ {a}")

    st.subheader("✍️ Mini-task (do this before moving on)")
    st.markdown('<div class="dashedbox">Open your phone\'s screen-time report for the last 7 days. '
                'Write down the 7 daily numbers, then calculate the <b>mean</b> and the <b>median</b> by hand. '
                'Was there one unusual day (an outlier) that pulled the mean away from the median?</div>',
                unsafe_allow_html=True)

    with st.expander("📺 Watch this topic in Tamil"):
        st.markdown("""
        - [Bharathi Yuvan — Statistics for Data Science (Tamil)](https://www.youtube.com/results?search_query=Bharathi+Yuvan+statistics+data+science+tamil)
        - [Karthikeyan's Tech Class — Statistics Tamil](https://www.youtube.com/results?search_query=Karthikeyan+Tech+Class+statistics+python+tamil)
        - [Learn AI 6 Semester — Probability basics Tamil](https://www.youtube.com/results?search_query=learn+ai+tamil+probability+statistics+beginners)
        """)
        st.caption("These open a YouTube search so the links never break when channels re-upload.")

    st.info("📌 **Next topic:** Data Handling — Cleaning & Visualization")

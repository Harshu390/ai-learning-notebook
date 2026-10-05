import streamlit as st
from diagrams import nested_circles_ai_ml_dl, pipeline_flow

def render():
    st.title("🤖 Day 1-3: What is AI, ML & Deep Learning?")
    st.caption("Foundations · Topic 1 · for absolute beginners")

    st.markdown('<div class="notebox"><b>Goal:</b> By the end, you can explain AI, ML, and Deep Learning to a friend using simple, real-life examples.</div>', unsafe_allow_html=True)

    st.header("1. What is Artificial Intelligence (AI)?")
    st.write("**AI = making machines do things that normally need human intelligence** — like seeing, listening, understanding, or deciding.")

    st.markdown('<div class="dashedbox">🎬 <b>Real-life example:</b> When Netflix suggests a movie you\'ll probably like, or Google Maps picks the fastest route — that\'s AI working quietly in the background.</div>', unsafe_allow_html=True)

    st.subheader("Everyday AI you already use")
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("- 📍 Google Maps route prediction\n- 🎥 Netflix/YouTube recommendations\n- 🔓 Phone face unlock")
    with col2:
        st.markdown("- 📧 Email spam filter\n- 🗣️ Siri / Google Assistant\n- 💬 ChatGPT / Claude")

    st.header("2. AI vs ML vs Deep Learning")
    st.write("Picture three nested circles — like Russian nesting dolls:")
    st.pyplot(nested_circles_ai_ml_dl())

    st.markdown("""
    | Term | Simple Meaning | Real Example |
    |---|---|---|
    | **AI** | Machine acts smart (rules OR learning) | A chess program with fixed rules |
    | **ML** | Machine **learns from data** | Spam filter learning from emails |
    | **Deep Learning** | ML using many-layer "neural networks" | Face recognition, ChatGPT |
    """)

    st.markdown('<div class="notebox">🧠 <b>Remember:</b> Every ML is AI, but not every AI is ML!</div>', unsafe_allow_html=True)

    st.header("3. Normal Programming vs Machine Learning")
    st.write("This is the **most important idea** in this whole topic.")

    c1, c2 = st.columns(2)
    with c1:
        st.markdown("**🖥️ Normal Programming**")
        st.graphviz_chart(pipeline_flow(["Data", "Rules (you write)", "Answers"],
                                         colors=["#bae6fd", "#bae6fd", "#bbf7d0"]))
    with c2:
        st.markdown("**🤖 Machine Learning**")
        st.graphviz_chart(pipeline_flow(["Data + Answers", "Computer learns", "Rules! (discovered)"],
                                         colors=["#fecaca", "#fecaca", "#bbf7d0"]))

    st.markdown("""
    **Example — spotting spam email:**
    - ❌ **Normal way:** A human writes a rule — *"if email contains 'lottery' → spam."* Spammers just change the word.
    - ✅ **ML way:** Show the computer 10,000 emails already marked spam/not-spam. It finds the *pattern* itself — and adapts as spam changes!
    """)

    st.header("4. Three Ways a Machine Learns")
    tab1, tab2, tab3 = st.tabs(["👩‍🏫 Supervised", "🔍 Unsupervised", "🎮 Reinforcement"])
    with tab1:
        st.write("**Learn with a teacher** — you show labeled examples (photo + correct answer).")
        st.markdown("🧑‍🏫 *Like a teacher showing flashcards: 'This is a cat 🐱', 'This is a dog 🐶'*")
    with tab2:
        st.write("**No labels given** — the machine finds hidden groups on its own.")
        st.markdown("🧺 *Like sorting a mixed fruit basket by color/shape without anyone telling you the names.*")
    with tab3:
        st.write("**Trial and reward** — good moves earn a point, bad moves lose a point.")
        st.markdown("🎮 *Like training a dog with treats — good behavior gets rewarded.*")

    st.header("5. Career Landscape (quick peek)")
    st.markdown("""
    - 🔹 **Data Scientist** – finds patterns in data
    - 🔹 **ML Engineer** – builds & deploys learning models
    - 🔹 **AI/Prompt Engineer** – works with LLMs like ChatGPT
    - 🔹 **MLOps Engineer** – keeps AI systems running in production
    """)

    st.header("✅ Practice Questions")
    questions = [
        ("Is Deep Learning a subset of ML, or is ML a subset of DL?",
         "DL is a subset of ML. (ML is the bigger box, DL is the smaller one inside it)"),
        ("Netflix recommending a show based on your watch history — is this ML or DL specifically?",
         "ML — it learns patterns from your viewing data."),
        ("True or False: 'All AI is Deep Learning'",
         "False! AI is the biggest umbrella category; DL is just one small, advanced part of it."),
        ("In Normal Programming we give Data + Rules to get Answers. In ML, what do we give instead?",
         "We give Data + Answers (examples), and the machine figures out the Rules itself!"),
    ]
    for i, (q, a) in enumerate(questions, 1):
        with st.expander(f"Q{i}: {q}"):
            st.success(f"✅ {a}")

    st.info("📌 **Next topic:** Python Basics for AI (numpy & pandas)")

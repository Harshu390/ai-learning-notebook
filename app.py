import streamlit as st
import importlib

st.set_page_config(page_title="AI Learning Notebook 📓", page_icon="📓", layout="wide")

# ---------- NOTEBOOK STYLE CSS ----------
def load_css():
    st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Kalam:wght@400;700&family=Patrick+Hand&display=swap');
    html, body, [class*="css"] { font-family: 'Patrick Hand', cursive; font-size: 18px; }
    .stApp { background-color: #CFC6AE; }
    .block-container {
        background: #F7F1E1;
        padding: 2.5rem 3rem;
        border-radius: 10px;
        box-shadow: 0 3px 14px rgba(0,0,0,.25);
        max-width: 950px;
    }
    h1 { font-family:'Kalam',cursive; color:#C9553D; transform: rotate(-0.6deg); }
    h2 { font-family:'Kalam',cursive; color:#3C6E8F; text-decoration: underline wavy #F2D062; text-underline-offset:6px; }
    h3 { font-family:'Kalam',cursive; color:#4C7A52; }
    .notebox {
        border:2px solid #2B2A28; border-radius:10px; padding:10px 16px;
        margin:12px 0; background:#FFF6C9; transform: rotate(-0.4deg);
    }
    .dashedbox {
        border:2px dashed #6A685F; border-radius:10px; padding:10px 16px;
        margin:12px 0; background:rgba(255,255,255,.45);
    }
    [data-testid="stSidebar"] { background-color:#E8DFC4; }
    </style>
    """, unsafe_allow_html=True)

load_css()

# ---------- CURRICULUM MAP ----------
CURRICULUM = {
    "📘 Phase 1: Foundations (Days 1-21)": [
        ("day1_3", "Day 1-3 · What is AI/ML/DL?"),
        ("day4_7", "Day 4-7 · Python Basics (numpy, pandas)"),
        ("day8_10", "Day 8-10 · Statistics & Probability"),
        ("day11_14", "Day 11-14 · Data Cleaning & Visualization"),
        ("day15_18", "Day 15-18 · Supervised vs Unsupervised"),
        ("day19_21", "Day 19-21 · Practice Project"),
    ],
    "📗 Phase 2: Core ML (Days 22-49)": [
        ("day22_26", "Day 22-26 · Regression & Classification"),
        ("day27_31", "Day 27-31 · Ensemble Methods"),
        ("day32_35", "Day 32-35 · Model Evaluation"),
        ("day36_40", "Day 36-40 · Unsupervised Learning (Clustering, PCA)"),
        ("day41_45", "Day 41-45 · Feature Engineering + Kaggle Project"),
        ("day46_49", "Day 46-49 · scikit-learn + Deployment Basics"),
    ],
    "📙 Phase 3: Deep Learning (Days 50-77)": [
        ("day50_56", "Day 50-56 · Neural Network Fundamentals"),
        ("day57_63", "Day 57-63 · CNNs & Vision Project"),
        ("day64_70", "Day 64-70 · RNNs/LSTMs → Transformers"),
        ("day71_77", "Day 71-77 · Transformer Architecture"),
    ],
    "📕 Phase 4: LLMs, Prompting & RAG (Days 78-110)": [
        ("day78_82", "Day 78-82 · What are LLMs?"),
        ("day83_86", "Day 83-86 · Prompt Engineering"),
        ("day87_91", "Day 87-91 · Embeddings & Vector Databases"),
        ("day92_96", "Day 92-96 · RAG Architecture"),
        ("day97_100", "Day 97-100 · Build a RAG Project"),
        ("day101_105", "Day 101-105 · Fine-tuning Basics"),
        ("day106_110", "Day 106-110 · AI Agents"),
    ],
}

# ---------- SESSION STATE ----------
if "completed" not in st.session_state:
    st.session_state.completed = set()
if "selected" not in st.session_state:
    st.session_state.selected = "day1_3"

# ---------- SIDEBAR ----------
st.sidebar.title("📓 AI Learning Notebook")
st.sidebar.caption("From Zero to RAG-Ready")

total_topics = sum(len(v) for v in CURRICULUM.values())
pct = int(len(st.session_state.completed) / total_topics * 100)
st.sidebar.progress(pct / 100)
st.sidebar.write(f"**{pct}% complete** ({len(st.session_state.completed)}/{total_topics} topics)")
st.sidebar.markdown("---")

for phase, topics in CURRICULUM.items():
    with st.sidebar.expander(phase, expanded=(phase == "📘 Phase 1: Foundations (Days 1-21)")):
        for key, label in topics:
            icon = "✅" if key in st.session_state.completed else "⬜"
            if st.button(f"{icon} {label}", key=f"nav_{key}", use_container_width=True):
                st.session_state.selected = key
                st.rerun()

# ---------- MAIN CONTENT ----------
selected_key = st.session_state.selected

try:
    module = importlib.import_module(f"content.{selected_key}")
    module.render()
except ModuleNotFoundError:
    st.title("🚧 Coming Soon")
    st.write("This topic note is being written — check back soon!")

st.markdown("---")
col1, col2 = st.columns([1, 3])
with col1:
    if st.button("✅ Mark as Complete", type="primary"):
        st.session_state.completed.add(selected_key)
        st.balloons()
        st.rerun()

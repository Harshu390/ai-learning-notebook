import matplotlib.pyplot as plt
import matplotlib.patches as patches
import graphviz

def nested_circles_ai_ml_dl():
    """AI > ML > DL as nested circles — like Russian dolls"""
    fig, ax = plt.subplots(figsize=(6, 4.5))
    ax.set_xlim(0, 10); ax.set_ylim(0, 8); ax.axis('off')

    ax.add_patch(patches.Circle((5, 3.8), 3.4, color="#bae6fd", ec="black", lw=2))
    ax.add_patch(patches.Circle((5, 3.3), 2.3, color="#bbf7d0", ec="black", lw=2))
    ax.add_patch(patches.Circle((5, 2.8), 1.2, color="#fecaca", ec="black", lw=2))

    ax.text(5, 7.1, "Artificial Intelligence (AI)", ha='center', fontsize=13, fontweight='bold')
    ax.text(5, 5.3, "Machine Learning (ML)", ha='center', fontsize=12, fontweight='bold')
    ax.text(5, 2.8, "Deep\nLearning", ha='center', fontsize=10, fontweight='bold')
    return fig

def pipeline_flow(steps, colors=None):
    """Horizontal flowchart — Data -> Process -> Output"""
    dot = graphviz.Digraph()
    dot.attr(rankdir='LR', bgcolor='transparent')
    dot.attr('node', shape='box', style='rounded,filled', fontname='Helvetica', fontsize='13')
    if colors is None:
        colors = ["#bae6fd"] * len(steps)
    for i, step in enumerate(steps):
        dot.node(str(i), step, fillcolor=colors[i])
    for i in range(len(steps) - 1):
        dot.edge(str(i), str(i + 1))
    return dot

def bar_chart_example(labels, values, title, ylabel, color="#60a5fa"):
    """Simple relatable bar chart"""
    fig, ax = plt.subplots(figsize=(4.5, 3.2))
    ax.bar(labels, values, color=color, edgecolor='black')
    ax.set_title(title, fontsize=11)
    ax.set_ylabel(ylabel, fontsize=10)
    plt.xticks(rotation=20, fontsize=9)
    return fig

def scatter_clusters_example():
    """Unsupervised learning visual - fruit grouping by features"""
    fig, ax = plt.subplots(figsize=(5, 4))
    import numpy as np
    rng = np.random.default_rng(42)
    group1 = rng.normal(loc=(2, 2), scale=0.4, size=(15, 2))
    group2 = rng.normal(loc=(6, 6), scale=0.4, size=(15, 2))
    group3 = rng.normal(loc=(2, 6), scale=0.4, size=(15, 2))
    ax.scatter(*group1.T, color="#f87171", s=70, label="Group A 🍎", edgecolor='black')
    ax.scatter(*group2.T, color="#4ade80", s=70, label="Group B 🍏", edgecolor='black')
    ax.scatter(*group3.T, color="#60a5fa", s=70, label="Group C 🍊", edgecolor='black')
    ax.set_title("Unsupervised Learning: machine finds these groups ITSELF")
    ax.legend()
    ax.axis('off')
    return fig

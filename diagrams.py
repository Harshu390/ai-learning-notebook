# =========================================================
# diagrams.py — COMPLETE FILE — Covers Day 1 to Day 31
# Compatible with Option A (Claude Opus) + Spark version
# =========================================================
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np
import graphviz


# =========================================================
# BATCH 1 — Days 1-3, 4-7 — Foundations
# =========================================================

def nested_circles_ai_ml_dl():
    """AI > ML > DL as nested circles — like Russian dolls"""
    fig, ax = plt.subplots(figsize=(6, 4.5))
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 8)
    ax.axis('off')

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
    plt.tight_layout()
    return fig


def scatter_clusters_example():
    """Unsupervised learning visual - fruit grouping by features"""
    fig, ax = plt.subplots(figsize=(5, 4))
    rng = np.random.default_rng(42)
    group1 = rng.normal(loc=(2, 2), scale=0.4, size=(15, 2))
    group2 = rng.normal(loc=(6, 6), scale=0.4, size=(15, 2))
    group3 = rng.normal(loc=(2, 6), scale=0.4, size=(15, 2))
    ax.scatter(*group1.T, color="#f87171", s=70, label="Group A", edgecolor='black')
    ax.scatter(*group2.T, color="#4ade80", s=70, label="Group B", edgecolor='black')
    ax.scatter(*group3.T, color="#60a5fa", s=70, label="Group C", edgecolor='black')
    ax.set_title("Unsupervised: machine finds groups ITSELF")
    ax.legend()
    ax.axis('off')
    return fig


# =========================================================
# BATCH 2 DIAGRAMS — Days 8-10, 11-14, 15-18 (Option A)
# =========================================================

def mean_median_chart(values, labels=None, ylabel="Salary (₹ thousands)"):
    """Bar chart with mean & median lines — shows how outliers drag the mean."""
    fig, ax = plt.subplots(figsize=(6.5, 3.4))
    if labels is None:
        labels = [f"P{i+1}" for i in range(len(values))]
    bars = ax.bar(labels, values, color="#93c5fd", edgecolor="black", lw=1.2)
    bars[-1].set_color("#fca5a5")  # highlight the last one (the outlier)

    mean_v = float(np.mean(values))
    median_v = float(np.median(values))
    ax.axhline(mean_v, color="#dc2626", ls="--", lw=2.2, label=f"Mean = {mean_v:,.0f}")
    ax.axhline(median_v, color="#16a34a", ls="-.", lw=2.2, label=f"Median = {median_v:,.0f}")
    ax.set_ylabel(ylabel, fontsize=10)
    ax.legend(fontsize=9, loc="upper left")
    for s in ['top', 'right']:
        ax.spines[s].set_visible(False)
    plt.tight_layout()
    return fig


def bell_curve(mean=70, std=10, title="Bell Curve (Normal Distribution)"):
    """Classic bell curve with 1-sigma shading."""
    x = np.linspace(mean - 4 * std, mean + 4 * std, 400)
    y = np.exp(-0.5 * ((x - mean) / std) ** 2)
    fig, ax = plt.subplots(figsize=(6.5, 3.2))
    ax.plot(x, y, color="#1f2937", lw=2.5)
    mask = (x >= mean - std) & (x <= mean + std)
    ax.fill_between(x[mask], y[mask], color="#fde68a", alpha=0.8,
                    label="~68% of people land here")
    ax.axvline(mean, color="#dc2626", ls="--", lw=2, label=f"Average = {mean}")
    ax.set_title(title, fontsize=11)
    ax.set_yticks([])
    ax.legend(fontsize=9)
    for s in ['top', 'right', 'left']:
        ax.spines[s].set_visible(False)
    plt.tight_layout()
    return fig


def spread_comparison(mean=30, std_a=3, std_b=12):
    """Two routes, same average time, different reliability."""
    x = np.linspace(0, 70, 400)
    ya = np.exp(-0.5 * ((x - mean) / std_a) ** 2)
    yb = np.exp(-0.5 * ((x - mean) / std_b) ** 2)
    fig, ax = plt.subplots(figsize=(6.5, 3.2))
    ax.plot(x, ya, color="#16a34a", lw=2.5, label=f"Bus A — reliable (spread {std_a})")
    ax.plot(x, yb, color="#dc2626", lw=2.5, label=f"Bus B — risky (spread {std_b})")
    ax.axvline(mean, color="#1f2937", ls="--", lw=1.5)
    ax.text(mean + 1, max(ya) * 0.95, f"Both average {mean} min", fontsize=9)
    ax.set_xlabel("Travel time (minutes)", fontsize=10)
    ax.set_yticks([])
    ax.legend(fontsize=9)
    for s in ['top', 'right', 'left']:
        ax.spines[s].set_visible(False)
    plt.tight_layout()
    return fig


def correlation_scatter(strength=0.9, n=40, seed=7):
    """Scatter showing a chosen correlation strength."""
    rng = np.random.default_rng(seed)
    x = rng.uniform(0, 10, n)
    noise = rng.normal(0, 3, n)
    y = strength * x * 1.0 + (1 - abs(strength)) * noise + 5
    fig, ax = plt.subplots(figsize=(5.2, 3.4))
    ax.scatter(x, y, color="#60a5fa", s=60, edgecolor="black", zorder=3)
    ax.set_xlabel("Ice cream sales", fontsize=10)
    ax.set_ylabel("Swimming accidents", fontsize=10)
    ax.set_title(f"Correlation strength = {strength:.1f}", fontsize=11)
    for s in ['top', 'right']:
        ax.spines[s].set_visible(False)
    plt.tight_layout()
    return fig


def coin_flip_convergence(n_flips=500, seed=1):
    """Law of large numbers — proportion settles near 0.5."""
    rng = np.random.default_rng(seed)
    flips = rng.integers(0, 2, n_flips)
    running = np.cumsum(flips) / np.arange(1, n_flips + 1)
    fig, ax = plt.subplots(figsize=(6.5, 3.2))
    ax.plot(range(1, n_flips + 1), running, color="#3C6E8F", lw=2)
    ax.axhline(0.5, color="#dc2626", ls="--", lw=2, label="True probability = 0.5")
    ax.set_xlabel("Number of coin flips", fontsize=10)
    ax.set_ylabel("Share of heads", fontsize=10)
    ax.set_ylim(0, 1)
    ax.legend(fontsize=9)
    for s in ['top', 'right']:
        ax.spines[s].set_visible(False)
    plt.tight_layout()
    return fig


def regression_demo(slope=50, intercept=100, show_errors=True, seed=3):
    """House size vs price — fit a line, show the gaps (errors)."""
    rng = np.random.default_rng(seed)
    size = np.array([600, 850, 1000, 1200, 1400, 1650, 1800, 2100])
    true_price = 0.055 * size + 95 + rng.normal(0, 12, len(size))
    pred = (slope / 1000) * size + intercept

    fig, ax = plt.subplots(figsize=(6.5, 3.8))
    ax.scatter(size, true_price, color="#f59e0b", s=80, edgecolor="black",
               zorder=3, label="Real houses sold")
    ax.plot(size, pred, color="#3C6E8F", lw=2.5, label="Your prediction line")
    if show_errors:
        for s, t, p in zip(size, true_price, pred):
            ax.plot([s, s], [t, p], color="#dc2626", ls=":", lw=1.6)
    ax.set_xlabel("House size (sq ft)", fontsize=10)
    ax.set_ylabel("Price (₹ lakhs)", fontsize=10)
    ax.legend(fontsize=9)
    for s in ['top', 'right']:
        ax.spines[s].set_visible(False)
    plt.tight_layout()
    total_error = float(np.mean(np.abs(true_price - pred)))
    return fig, total_error


def classification_demo(threshold=5.0, seed=11):
    """Spam vs not-spam separated by a movable line."""
    rng = np.random.default_rng(seed)
    ham = rng.normal(loc=(3, 3), scale=1.1, size=(22, 2))
    spam = rng.normal(loc=(7.5, 7.0), scale=1.2, size=(22, 2))

    fig, ax = plt.subplots(figsize=(5.6, 4))
    ax.scatter(*ham.T, color="#4ade80", s=70, edgecolor="black",
               label="Normal email", zorder=3)
    ax.scatter(*spam.T, color="#f87171", s=70, edgecolor="black",
               label="Spam", zorder=3)
    xs = np.linspace(0, 11, 10)
    ax.plot(xs, 2 * threshold - xs, color="#1f2937", lw=2.5, ls="--",
            label="Decision line")
    ax.set_xlim(0, 11)
    ax.set_ylim(0, 11)
    ax.set_xlabel("Number of suspicious words", fontsize=10)
    ax.set_ylabel("Number of links", fontsize=10)
    ax.legend(fontsize=9, loc="upper left")
    for s in ['top', 'right']:
        ax.spines[s].set_visible(False)
    plt.tight_layout()

    all_pts = np.vstack([ham, spam])
    truth = np.array([0] * len(ham) + [1] * len(spam))
    pred = (all_pts[:, 0] + all_pts[:, 1] > 2 * threshold).astype(int)
    acc = float((pred == truth).mean())
    return fig, acc


def train_test_diagram():
    """Graphviz: splitting data into train & test."""
    dot = graphviz.Digraph()
    dot.attr(rankdir="LR", bgcolor="transparent")
    dot.attr("node", shape="box", style="rounded,filled",
             fontname="Helvetica", fontsize="12")
    dot.node("A", "All your data\n(1000 houses)", fillcolor="#fde68a")
    dot.node("B", "Training set\n80% = 800 houses\n(model studies these)", fillcolor="#bbf7d0")
    dot.node("C", "Test set\n20% = 200 houses\n(hidden exam!)", fillcolor="#fecaca")
    dot.node("D", "Trained Model", fillcolor="#bae6fd")
    dot.node("E", "Score / Accuracy", fillcolor="#ddd6fe")
    dot.edge("A", "B")
    dot.edge("A", "C")
    dot.edge("B", "D", label="learn")
    dot.edge("C", "E", label="check")
    dot.edge("D", "E")
    return dot


def cleaning_pipeline():
    dot = graphviz.Digraph()
    dot.attr(rankdir="LR", bgcolor="transparent")
    dot.attr("node", shape="box", style="rounded,filled",
             fontname="Helvetica", fontsize="11")
    steps = [("1", "Raw messy data", "#fecaca"),
             ("2", "Remove\nduplicates", "#fed7aa"),
             ("3", "Fix missing\nvalues", "#fde68a"),
             ("4", "Fix formats\n& typos", "#d9f99d"),
             ("5", "Handle\noutliers", "#bbf7d0"),
             ("6", "Clean data\nready", "#bae6fd")]
    for k, lbl, c in steps:
        dot.node(k, lbl, fillcolor=c)
    for i in range(1, len(steps)):
        dot.edge(str(i), str(i + 1))
    return dot


# =========================================================
# COMPATIBILITY — Older Spark names (so old files don't break)
# =========================================================

def mean_median_mode_diagram():
    numbers = [50, 60, 60, 70, 90]
    fig, ax = plt.subplots(figsize=(6, 2.2))
    ax.set_xlim(40, 100)
    ax.set_ylim(0, 2)
    ax.axis("off")
    ax.hlines(1, 45, 95, color="black", linewidth=2)
    for n in numbers:
        ax.plot(n, 1, "o", markersize=14, color="#F2D062", markeredgecolor="black")
        ax.text(n, 1.25, str(n), ha="center", fontsize=11)
    mean = sum(numbers) / len(numbers)
    median = numbers[len(numbers)//2]
    mode = 60
    ax.annotate("Mean = average\n66", xy=(mean, 1), xytext=(66, 0.15),
                arrowprops=dict(arrowstyle="->", lw=1.5), ha="center", fontsize=10)
    ax.annotate("Median = middle\n60", xy=(median, 1), xytext=(53, 0.15),
                arrowprops=dict(arrowstyle="->", lw=1.5), ha="center", fontsize=10)
    ax.annotate("Mode = repeated most\n60", xy=(mode, 1), xytext=(82, 1.55),
                arrowprops=dict(arrowstyle="->", lw=1.5), ha="center", fontsize=10)
    ax.set_title("Marks: 50, 60, 60, 70, 90", fontsize=12)
    return fig


def probability_bag_diagram(red=3, blue=2):
    fig, ax = plt.subplots(figsize=(5.2, 3.2))
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 6)
    ax.axis("off")
    bag = patches.FancyBboxPatch((1, 0.8), 5, 4, boxstyle="round,pad=0.25",
                                 facecolor="#FFF6C9", edgecolor="black", linewidth=2)
    ax.add_patch(bag)
    ax.text(3.5, 5.2, "Bag of balls", ha="center", fontsize=13, fontweight="bold")
    positions = [(2, 3.8), (3.2, 3.5), (4.5, 3.8), (2.7, 2.3), (4, 2.2)]
    colors = ["#f87171"] * red + ["#60a5fa"] * blue
    for (x, y), c in zip(positions, colors):
        ax.add_patch(patches.Circle((x, y), 0.42, facecolor=c, edgecolor="black", linewidth=1.5))
    total = red + blue
    ax.text(7.2, 3.8, f"Red balls = {red}", fontsize=12)
    ax.text(7.2, 3.1, f"Blue balls = {blue}", fontsize=12)
    ax.text(7.2, 2.2, f"P(red) = {red}/{total}", fontsize=13, fontweight="bold", color="#C9553D")
    return fig


def simple_bell_curve():
    x = np.linspace(-4, 4, 300)
    y = np.exp(-x**2 / 2)
    fig, ax = plt.subplots(figsize=(5.5, 3.2))
    ax.plot(x, y, color="#3C6E8F", linewidth=3)
    ax.fill_between(x, y, color="#bae6fd", alpha=0.6)
    ax.axvline(0, color="#C9553D", linestyle="--", linewidth=2)
    ax.text(0, 1.05, "average area", ha="center", color="#C9553D", fontsize=11)
    ax.text(-2.8, 0.25, "few low\nvalues", ha="center", fontsize=10)
    ax.text(2.8, 0.25, "few high\nvalues", ha="center", fontsize=10)
    ax.set_title("Bell Curve: many values near the average", fontsize=12)
    ax.axis("off")
    return fig


def messy_clean_table_diagram():
    fig, ax = plt.subplots(figsize=(6, 3))
    ax.axis("off")
    ax.text(0.05, 0.9, "Messy data", fontsize=13, fontweight="bold", color="#C9553D")
    ax.text(0.62, 0.9, "Clean data", fontsize=13, fontweight="bold", color="#4C7A52")
    messy = [
        ["Name", "Age", "City"],
        ["Ravi", "25 yrs", "chennai"],
        ["Meena", "", "CHENNAI"],
        ["Ravi", "25", "chennai"],
    ]
    clean = [
        ["Name", "Age", "City"],
        ["Ravi", "25", "Chennai"],
        ["Meena", "Unknown", "Chennai"],
    ]
    left_table = ax.table(cellText=messy, loc="left", bbox=[0.02, 0.15, 0.42, 0.65])
    right_table = ax.table(cellText=clean, loc="right", bbox=[0.58, 0.15, 0.38, 0.65])
    for table in [left_table, right_table]:
        table.auto_set_font_size(False)
        table.set_fontsize(9)
        for key, cell in table.get_celld().items():
            cell.set_edgecolor("black")
            if key[0] == 0:
                cell.set_facecolor("#F2D062")
    ax.annotate("", xy=(0.56, 0.48), xytext=(0.46, 0.48),
                arrowprops=dict(arrowstyle="->", lw=2))
    ax.text(0.50, 0.58, "clean", ha="center", fontsize=11)
    return fig


def regression_vs_classification_diagram():
    fig, ax = plt.subplots(figsize=(6, 3.5))
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 6)
    ax.axis("off")
    ax.add_patch(patches.FancyBboxPatch((0.5, 1), 4, 4, boxstyle="round,pad=0.25",
                                        facecolor="#bae6fd", edgecolor="black", linewidth=2))
    ax.text(2.5, 4.6, "Regression", ha="center", fontsize=14, fontweight="bold")
    ax.text(2.5, 3.7, "Predicts a NUMBER", ha="center", fontsize=11)
    ax.text(2.5, 2.7, "House price", ha="center", fontsize=12)
    ax.text(2.5, 2.0, "Rs.45,00,000", ha="center", fontsize=15, color="#C9553D", fontweight="bold")
    ax.add_patch(patches.FancyBboxPatch((5.5, 1), 4, 4, boxstyle="round,pad=0.25",
                                        facecolor="#bbf7d0", edgecolor="black", linewidth=2))
    ax.text(7.5, 4.6, "Classification", ha="center", fontsize=14, fontweight="bold")
    ax.text(7.5, 3.7, "Predicts a CATEGORY", ha="center", fontsize=11)
    ax.text(7.5, 2.7, "Email type", ha="center", fontsize=12)
    ax.text(7.5, 2.0, "Spam / Not Spam", ha="center", fontsize=14, color="#C9553D", fontweight="bold")
    return fig


# =========================================================
# BATCH 3 — Days 19-21, 22-26, 27-31 — Core ML start
# =========================================================

def decision_tree_diagram():
    """Simple visual of how a decision tree asks questions"""
    fig, ax = plt.subplots(figsize=(7, 4.5))
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 7)
    ax.axis("off")

    def box(x, y, w, h, text, color="#bae6fd"):
        ax.add_patch(patches.FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0.15",
                     facecolor=color, edgecolor="black", linewidth=2))
        ax.text(x + w/2, y + h/2, text, ha="center", va="center", fontsize=10)

    box(3.5, 5.5, 3, 1, "Is salary > 50k?", "#fde68a")
    box(0.5, 3.2, 2.5, 1, "Is age < 30?", "#bae6fd")
    box(6.5, 3.2, 2.5, 1, "Has savings?", "#bae6fd")
    box(0, 1, 2, 1, "Loan: NO", "#fecaca")
    box(2.5, 1, 2, 1, "Loan: YES", "#bbf7d0")
    box(6, 1, 2, 1, "Loan: YES", "#bbf7d0")
    box(8.2, 1, 1.8, 1, "Loan: NO", "#fecaca")

    ax.annotate("", xy=(1.7, 4.2), xytext=(4.5, 5.5), arrowprops=dict(arrowstyle="->"))
    ax.annotate("", xy=(7.7, 4.2), xytext=(5.5, 5.5), arrowprops=dict(arrowstyle="->"))
    ax.annotate("", xy=(1, 2), xytext=(1.5, 3.2), arrowprops=dict(arrowstyle="->"))
    ax.annotate("", xy=(3, 2), xytext=(2, 3.2), arrowprops=dict(arrowstyle="->"))
    ax.annotate("", xy=(6.5, 2), xytext=(7.2, 3.2), arrowprops=dict(arrowstyle="->"))
    ax.annotate("", xy=(8.8, 2), xytext=(8, 3.2), arrowprops=dict(arrowstyle="->"))
    ax.text(2.2, 5.9, "No", fontsize=9)
    ax.text(5.9, 5.9, "Yes", fontsize=9)
    plt.tight_layout()
    return fig


def linear_vs_logistic_diagram():
    """Straight line vs S-curve"""
    x = np.linspace(0, 10, 100)
    y_linear = 2*x + 3
    y_logistic = 1 / (1 + np.exp(-(x-5)))

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(9, 3.5))
    ax1.plot(x, y_linear, color="#3C6E8F", linewidth=3)
    ax1.set_title("Linear Regression\n(predicts a number)")
    ax1.set_xlabel("House size")
    ax1.set_ylabel("Price")

    ax2.plot(x, y_logistic, color="#C9553D", linewidth=3)
    ax2.set_title("Logistic Regression\n(predicts yes/no probability)")
    ax2.set_xlabel("Study hours")
    ax2.set_ylabel("Probability of passing")
    ax2.axhline(0.5, color="gray", linestyle="--")
    plt.tight_layout()
    return fig


def ensemble_forest_diagram():
    """Many trees voting together = random forest"""
    fig, ax = plt.subplots(figsize=(7, 3.5))
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 5)
    ax.axis("off")

    tree_positions = [1.5, 3.5, 5.5, 7.5]
    votes = ["YES", "YES", "NO", "YES"]
    colors = ["#bbf7d0" if v == "YES" else "#fecaca" for v in votes]

    for x, vote, color in zip(tree_positions, votes, colors):
        ax.add_patch(patches.Circle((x, 3), 0.8, facecolor=color, edgecolor="black", linewidth=2))
        ax.text(x, 3, "T", ha="center", va="center", fontsize=20, fontweight="bold")
        ax.text(x, 1.8, vote, ha="center", fontsize=11, fontweight="bold")

    for xp in tree_positions:
        ax.annotate("", xy=(4.5, 0.3), xytext=(xp, 1.2), arrowprops=dict(arrowstyle="->", lw=1.5))

    ax.text(4.5, 0, "Final answer: YES (majority vote: 3 vs 1)",
            ha="center", fontsize=12, fontweight="bold", color="#4C7A52")
    return fig


def boosting_diagram():
    """Sequential learning from mistakes - boosting concept"""
    fig, ax = plt.subplots(figsize=(8, 2.8))
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 3)
    ax.axis("off")

    steps = ["Model 1\n(many mistakes)", "Model 2\nfixes Model 1's\nmistakes",
             "Model 3\nfixes remaining\nmistakes", "Final\nstrong model"]
    colors = ["#fecaca", "#fde68a", "#bae6fd", "#bbf7d0"]
    xpos = [1, 3.5, 6, 8.5]

    for x, step, color in zip(xpos, steps, colors):
        ax.add_patch(patches.FancyBboxPatch((x-0.9, 0.8), 1.8, 1.4, boxstyle="round,pad=0.1",
                     facecolor=color, edgecolor="black", linewidth=2))
        ax.text(x, 1.5, step, ha="center", va="center", fontsize=9)

    for i in range(len(xpos)-1):
        ax.annotate("", xy=(xpos[i+1]-0.9, 1.5), xytext=(xpos[i]+0.9, 1.5),
                    arrowprops=dict(arrowstyle="->", lw=2))
    plt.tight_layout()
    return fig

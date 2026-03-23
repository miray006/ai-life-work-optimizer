import streamlit as st
import pandas as pd

# Page config
st.set_page_config(page_title="AI Life & Work Optimizer", layout="wide")

# Title
st.title("🚀 AI Life & Work Optimizer")
st.markdown("Plan your tasks, optimize your time, and improve productivity with AI-inspired logic.")

# Layout
col1, col2 = st.columns(2)

with col1:
    st.subheader("🧾 Inputs")
    
    goals = st.text_area("🎯 Goals")
    tasks = st.text_area("📝 Tasks (comma separated)")
    time = st.slider("⏱️ Available Hours", 1, 12, 4)

    generate = st.button("Generate Plan")

with col2:
    st.subheader("📊 Output")

if generate:

    if not tasks:
        st.warning("Please enter tasks.")
    else:
        task_list = [t.strip() for t in tasks.split(",") if t.strip()]

        # --- PRIORITY LOGIC ---
        priority_tasks = sorted(task_list, key=lambda x: len(x), reverse=True)

        # --- SCORING SYSTEM ---
        difficulty = sum(len(t) for t in task_list)
        score = int((time * 10) - (difficulty * 0.5))
        score = max(0, min(100, score))

        # --- OUTPUT ---
        with col2:

            st.subheader("📊 Productivity Score")

            st.metric(label="Score", value=f"{score} / 100")

            # Chart
            chart_data = pd.DataFrame({
                "Metric": ["Score"],
                "Value": [score]
            })

            st.bar_chart(chart_data.set_index("Metric"))

            st.subheader("📊 Priority Tasks")
            for i, task in enumerate(priority_tasks, 1):
                st.write(f"{i}. {task}")

            st.subheader("📅 Suggested Plan")

            for i in range(time):
                if i < len(priority_tasks):
                    st.write(f"Hour {i+1}: Focus on → {priority_tasks[i]}")
                else:
                    st.write(f"Hour {i+1}: Review / Break")

            st.subheader("💡 Suggestions")

            if score < 40:
                suggestions = [
                    "Reduce task load",
                    "Increase available time",
                    "Focus on top priority tasks only"
                ]
            elif score < 70:
                suggestions = [
                    "Improve task prioritization",
                    "Avoid multitasking",
                    "Group similar tasks"
                ]
            else:
                suggestions = [
                    "Great planning!",
                    "Maintain consistency",
                    "Optimize break intervals"
                ]

            for s in suggestions:
                st.write("•", s)
        
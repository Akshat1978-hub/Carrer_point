import streamlit as st
import pandas as pd
import plotly.express as px
from src.careers import CAREERS, recommend_careers, career_demand_history
from src.forecasting import forecast_demand
from src.quiz import QUESTIONS, score_quiz

st.set_page_config(page_title="CareerPredict AI", page_icon="🚀", layout="wide", initial_sidebar_state="expanded")
st.markdown("""
<style>
.stApp {background:linear-gradient(135deg,#081226 0%,#101a38 55%,#21163d 100%);color:#f4f7ff}
section[data-testid="stSidebar"] {background:#0a1226}
.hero {padding:1.5rem 1.7rem;border:1px solid #34456f;border-radius:22px;background:linear-gradient(120deg,rgba(27,57,110,.75),rgba(67,35,104,.7))}
.hero h1 {font-size:2.65rem;line-height:1.1;margin-bottom:.5rem;color:#fff}
.hero p {font-size:1.1rem;color:#d6e4ff}
.tag {display:inline-block;padding:.3rem .7rem;border-radius:999px;background:#19365a;color:#9ee7ff;margin:.2rem;font-size:.85rem}
.card {padding:1rem 1.1rem;border:1px solid #2c3d64;border-radius:16px;background:rgba(15,28,55,.8);min-height:115px}
div[data-testid="stMetric"] {background:rgba(17,34,65,.8);padding:12px;border-radius:14px;border:1px solid #2d426c}
</style>
""", unsafe_allow_html=True)

if "game_score" not in st.session_state:
    st.session_state.game_score = None

with st.sidebar:
    st.markdown("## 🚀 CareerPredict AI")
    st.caption("Explore possibilities. Discover tomorrow.")
    page = st.radio("Explore", ["🏠 Home", "🧭 Discover Careers", "📈 Future Predictor", "🪄 Scenario Simulator", "🎮 Career Quest", "🧠 How AI Forecasts"])
    st.markdown("---")
    st.caption("Python • Streamlit • Plotly")
    st.caption("Demo forecasts are illustrative, not guarantees.")

def header(title, subtitle):
    st.markdown(f"<div class='hero'><h1>{title}</h1><p>{subtitle}</p><span class='tag'>AI & Data Science</span><span class='tag'>Interactive learning</span><span class='tag'>No login needed</span></div>", unsafe_allow_html=True)
    st.write("")

if page == "🏠 Home":
    header("Your future has possibilities. 🌟", "Explore careers, understand changing job trends, and learn how forecasting works.")
    cols = st.columns(3)
    cards = [
        ("🧭 Discover", "Match your interests to careers and see why each path may suit you."),
        ("📈 Explore trends", "View illustrative demand scenarios and learn to read uncertainty."),
        ("🎮 Play & learn", "Try a quick career quiz and earn a Future Explorer result.")
    ]
    for col, (title, desc) in zip(cols, cards):
        with col:
            st.markdown(f"<div class='card'><h3>{title}</h3><p>{desc}</p></div>", unsafe_allow_html=True)
    st.write("")
    st.subheader("✨ Careers that shape tomorrow")
    cols = st.columns(4)
    for i, (name, info) in enumerate(list(CAREERS.items())[:8]):
        with cols[i % 4]:
            st.markdown(f"<div class='card'><h3>{info['icon']} {name}</h3><p>{', '.join(info['skills'][:3])}</p></div>", unsafe_allow_html=True)
    st.write("")
    st.info("Exhibition idea: ask a visitor to choose a career, change a scenario slider, then explain why the chart changes.")
    st.warning("The included trend series is synthetic demo data for demonstrating the interface. It is not official labour-market data.")

elif page == "🧭 Discover Careers":
    header("Find paths that fit your interests", "Answer a few questions. This is a learning tool, not a high-stakes aptitude test.")
    subjects = st.multiselect("Which subjects or topics do you enjoy?", ["Maths", "Science", "Computers", "Art & Design", "Biology", "Business", "Environment", "Writing & Communication"], default=["Computers", "Maths"])
    activities = st.multiselect("Which activities sound fun?", ["Solving puzzles", "Building apps", "Helping people", "Designing visuals", "Exploring nature", "Finding patterns in data", "Building machines", "Investigating security"], default=["Solving puzzles", "Finding patterns in data"])
    strengths = st.multiselect("Choose strengths you want to use", ["Logical thinking", "Creativity", "Communication", "Research", "Attention to detail", "Teamwork"], default=["Logical thinking", "Research"])
    comfort = st.slider("How comfortable are you with maths and problem-solving?", 1, 5, 3)
    if st.button("✨ Recommend my careers", type="primary"):
        st.session_state["career_results"] = recommend_careers(subjects, activities, strengths, comfort)
    results = st.session_state.get("career_results")
    if results:
        st.subheader("Your career matches")
        cols = st.columns(2)
        for idx, item in enumerate(results[:6]):
            with cols[idx % 2]:
                st.markdown(f"<div class='card'><h3>{item['icon']} {item['career']}</h3><h2>{item['match']}% match</h2><p>{item['why']}</p><p><b>Start with:</b> {item['first_step']}</p></div>", unsafe_allow_html=True)
                with st.expander("Skills to explore"):
                    st.write(", ".join(CAREERS[item["career"]]["skills"]))
        st.caption("Match scores reflect selected preferences only; they are not probabilities of career success or employment.")

elif page == "📈 Future Predictor":
    header("Explore career-demand trends", "Choose a career and time horizon to see an illustrative forecast with transparent assumptions.")
    st.warning("Data note: the included values are synthetic and are not real labour-market statistics. Replace the dataset with a documented official source before making factual claims.")
    career = st.selectbox("Career area", list(CAREERS.keys()))
    horizon = st.select_slider("Forecast horizon", options=[1, 3, 5, 10], value=5, format_func=lambda x: f"Next {x} year{'s' if x != 1 else ''}")
    hist = career_demand_history(career)
    fc = forecast_demand(hist, horizon)
    hist_df = pd.DataFrame({"Period": list(range(-len(hist)+1, 1)), "Index": hist, "Type": "Illustrative demo history"})
    future_df = pd.DataFrame({"Period": list(range(1, horizon+1)), "Index": fc["forecast"], "Type": "Illustrative scenario"})
    chart_df = pd.concat([hist_df, future_df], ignore_index=True)
    fig = px.line(chart_df, x="Period", y="Index", color="Type", markers=True,
                  color_discrete_map={"Illustrative demo history":"#52c7ff","Illustrative scenario":"#ffcf5a"},
                  title=f"Trend illustration: {career}")
    fig.update_layout(template="plotly_dark", paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)", xaxis_title="Relative time (0 = latest demo point)", yaxis_title="Synthetic index (not real data)")
    st.plotly_chart(fig, use_container_width=True)
    m1, m2, m3 = st.columns(3)
    m1.metric("Forecast horizon", f"{horizon} year(s)")
    m2.metric("Illustrative change", f"{fc['change_pct']:+.1f}%")
    m3.metric("Method", "Linear trend baseline")
    st.markdown("### How to read this")
    st.write("The chart extends a simple trend from synthetic example values. It teaches extrapolation but does not establish actual future demand. Real forecasts require a trustworthy dataset, backtesting, and uncertainty analysis.")
    with st.expander("View demo values"):
        st.dataframe(pd.DataFrame({"Demo point": range(1, len(hist)+1), "Synthetic index": hist}), use_container_width=True)

elif page == "🪄 Scenario Simulator":
    header("What if the world changes?", "Move the sliders and explore how assumptions can change a hypothetical scenario.")
    st.info("This is a transparent scenario simulator, not a trained predictive model.")
    career = st.selectbox("Career area to explore", list(CAREERS.keys()), key="scenario_career")
    a, b = st.columns(2)
    with a:
        tech = st.slider("Technology adoption", -30, 30, 10, 5)
        investment = st.slider("Industry investment", -30, 30, 5, 5)
    with b:
        automation = st.slider("Automation exposure", -30, 30, 0, 5)
        skills = st.slider("Skills adoption", -30, 30, 10, 5)
    base = CAREERS[career]["base_scenario"]
    effect = tech * CAREERS[career]["tech_weight"] / 100 + investment * .25 + skills * .35 - automation * CAREERS[career]["automation_weight"] / 100
    projected = max(0, base + effect)
    scenario = pd.DataFrame({"Scenario":["Cautious","Baseline","Your assumptions","Optimistic"], "Illustrative index":[max(0, base-18), base, projected, base+18]})
    fig = px.bar(scenario, x="Scenario", y="Illustrative index", color="Scenario",
                 color_discrete_sequence=["#9278ff","#52c7ff","#ffcf5a","#5ce1b6"], title="How assumptions change a hypothetical index")
    fig.update_layout(template="plotly_dark", paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)", showlegend=False)
    st.plotly_chart(fig, use_container_width=True)
    st.metric("Your scenario index", f"{projected:.1f}", delta=f"{projected-base:+.1f} vs baseline")
    st.markdown("**Why did it change?** The simulator uses an illustrative formula with career-specific sensitivity weights. The index is arbitrary; it is not job openings, salary, or employment probability.")

elif page == "🎮 Career Quest":
    header("Career Quest 🎮", "Answer quick questions and discover your Future Explorer style.")
    st.write("Choose one answer for each question. Your result is for fun and learning.")
    answers = {}
    for i, q in enumerate(QUESTIONS):
        answers[i] = st.radio(f"{i+1}. {q['question']}", q["options"], key=f"quest_{i}")
    if st.button("🏆 Reveal my result", type="primary"):
        score, feedback = score_quiz(answers)
        st.session_state.game_score = score
        st.session_state.game_feedback = feedback
    if st.session_state.game_score is not None:
        st.balloons()
        st.success(f"Quest complete! You scored {st.session_state.game_score}/{len(QUESTIONS)}.")
        st.subheader(st.session_state.game_feedback["title"])
        st.write(st.session_state.game_feedback["message"])
        st.caption("This quiz is not a formal intelligence or career aptitude assessment.")
        if st.button("Reset quiz"):
            st.session_state.game_score = None
            st.rerun()

elif page == "🧠 How AI Forecasts":
    header("How can AI estimate future trends?", "A simple, honest explanation for students and exhibition visitors.")
    steps = [
        ("1. Collect data", "Gather reliable historical observations and document their source."),
        ("2. Clean the data", "Handle missing values, inconsistent labels, and measurement changes."),
        ("3. Choose a baseline", "Start with a simple method before trying a complex model."),
        ("4. Test on the past", "Train on earlier observations and test on later data the model has not seen."),
        ("5. Forecast with uncertainty", "Show a range of plausible outcomes rather than pretending one number is certain."),
        ("6. Explain limitations", "Technology, policy, economic shocks, and human choices can change trends.")
    ]
    for title, desc in steps:
        st.markdown(f"<div class='card'><h3>{title}</h3><p>{desc}</p></div>", unsafe_allow_html=True)
        st.write("")
    st.subheader("Ask the audience")
    st.write("If a model predicts that demand may rise, what evidence supports it? What assumptions could make that prediction wrong?")
    st.info("For a production version, add an official dataset, cite its source and date, compare models with a baseline, and report appropriate backtesting metrics.")

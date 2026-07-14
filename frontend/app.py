import streamlit as st
import requests

API_URL = "http://127.0.0.1:8000"

st.set_page_config(
    page_title="Atlas AI",
    page_icon="🚀",
    layout="wide"
)

# ---------- Custom CSS ----------
st.markdown("""
<style>

.main {
    padding-top: 1rem;
}

.metric-card{
    background:#262730;
    padding:18px;
    border-radius:12px;
    border:1px solid #444;
}

.skill{
    display:inline-block;
    padding:8px 14px;
    margin:5px;
    border-radius:20px;
    font-weight:600;
}

.green{
    background:#d4edda;
    color:#155724;
}

.red{
    background:#f8d7da;
    color:#721c24;
}

.project-card{
    border:1px solid #444;
    border-radius:15px;
    padding:18px;
    margin-bottom:18px;
}

.score{
    font-size:22px;
    font-weight:bold;
    color:#00d084;
}

</style>
""", unsafe_allow_html=True)

st.title("🚀 Atlas AI")
st.caption("Your Personal AI Career Mentor")

# ---------- Fetch Data ----------

try:
    response = requests.get(f"{API_URL}/analyze")
    data = response.json()
except:
    st.error("Backend is not running.")
    st.stop()

# ---------- Top Metrics ----------

c1, c2, c3 = st.columns(3)

with c1:
    st.metric(
        "🎯 Career",
        data["career"]
    )

with c2:
    st.metric(
        "📈 Readiness",
        f'{data["readiness"]}%'
    )

with c3:
    st.metric(
        "⭐ Progress",
        f'{data["earned_points"]}/{data["total_points"]}'
    )

st.progress(data["readiness"]/100)

st.divider()

# ---------- Skills ----------

left,right = st.columns(2)

with left:

    st.subheader("✅ Current Skills")

    for skill in data["matched_skills"]:
        st.markdown(
            f'<span class="skill green">{skill}</span>',
            unsafe_allow_html=True
        )

with right:

    st.subheader("❌ Missing Skills")

    for skill in data["missing_skills"]:
        st.markdown(
            f'<span class="skill red">{skill}</span>',
            unsafe_allow_html=True
        )

st.divider()

# ---------- Projects ----------

st.header("📚 Recommended Projects")

for project in data["recommended_projects"]:

    with st.container(border=True):

        st.subheader(project["title"])

        st.write(
            f"**Difficulty:** {project['difficulty']}"
        )

        st.write(
            f"**Impact Score:** {project['score']}"
        )

        st.write("**Skills Covered**")

        st.write(", ".join(project["skills"]))
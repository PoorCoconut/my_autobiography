import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Cueshe Alforque | Portfolio",
    page_icon="🦊",
    layout="wide",
)

with st.sidebar:
    st.image("coco.jpg", caption="^ Yours truly ^", use_container_width=True)
    st.write("**Name:** Ryan Cueshe B. Alforque")
    st.write("**Section:** BSCS-3 F1")
    st.write("**Alias:** Cueshe")
    
    st.radio("Current Status:", ["Studying", "Developing", "Jamming"])

st.title("Cueshe Alforque's Portfolio")
st.write("Hey there! Welcome to my website! I am a 3rd Year BS Computer Science student.")

st.header("Autobiography")
col1, col2 = st.columns([2, 1])

with col1:
    st.write("I was born at a very young age. I live in Tungkop Minglanilla.")
    st.write("I attended my kindergarten, elementary, high school, and senior high school at Mary Help of Christians School.")
    st.write("My interests include anything that touches creativity: creating games, music, stories, and art.")
    
    show_milestones = st.checkbox("Show my proudest milestones")
    if show_milestones:
        st.success("♟️ Won 2nd in our school's Chess Competition")
        st.success("🕹️ Attended my first ever game jam with my friends [Sugbuanon Saga Game Jam]")
        st.success("🧠 Passed the DOST-JLSS Exam!")

with col2:
    st.metric(label="Songs Composed", value="200+")
    st.metric(label="Games Published", value="10")

st.divider()

st.header("Skills")

data = {
    "Skill": ["Composer", "Artist", "Game Developer", "Story Writer"],
    "Proficiency (%)": [80, 80, 85, 90],
    "Description": [
        "I've composed over 200 songs already. I find the seemingly infinite permutations of music fascinating.",
        "I draw traditionally with a pencil and draw a ton of pixel art digitally.",
        "Developing games is my dream. My ultimate goal is to develop my dream game.",
        "I am a world builder. Imagining worlds full of grand or grim things is always fun. Woooo hallucinations!"
    ],
}
df = pd.DataFrame(data)

skill_col1, skill_col2 = st.columns([2, 1])
with skill_col1:
    st.dataframe(df[["Skill", "Description"]], hide_index=True, use_container_width=True)
with skill_col2:
    st.bar_chart(df.set_index("Skill")["Proficiency (%)"])

st.divider()

st.header("My Top Projects")
tab1, tab2, tab3 = st.tabs(["Blind Harvest", "Void Vanguard", "Terminal Friction"])

with tab1:
    st.subheader("Blind Harvest")
    st.markdown("**Role:** Solo Developer | **Tools:** Godot Engine, Aseprite")
    st.write("Harvest crops and pay your debt at the dead of night whilst weird events happen!")
    st.link_button("Try Me!", 'https://poorcoco.itch.io/blind-harvest')

with tab2:
    st.subheader("Void Vanguard")
    st.markdown("**Role:** Solo Developer | **Tools:** Godot Engine, GDScript")
    st.write("Dispel The Void in this Asteroids-like arcade inspired game!")
    st.link_button("Try Me!", 'https://poorcoco.itch.io/void-vanguard')

with tab3:
    st.subheader("Terminal Friction")
    st.markdown("**Role:** Solo Developer | **Tools:** Godot Engine")
    st.write("Do you hate yourself and have time to waste? Try to slide to the top of a long tower designed to frustrate you.")
    st.link_button("Try Me!", 'https://poorcoco.itch.io/terminal-friction')

st.divider()

st.header("Got Feedback?")
st.write("Share them!")

with st.form("feedback_form"):
    visitor_type = st.selectbox("I am a:", ["Recruiter", "Fellow Developer", "Friend", "Just browsing"])
    
    user_text = st.text_area("Write feedback:", placeholder="Type here...")
    
    rating = st.slider("Rate my portfolio", min_value=1, max_value=10, value=10)
    
    submitted = st.form_submit_button("Submit Feedback")
    
    if submitted:
        if user_text:
            st.success(f"Thank you for sharing your thoughts! You rated this {rating}/10.")
        else:
            st.warning("Please type some feedback before submitting.")
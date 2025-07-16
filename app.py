import streamlit as st
from agents.search_agent import search_arxiv
from agents.classification import classify_paper_to_topic
from agents.synthesis_agent import synthesise_summary
from agents.audio_agent import text_to_audio_light
import os

st.set_page_config(page_title="Research Summarizer", layout="centered")
st.title("📚 Research Summarizer & Audio Generator")

# --- Step 1: Search Papers ---
st.header("🔍 1. Search Papers")
query = st.text_input("Enter a topic:", "AI summarization")
num_papers = st.slider("Number of papers", 1, 10, 3)

if st.button("Search"):
    with st.spinner("Searching papers..."):
        papers = search_arxiv(query, max_results=num_papers)
        st.session_state["papers"] = papers
    st.success(f"✅ Found {len(papers)} papers.")

# --- Step 2: Review Papers ---
if "papers" in st.session_state:
    st.header("2. Review Papers")
    for i, paper in enumerate(st.session_state["papers"], 1):
        st.markdown(f"**{i}. {paper['title']}**")
        st.write(f"Link: {paper['link']}")
        st.write(f"Published: {paper['Published']}")
        st.write(f"Summary: {paper['summary'][:300]}...")

# --- Step 3: Classify & Synthesize ---
if "papers" in st.session_state:
    st.header("3. Classify and Synthesize")
    topic_input = st.text_input("Enter topics (comma-separated):", "Natural Language Processing, Reinforcement Learning")

    if st.button("Classify & Summarize"):
        topics = [t.strip() for t in topic_input.split(",")]
        grouped = {}

        for paper in st.session_state["papers"]:
            topic, _ = classify_paper_to_topic(paper["summary"], topics)
            grouped.setdefault(topic, []).append(paper)  # full paper dictS

        with st.spinner("Summarizing..."):
            result = synthesise_summary(grouped)
            st.session_state["summary_result"] = result

# --- Step 4: Display Summary + Audio ---
if "summary_result" in st.session_state:
    st.header("4. Topic-wise Summaries & Audio")

    for topic, content in st.session_state["summary_result"].items():
        st.subheader(f"Topic: {topic}")
        st.write(content["summary"])
        st.markdown("**Sources:**")
        for src in content["sources"]:
            st.markdown(f"- [{src['title']}]({src['link']})")

        if st.button(f"Generate Audio for {topic}", key=f"audio_btn_{topic}"):
            audio_path = text_to_audio_light(content["summary"], filename=f"{topic}.mp3")
            st.session_state[f"audio_path_{topic}"] = audio_path
            st.success("Audio ready!")

        if f"audio_path_{topic}" in st.session_state:
            st.audio(st.session_state[f"audio_path_{topic}"])

            

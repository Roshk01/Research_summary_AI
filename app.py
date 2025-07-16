import streamlit as st
from agents.search_agent import search_arxiv
from agents.classification import classify_paper_to_topic
from agents.synthesis_agent import synthesise_summary
from agents.audio_agent import text_to_audio_light

st.set_page_config(page_title="Research Summarizer & Podcast", layout="centered")
st.title("📚 Research Summarizer & Audio Generator")

# ---- Step 1: Search papers ----
st.header("🔍 1. Search Research Papers")
query = st.text_input("Enter a research topic:", value="AI summarization")
num_papers = st.slider("Number of papers to fetch", 1, 10, 4)

if st.button("Fetch Papers"):
    with st.spinner("🔎 Searching papers..."):
        papers = search_arxiv(query, max_results=num_papers)
        st.session_state["papers"] = papers
    st.success(f"✅ Found {len(papers)} papers.")

# ---- Step 2: Review papers ----
if "papers" in st.session_state:
    st.header("📄 2. Review Fetched Papers")
    for i, paper in enumerate(st.session_state["papers"], 1):
        st.markdown(f"**{i}. {paper['title']}**")
        st.markdown(f"🔗 [Link to Paper]({paper['link']})")
        st.markdown(f"🕒 Published: {paper['Published']}")
        st.markdown(f"📝 Summary:\n{paper['summary'][:300]}...")

# ---- Step 3: Classify Summaries ----
if "papers" in st.session_state:
    st.header("🧠 3. Classify Summaries by Topic")
    topic_input = st.text_input("Enter comma-separated topics:", value="Natural Language Processing, Reinforcement Learning, Medical AI")

    if st.button("Classify & Group"):
        topics = [t.strip() for t in topic_input.split(",")]
        grouped = {}

        with st.spinner("🧠 Classifying summaries..."):
            for paper in st.session_state["papers"]:
                topic, score = classify_paper_to_topic(paper["summary"], topics)
                grouped.setdefault(topic, []).append(paper["summary"])

        st.session_state["grouped_summaries"] = grouped
        st.success("✅ Classification completed!")

# ---- Step 4: Synthesize Text Summaries and Generate Audio ----
if "grouped_summaries" in st.session_state:
    st.header("📄 4. Synthesize Summaries & Generate Audio")

    with st.spinner("📝 Synthesizing summaries using transformer..."):
        output = synthesise_summary(st.session_state["grouped_summaries"])

    for topic, summary_text in output.items():
        st.subheader(f"📌 {topic}")
        st.write(summary_text)

        if st.button(f"🔊 Generate Audio for {topic}", key=f"audio_{topic}"):
            audio_path = text_to_audio_light(summary_text, filename=f"{topic}.mp3")
            st.audio(audio_path)
            st.success("🎧 Audio generated for topic: " + topic)

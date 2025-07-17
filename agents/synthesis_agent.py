from transformers import pipeline

synthesizer = pipeline("summarization", model="sshleifer/distilbart-cnn-12-6")

def synthesise_summary(grouped_papers, max_chunk_len=1000):
    output = {}
    for topic, paper_list in grouped_papers.items():
        summaries = []
        sources = []
        for paper in paper_list:
            if isinstance(paper, dict):
                summaries.append(paper.get("summary", ""))
                sources.append({
                    "title": paper.get("title", "No Title"),
                    "link": paper.get("link", "#")
                })
            else:
                summaries.append(str(paper))  # fallback for stray strings

        combined_text = " ".join(summaries)
        if not combined_text.strip():
            output[topic] = {
                "summary": "No content to summarize.",
                "sources": sources
            }
            continue

        chunks = [combined_text[i:i + max_chunk_len] for i in range(0, len(combined_text), max_chunk_len)]
        topic_synthesis = []
        for chunk in chunks:
            result = synthesizer(chunk, max_length=150, min_length=40, do_sample=False)
            if isinstance(result, list) and "summary_text" in result[0]:
                topic_synthesis.append(result[0]["summary_text"])
            else:
                topic_synthesis.append("Summarization failed.")

        output[topic] = {
            "summary": " ".join(topic_synthesis),
            "sources": sources
        }

    return output
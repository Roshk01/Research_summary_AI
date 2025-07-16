from transformers import pipeline

synthesizer = pipeline("summarization", model="sshleifer/distilbart-cnn-12-6")

def synthesise_summary(grouped_papers, max_chunk_len=1000):
    output = {}

    for topic, paper_list in grouped_papers.items():
        # Combine all summaries into one chunk
        summaries = [paper["summary"] for paper in paper_list]
        combined_text = " ".join(summaries)

        for i, s in enumerate(summaries):
            if not isinstance(s, str):
                raise TypeError(f"[{topic}] Summary at index {i} is not a string: {type(s)} → {s}")

        # Chunk if too long
        chunks = [combined_text[i:i + max_chunk_len] for i in range(0, len(combined_text), max_chunk_len)]
        topic_synthesis = []

        for chunk in chunks:
            summary = synthesizer(chunk, max_length=150, min_length=40, do_sample=False)[0]["summary_text"]
            topic_synthesis.append(summary)

        # Attach synthesis + source mapping
        output[topic] = {
            "summary": " ".join(topic_synthesis),
            "sources": [{"title": p["title"], "link": p["link"]} for p in paper_list]
        }

    return output



grouped_data = {
    "Natural Language Processing": [
        {
            "title": "Understanding Transformers",
            "link": "http://arxiv.org/abs/1234.5678",
            "summary": "Transformer models have revolutionized NLP using attention mechanisms."
        },
        {
            "title": "BERT Fine-tuning Strategies",
            "link": "http://arxiv.org/abs/2345.6789",
            "summary": "Various fine-tuning methods have been explored to improve BERT on summarization."
        }
    ]
}

result = synthesise_summary(grouped_data)

for topic, content in result.items():
    print(f"\n🧠 {topic}:\nSummary:\n{content['summary']}")
    print("\n📚 Sources:")
    for src in content["sources"]:
        print(f"- {src['title']} → {src['link']}")
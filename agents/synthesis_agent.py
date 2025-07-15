from transformers import pipeline

summerizer = pipeline("summarization", model="sshleifer/distilbart-cnn-12-6")

def summarize_text(summarize_by_topic, max_chunk_len=1000):
    synthesized_output = []

    for topic, text in summarize_by_topic.items():
        combined_text = " ".join(text)
        chunks = [combined_text[i:i + max_chunk_len] for i in range(0,len(combined_text), max_chunk_len)]
        for chunk in chunks:
            chunk_summary = summerizer(chunk, max_length=150, min_length=40, do_sample=False)[0]['summary_text']
            synthesized_output.append(f"Topic: {topic}\nSummary: {chunk_summary}")

            return synthesized_output
from transformers import pipeline

summerizer = pipeline("summarization", model="sshleifer/distilbart-cnn-12-6")

def summarize_text(text, max_chunk_len = 1000):
    chunks = [text[i:i+max_chunk_len] for i in range (0, len(text), max_chunk_len)]
    summaries= []

    # iterate through each chunk and summarize
    for chunk in chunks:
        chunk_summary = summerizer(chunk,max_chunk_len,min_length= 50, do_sample=False)[0]['summary_text']
        summaries.append(chunk_summary)

        return " ".join(summaries)
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


def classify_paper_to_topic(paper_text, topic_keywords):
    documents = topic_keywords + [paper_text]

    # Create a TF-IDF Vectorizer
    vectorizer = TfidfVectorizer(stop_words='english')
    tfidf_matrix = vectorizer.fit_transform(documents)
    
    # Calculate cosine similarity
    similarity = cosine_similarity(tfidf_matrix[-1], tfidf_matrix[:-1]).flatten()

    # most similar topic
    best_match_index = similarity.argmax()
    best_match_topic = topic_keywords[best_match_index]

    return best_match_topic, similarity[best_match_index]



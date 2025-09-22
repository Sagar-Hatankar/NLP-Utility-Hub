from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np


FAQS = [
("What can you do?", "I can categorize news, parse resumes, analyze sentiment, extract keywords, and answer FAQ-style questions."),
("How do I upload a resume?", "Use the Resume Parser section and upload a PDF or DOCX file."),
("Which dataset does the news model use?", "It uses scikit-learn's 20 Newsgroups dataset for demonstration.")
]




def get_chatbot_response(query):
    corpus = [q for q,_ in FAQS]
    vect = TfidfVectorizer(stop_words='english')
    X = vect.fit_transform(corpus + [query])
    sims = cosine_similarity(X[-1], X[:-1])[0]
    idx = np.argmax(sims)
    if sims[idx] < 0.2:
        return "Sorry, I don't know the answer to that. Try asking about the app features."
    return FAQS[idx][1]
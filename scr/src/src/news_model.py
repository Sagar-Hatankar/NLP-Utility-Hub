from sklearn.datasets import fetch_20newsgroups
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import make_pipeline
from joblib import dump, load
import os


MODEL_PATH = "news_clf.joblib"




def train_news_model():
    data = fetch_20newsgroups(subset='train')
    clf = make_pipeline(TfidfVectorizer(stop_words='english', max_df=0.7), MultinomialNB())
    clf.fit(data.data, data.target)
    # save labels mapping
    dump({'model': clf, 'target_names': data.target_names}, MODEL_PATH)




def load_model():
    if os.path.exists(MODEL_PATH):
        d = load(MODEL_PATH)
        return d['model'], d['target_names']
    else:
        train_news_model()
        return load_model()




def predict_news_category(text):
    model, target_names = load_model()
    probs = model.predict_proba([text])[0]
    idx = probs.argmax()
    return target_names[idx], probs[idx]
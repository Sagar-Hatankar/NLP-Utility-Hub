import re
import io
import pdfplumber
from rake_nltk import Rake
from sklearn.feature_extraction.text import TfidfVectorizer




def extract_text_from_pdf_bytes(bytes_data):
    text = ""
    with pdfplumber.open(io.BytesIO(bytes_data)) as pdf:
        for page in pdf.pages:
            text += page.extract_text() or ""
    return text




def extract_text_from_upload(uploaded_file):
    name = uploaded_file.name.lower()
    data = uploaded_file.read()
    if name.endswith('.pdf'):
        return extract_text_from_pdf_bytes(data)
    elif name.endswith('.docx'):
        from docx import Document
        doc = Document(io.BytesIO(data))
        return "\n".join([p.text for p in doc.paragraphs])
    else:
        return data.decode('utf-8')




def top_keywords(text, top_n=10):
    # Try RAKE first
    r = Rake()
    r.extract_keywords_from_text(text)
    phrases = r.get_ranked_phrases()[:top_n]
    if len(phrases) >= top_n:
        return phrases
    # Fallback to TF-IDF on the single doc (chunk into sentences)
    sentences = re.split(r'[\n\.]', text)
    sentences = [s.strip() for s in sentences if s.strip()]
    vec = TfidfVectorizer(ngram_range=(1,2), stop_words='english')
    X = vec.fit_transform(sentences)
    sums = X.sum(axis=0)
    terms = vec.get_feature_names_out()
    scores = [(terms[i], sums[0,i]) for i in range(len(terms))]
    scores = sorted(scores, key=lambda x: x[1], reverse=True)
    return [t for t,_ in scores[:top_n]]
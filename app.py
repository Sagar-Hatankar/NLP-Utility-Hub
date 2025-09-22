import streamlit as st
from textblob import TextBlob
import nltk
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
# import language_tool_python  # Commented out to avoid Java dependency

# Download NLTK resources (only first time)
nltk.download('punkt')
nltk.download('stopwords')

# -----------------------------
# TRAIN SIMPLE NEWS CATEGORIZER
# -----------------------------
train_data = [
    ("The team won the football match", "Sports"),
    ("The stock market crashed today", "Business"),
    ("The government passed a new law", "Politics"),
    ("A new smartphone was launched", "Technology"),
    ("The actor won an award for best movie", "Entertainment"),
]
X_train, y_train = zip(*train_data)
vectorizer = CountVectorizer(stop_words="english")
X_vec = vectorizer.fit_transform(X_train)
classifier = MultinomialNB()
classifier.fit(X_vec, y_train)

def categorize_news(text):
    vec = vectorizer.transform([text])
    return classifier.predict(vec)[0]

# -----------------------------
# SIMPLE CHATBOT (RULE-BASED)
# -----------------------------
def simple_chatbot(user_input):
    user_input = user_input.lower()
    if "hello" in user_input or "hi" in user_input:
        return "Hello! How can I help you today?"
    elif "your name" in user_input:
        return "I'm your NLP Utility Hub chatbot 🤖"
    elif "bye" in user_input:
        return "Goodbye! Have a nice day."
    else:
        return "I'm still learning. Could you rephrase that?"

# -----------------------------
# RESUME PARSER (Keyword-based)
# -----------------------------
def parse_resume(text):
    lines = text.split("\n")
    skills = []
    education = []
    experience = []
    for line in lines:
        line_lower = line.lower()
        if "experience" in line_lower or "worked" in line_lower:
            experience.append(line.strip())
        elif "university" in line_lower or "college" in line_lower:
            education.append(line.strip())
        elif "python" in line_lower or "nlp" in line_lower or "machine learning" in line_lower:
            skills.append(line.strip())
    return skills, education, experience

# -----------------------------
# GRAMMAR CHECKER
# -----------------------------
def grammar_check(text):
    # Simplified version without language_tool_python (requires Java)
    return text, []  # Return original text and empty matches list

# -----------------------------
# SENTIMENT ANALYSIS
# -----------------------------
def analyze_sentiment(text):
    blob = TextBlob(text)
    polarity = blob.sentiment.polarity
    if polarity > 0:
        return "Positive 😊"
    elif polarity < 0:
        return "Negative 😞"
    else:
        return "Neutral 😐"

# -----------------------------
# STREAMLIT UI
# -----------------------------
st.set_page_config(page_title="NLP Utility Hub", page_icon="🧰", layout="wide")
st.title("🧰 NLP Utility Hub")

menu = ["News Categorizer", "Simple Chatbot", "Resume Parser", "Grammar Checker", "Sentiment Analysis"]
choice = st.sidebar.selectbox("Choose a tool:", menu)

if choice == "News Categorizer":
    st.header("📰 News Categorizer")
    text = st.text_area("Enter a news article:")
    if st.button("Categorize"):
        if text.strip():
            category = categorize_news(text)
            st.success(f"**Predicted Category:** {category}")
        else:
            st.warning("⚠ Please enter a news article.")

elif choice == "Simple Chatbot":
    st.header("💬 Simple Chatbot")
    user_input = st.text_input("You:")
    if st.button("Send"):
        if user_input.strip():
            response = simple_chatbot(user_input)
            st.info(f"**Bot:** {response}")
        else:
            st.warning("⚠ Please enter a message.")

elif choice == "Resume Parser":
    st.header("📄 Resume Parser")
    resume_text = st.text_area("Paste your resume text:")
    if st.button("Parse"):
        skills, education, experience = parse_resume(resume_text)
        st.subheader("✅ Skills Found:")
        st.write(skills if skills else "No skills found.")
        st.subheader("🎓 Education Found:")
        st.write(education if education else "No education found.")
        st.subheader("💼 Experience Found:")
        st.write(experience if experience else "No experience found.")

elif choice == "Grammar Checker":
    st.header("✍️ Grammar Checker")
    text = st.text_area("Enter text to check grammar:")
    if st.button("Check"):
        if text.strip():
            corrected, matches = grammar_check(text)
            st.subheader("✅ Corrected Text:")
            st.success(corrected)
            st.subheader("⚠ Issues Found:")
            for match in matches:
                st.write(f"- {match.ruleId}: {match.message}")
        else:
            st.warning("⚠ Please enter some text.")

elif choice == "Sentiment Analysis":
    st.header("🧠 Sentiment Analysis")
    text = st.text_area("Enter text to analyze sentiment:")
    if st.button("Analyze"):
        if text.strip():
            sentiment = analyze_sentiment(text)
            st.success(f"**Sentiment:** {sentiment}")
        else:
            st.warning("⚠ Please enter some text.")
from scr.src.src.resume_parser import parse_resume_file
from scr.src.chatbot import get_chatbot_response    
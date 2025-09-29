# 🧰 NLP Utility Hub

A comprehensive Natural Language Processing (NLP) utility application built with Streamlit that provides multiple text analysis and processing tools in one convenient interface.

![Python](https://img.shields.io/badge/Python-3.7%2B-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-Latest-red)
![License](https://img.shields.io/badge/License-MIT-green)
![Status](https://img.shields.io/badge/Status-Active-brightgreen)

## 🌟 Features

### 📰 News Categorizer
- Automatically categorizes news articles into predefined categories
- Uses machine learning with Naive Bayes classifier
- Categories: Sports, Business, Politics, Technology, Entertainment

### 💬 Simple Chatbot
- Rule-based conversational AI agent
- FAQ-style responses using pattern matching
- Interactive chat interface

### 📄 Resume Parser
- Extracts key information from resumes
- Identifies skills, education, and work experience
- Supports text input for now.

### ✍️ Grammar Checker
- Basic grammar and spell checking functionality
- Text correction suggestions
- Requires Java for full functionality

### 🧠 Sentiment Analysis
- Analyzes text sentiment using TextBlob
- Returns sentiment classification: Positive 😊, Negative 😞, or Neutral 😐
- Real-time sentiment scoring

## 🚀 Quick Start

### Prerequisites
- Python 3.7 or higher
- Windows PowerShell
- Java (optional, for full grammar checker functionality)

### Installation

1. **Clone the repository**
   ```powershell
   git clone https://github.com/Sagar-Hatankar/NLP-Utility-Hub.git
   cd NLP-Utility-Hub
   ```

2. **Create and activate virtual environment**
   ```powershell
   python -m venv venv
   venv\Scripts\Activate.ps1
   ```

3. **Install dependencies**
   ```powershell
   pip install -r requirements.txt
   ```

4. **Download NLTK data**
   ```powershell
   python -c "import nltk; nltk.download('punkt'); nltk.download('stopwords')"
   ```

### Running the Application

```powershell
streamlit run app.py
```

Access the application at: `http://localhost:8501`

## 📁 Project Structure

```
NLP-Utility-Hub/
├── app.py                          # Main Streamlit application
├── requirements.txt                # Python dependencies
├── README.md                       # Project documentation
├── PROJECT_SETUP_GUIDE.md         # Detailed setup guide
├── venv/                          # Virtual environment (created after setup)
└── scr/
    └── src/
        ├── chatbot.py             # Enhanced chatbot functionality
        ├── utils.py               # Utility functions
        └── src/
            ├── news_model.py      # News categorization model
            └── resume_parser.py   # Advanced resume parsing functions
```

## 🛠️ Technologies Used

- **Frontend**: Streamlit
- **NLP Libraries**: 
  - NLTK
  - TextBlob
  - Transformers
- **Machine Learning**: 
  - Scikit-learn
  - TensorFlow
- **Document Processing**: 
  - PyPDF2
  - pdfplumber
  - python-docx
- **Text Processing**: 
  - RAKE-NLTK
  - language-tool-python

## 📊 Usage Examples

### News Categorization
```python
# Input: "The team won the football match"
# Output: "Sports"
```

### Sentiment Analysis
```python
# Input: "I love this product!"
# Output: "Positive 😊"
```

### Chatbot Interaction
```
User: "Hello"
Bot: "Hello! How can I help you today?"
```

## 🔧 Configuration

### Environment Variables (Optional)
```powershell
$env:STREAMLIT_SERVER_PORT = "8501"
$env:STREAMLIT_SERVER_ADDRESS = "localhost"
```

### Custom Settings
- Modify news categories in `app.py`
- Extend chatbot responses in `scr/src/chatbot.py`
- Customize resume parsing rules in `scr/src/src/resume_parser.py`

## 🐛 Troubleshooting

### Common Issues

1. **ModuleNotFoundError**
   - Ensure virtual environment is activated
   - Reinstall dependencies: `pip install -r requirements.txt`

2. **Grammar Checker Issues**
   - Install Java from [java.com](https://www.java.com/download/)
   - Application works without Java but with limited grammar checking

3. **Port Already in Use**
   ```powershell
   streamlit run app.py --server.port 8502
   ```

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👨‍💻 Author

**Sagar Hatankar**
- GitHub: [@Sagar-Hatankar](https://github.com/Sagar-Hatankar)
- Repository: [NLP-Utility-Hub](https://github.com/Sagar-Hatankar/NLP-Utility-Hub)

## 🙏 Acknowledgments

- Streamlit team for the amazing web framework
- NLTK and TextBlob communities for NLP tools
- Scikit-learn for machine learning capabilities
- All contributors and users of this project

## 🔮 Future Enhancements

- [ ] Advanced deep learning models for better accuracy
- [ ] Multi-language support
- [ ] Real-time file upload and processing
- [ ] User authentication and personalization
- [ ] API endpoints for external integration
- [ ] Enhanced chatbot with conversational AI
- [ ] Export functionality for analysis results

## 📞 Support

For support, issues, or feature requests:
- Open an issue on [GitHub](https://github.com/Sagar-Hatankar/NLP-Utility-Hub/issues)

---

⭐ **Star this repository if you find it helpful!**

Last Updated: September 29, 2025
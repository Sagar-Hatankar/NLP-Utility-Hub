# NLP Utility Hub - Project Setup Guide

## 📋 Project Overview
This is a comprehensive NLP (Natural Language Processing) Utility Hub built with Streamlit that includes:
- News Categorizer
- Simple Chatbot
- Resume Parser
- Grammar Checker
- Sentiment Analysis

## 🛠️ Prerequisites
- Python 3.7 or higher
- Windows PowerShell
- Java (optional, for full grammar checker functionality)

## 📁 Project Structure
```
Sagar/
├── app.py                          # Main Streamlit application
├── requirements.txt                # Python dependencies
├── venv/                          # Virtual environment folder
├── scr/
│   └── src/
│       ├── chatbot.py             # Chatbot functionality
│       ├── utils.py               # Utility functions
│       └── src/
│           ├── news_model.py      # News categorization model
│           └── resume_parser.py   # Resume parsing functions
└── PROJECT_SETUP_GUIDE.md        # This guide
```

## 🚀 Step-by-Step Setup Instructions

### 1. Initial Setup (One-time only)

#### Create Virtual Environment
```powershell
# Navigate to project directory
cd C:\Users\dell\Sagar

# Create virtual environment (if not already created)
python -m venv venv
```

#### Enable Script Execution (if needed)
```powershell
# Allow PowerShell to run activation scripts
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser -Force
```

### 2. Activate Virtual Environment

```powershell
# Method 1: Using PowerShell script (recommended)
C:\Users\dell\Sagar\venv\Scripts\Activate.ps1

# Method 2: Using batch file (alternative)
C:\Users\dell\Sagar\venv\Scripts\activate.bat

# Verify activation - you should see (venv) in your prompt
# Example: (venv) PS C:\Users\dell\Sagar>
```

### 3. Install Dependencies

```powershell
# Make sure virtual environment is activated first!
# Install all required packages
pip install -r requirements.txt

# Download required NLTK data
python -c "import nltk; nltk.download('punkt'); nltk.download('stopwords')"
```

### 4. Run the Application

```powershell
# Make sure virtual environment is activated
# Start the Streamlit application
streamlit run app.py
```

### 5. Access the Application
- **Local URL:** http://localhost:8501
- **Network URL:** http://192.168.0.108:8501 (or your local IP)

### 6. Deactivate Virtual Environment

```powershell
# When you're done working on the project
deactivate
```

## 🔄 Daily Workflow

### Starting Work Session
```powershell
# 1. Navigate to project
cd C:\Users\dell\Sagar

# 2. Activate virtual environment
C:\Users\dell\Sagar\venv\Scripts\Activate.ps1

# 3. Verify activation (should show (venv) in prompt)
python --version

# 4. Run the application
streamlit run app.py
```

### Ending Work Session
```powershell
# 1. Stop Streamlit (Ctrl+C in terminal)
# 2. Deactivate virtual environment
deactivate
```

## 📦 Package Management

### Install New Packages
```powershell
# Activate virtual environment first
C:\Users\dell\Sagar\venv\Scripts\Activate.ps1

# Install new package
pip install package-name

# Update requirements.txt
pip freeze > requirements.txt
```

### View Installed Packages
```powershell
# List all installed packages
pip list

# Show specific package info
pip show package-name
```

## 🐛 Troubleshooting

### Common Issues and Solutions

#### 1. "Scripts is disabled on this system" Error
```powershell
# Solution: Enable script execution
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser -Force
```

#### 2. "ModuleNotFoundError" for packages
```powershell
# Solution: Make sure virtual environment is activated
C:\Users\dell\Sagar\venv\Scripts\Activate.ps1

# If still not working, reinstall packages
pip install -r requirements.txt
```

#### 3. "No java install detected" for Grammar Checker
```powershell
# Solution 1: Install Java from https://www.java.com/download/
# Solution 2: The app runs without full grammar checker functionality
```

#### 4. Port Already in Use (8501)
```powershell
# Solution: Use different port
streamlit run app.py --server.port 8502
```

#### 5. Virtual Environment Not Activating
```powershell
# Alternative activation method
& C:\Users\dell\Sagar\venv\Scripts\activate.bat
```

## 🔧 Virtual Environment Management

### Check Virtual Environment Status
```powershell
# Check if virtual environment is active
python -c "import sys; print('Virtual env active:', 'venv' in sys.executable)"

# Show Python executable path
python -c "import sys; print(sys.executable)"
```

### Recreate Virtual Environment (if corrupted)
```powershell
# Remove existing virtual environment
Remove-Item -Recurse -Force venv

# Create new virtual environment
python -m venv venv

# Activate and install packages
C:\Users\dell\Sagar\venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

### Environment Variables (optional)
```powershell
# Set environment variables for the session
$env:STREAMLIT_SERVER_PORT = "8501"
$env:STREAMLIT_SERVER_ADDRESS = "localhost"
```

## 📝 Quick Reference Commands

### Essential Commands
```powershell
# Activate venv
C:\Users\dell\Sagar\venv\Scripts\Activate.ps1

# Run app
streamlit run app.py

# Install packages
pip install package-name

# Deactivate venv
deactivate
```

### Development Commands
```powershell
# Check Python version
python --version

# List packages
pip list

# Update all packages
pip list --outdated
pip install --upgrade package-name

# Generate requirements
pip freeze > requirements.txt
```

## 🌟 Features Available

### 1. News Categorizer
- Categorizes news articles into predefined categories
- Uses scikit-learn's Naive Bayes classifier

### 2. Simple Chatbot
- Rule-based conversational agent
- FAQ-style responses using TF-IDF similarity

### 3. Resume Parser
- Extracts information from PDF/DOCX resumes
- Identifies skills, education, and experience

### 4. Grammar Checker
- Basic grammar checking functionality
- Full functionality requires Java installation

### 5. Sentiment Analysis
- Analyzes text sentiment using TextBlob
- Returns Positive, Negative, or Neutral sentiment

## 🔒 Security Notes

- Virtual environment keeps your system Python clean
- Packages are isolated to this project only
- Execution policy changes only affect current user
- No system-wide modifications required

## 📞 Support

If you encounter issues:
1. Check this guide first
2. Verify virtual environment is activated
3. Ensure all dependencies are installed
4. Check Python and package versions

## 🎯 Next Steps

- Install Java for full grammar checker functionality
- Customize the news categories in `app.py`
- Add more sophisticated NLP models
- Enhance the chatbot with better responses
- Add file upload functionality for resume parser

---

**Happy Coding! 🚀**

Last Updated: September 23, 2025
import re
from scr.src.utils import extract_text_from_upload


EMAIL_RE = re.compile(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}")
PHONE_RE = re.compile(r"(\+?\d[\d\-() ]{7,}\d)")


SKILLS_DB = [
'python','java','c++','sql','excel','pandas','numpy','scikit-learn','machine learning','deep learning',
'nlp','natural language processing','tensorflow','pytorch','docker','aws'
]


EDU_KEYWORDS = ['bachelor', 'master', 'phd', 'b.sc', 'bachelor of', 'master of', 'msc', 'ba', 'bs']




def parse_resume_file(uploaded_file):
    text = extract_text_from_upload(uploaded_file)
    text_low = text.lower()
    emails = EMAIL_RE.findall(text)
    phones = PHONE_RE.findall(text)
    skills = [s for s in SKILLS_DB if s in text_low]
    education = [line for line in text.split('\n') if any(k in line.lower() for k in EDU_KEYWORDS)]
    name = None
    # naive name extraction: assume first non-empty line is name if it's short
    for line in text.split('\n'):
        if line.strip():
            if 2 <= len(line.split()) <= 4 and not EMAIL_RE.search(line) and not PHONE_RE.search(line):
                name = line.strip()
                break
    return {
        'name': name,
        'emails': emails,
        'phones': phones,
        'skills': skills,
        'education_lines': education,
        'raw_text_snippet': text[:1000]
    }
# 🤖 Bias-Free Recruitment AI

## Overview
Bias-Free Recruitment AI detects and mitigates biased language in job descriptions using both dictionary-based checks and a fine-tuned BERT model. It highlights gender and age bias, suggests neutral alternatives, and provides analytics dashboards to help HR teams align with diversity and inclusion goals.

## Features
- ⚠️ Detects biased words and phrases (gender, age, etc.)
- 🤖 Transformer-based subtle bias detection (BERT/DistilBERT)
- 🔄 Suggests neutral alternatives for biased terms
- 📊 Analytics dashboard with bias scores and category breakdowns
- 🌐 Streamlit interface for interactive use

## Tech Stack
- Python (Pandas, NLTK, Scikit-Learn)
- HuggingFace Transformers (BERT/DistilBERT)
- Streamlit (dashboard)
- Matplotlib/Seaborn (visualizations)

## Installation
Clone the repository and install dependencies:
```bash
git clone https://github.com/<your-username>/bias-free-recruitment-ai.git
cd bias-free-recruitment-ai
pip install -r requirements.txt
Usage
Run the Streamlit app:

bash
streamlit run app.py
Paste a job description into the dashboard to analyze bias, view suggestions, and explore analytics.

Business Impact
This project helps recruiters reduce unconscious bias in hiring, supports diversity and inclusion initiatives, and improves candidate experience by ensuring fair and neutral job postings.
Future Scope
Resume bias detection

Multilingual support

Cloud deployment (Azure/AWS/GCP)

Integration with Applicant Tracking Systems (ATS)
## Screenshots

### Dashboard
![Dashboard Screenshot](Screenshot%202026-04-05%20112256.png)

### Suggestions Tab
![Suggestions Screenshot](Screenshot%202026-04-05%20112347.png)

### Analytics Tab
![Analytics Screenshot](Screenshot%202026-04-05%20112432.png)

### Transformer Output
![Transformer Screenshot](Screenshot%202026-04-05%20112502.png)
git add README.md screenshots/
git commit -m "Added screenshots to README"
git push


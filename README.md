# Persona-Driven Document Intelligence (Offline)

**Adobe India Hackathon 2025 – Round 1B Submission**

Built by:
- ✨ Divya — [ddivya_be23@thapar.edu]  
- ✨ Harman Preet Singh — [hsingh6_be23@thapar.edu]

---

## 🚀 Project Overview

This solution processes multi-page documents to extract and rank content **most relevant to a persona’s goals**. Given a `persona.json` and one or more documents, the system outputs ranked sections based on semantic similarity to the persona’s objective.

Everything runs **completely offline** — all models and dependencies are included in the container for use in secure, air-gapped environments.

---

## ✅ Features

- Multilingual document support (English, Hindi, etc.)
- Fast: ~2–5 sec per 50-page PDF
- Supports `.pdf`, `.txt`, `.docx`
- Offline transformer model
- Output saved per file as `<filename>.json`
- Fully Dockerized with local wheels

---

## 🏗️ Project Structure

Round1b/
├── app/
│ ├── input/ # Drop input PDFs here
│ ├── output/ # Output JSONs go here
│ ├── model/ # Pre-downloaded transformer model
│ ├── main.py # Entry-point script
│ └── persona.json # Persona configuration
├── wheels/ # All offline Python dependencies
├── requirements.txt # List of Python packages
├── Dockerfile # Builds offline container
├── download_model.py # One-time model download
├── README.md # This file
├── approach_explanation.md # Methodology explained

yaml

---

## 📦 persona.json Format

```json
{
  "persona": "HR Manager at Adobe",
  "goal": "Streamline employee onboarding using AI"
}
🔧 Requirements
Docker Desktop (WSL2 for Windows)

~600MB disk space

🛠️ Build Docker Image

docker build --platform linux/amd64 -t persona-sidhu:securev1 .

▶️ Run Your Solution

bash

docker run --rm \
  -v $(pwd)/app/input:/app/input \
  -v $(pwd)/app/output:/app/output \
  --network none \
  persona-sidhu:securev1
The container will:

Read all .pdf files in /app/input

Process and extract relevant sections

Save results as /app/output/<filename>.json

🧪 Run Without Docker
Only for local testing (optional):

bash

pip install --no-index --find-links=wheels -r requirements.txt
python app/main.py
🧠 How It Works
Load persona from persona.json

Split each input document into sections (pages or headings)

Embed each section + persona using sentence-transformers/all-MiniLM-L6-v2

Rank sections by cosine similarity

Output top-ranked content as JSON

📝 Output Format
Each input file (sample.pdf) generates an output like:

json

[
  {
    "section_title": "Introduction to AI in HR",
    "score": 0.89,
    "content": "AI enables faster onboarding and improves efficiency..."
  }
]

👥 Team Credits
Divya — [ddivya_be23@thapar.edu]

Harman Preet Singh — [hsingh6_be23@thapar.edu]

Challenge: Adobe India Hackathon 2025 – Round 1B
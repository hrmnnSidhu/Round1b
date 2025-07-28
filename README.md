**Round 1B Submission – Adobe India Hackathon 2025**  
Built by:  
- ✨ Divya — [ddivya_be23@thapar.edu]  
- ✨ Harman Preet Singh — [hsingh6_be23@thapar.edu]  

---

## 🚀 Overview

This solution extracts task-relevant information from multi-page documents based on a `persona.json` configuration file. It scores each section of the document using semantic similarity to the persona’s goals and ranks them accordingly.

> 💡 Everything runs **fully offline**, including model inference and dependencies — suitable for air-gapped or secure environments.

---

## 🧠 Features

- ✅ Supports **multilingual documents**
- ✅ Uses **offline language models**
- ✅ Accepts `.pdf`, `.txt`, `.docx` documents
- ✅ Outputs ranked JSON for top relevant sections
- ✅ Fast runtime (~2–5 sec for 50 pages)

---

## 🏗️ Folder Structure

```
project/
├── app/
│   ├── input/                ← Drop input documents here
│   ├── output/               ← Extracted + ranked content (JSON)
│   ├── model/                ← Offline transformer model (downloaded)
│   ├── main.py               ← Main code for processing + ranking
│   └── persona.json          ← Persona config file
├── wheels/                   ← Offline `.whl` packages
├── requirements.txt          ← Python dependency list
├── Dockerfile                ← Offline Docker config
├── download_model.py         ← Optional: model download script
├── README.md                 ← You are here
```

---

## 🔧 Requirements

- Docker Desktop with WSL2 backend (Windows/Linux)
- Python 3.10+ (if running without Docker)

---

## 🔌 Offline Setup Instructions

### 1. ✅ Download Dependencies

Use the following command (already done):

```bash
pip download -d wheels -r requirements.txt
```

---

### 2. ✅ Build Docker Image

```powershell
docker build -t persona-offline .
```

---

### 3. ✅ Run the Container

```powershell
docker run --rm `
  -v "${PWD}\app\input:/app/input" `
  -v "${PWD}\app\output:/app/output" `
  -v "${PWD}\app\persona.json:/app/persona.json" `
  -v "${PWD}\app\model:/app/model" `
  persona-offline
```

---

## 🧪 Run Without Docker (For Testing)

```bash
pip install --no-index --find-links=wheels -r requirements.txt
python app/main.py
```

---

## 📦 Output Format

The output file will be generated at:

```
app/output/ranked_output.json
```

Example:
```json
[
  {
    "section_title": "Introduction to AI in HR",
    "score": 0.89,
    "content": "AI enables faster onboarding and improves efficiency..."
  }
]
```

---

## 🧠 How It Works

1. `main.py` loads the persona objective from `persona.json`
2. The document is broken into sections and vectorized using a sentence-transformer model
3. Each section is scored by cosine similarity to the persona vector
4. Ranked output is stored in `output/`

---

## 📥 Persona Config Format

`app/persona.json` should follow this structure:

```json
{
  "persona": "HR Manager at Adobe",
  "goal": "Improve onboarding efficiency using AI tools"
}
```

---

## 📚 Credits

- **Team:** Divya & Harman Preet Singh    
- **Challenge:** Adobe India Hackathon 2025 – Round 1B

---


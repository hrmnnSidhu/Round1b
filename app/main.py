import os
import json
import fitz  # PyMuPDF
from sentence_transformers import SentenceTransformer, util

# Load persona from JSON
with open("app/persona.json", "r", encoding="utf-8") as f:
    persona_data = json.load(f)
persona_desc = persona_data.get("persona_description", "")

# Load the multilingual sentence transformer model (offline)
model = SentenceTransformer("app/model/sbert-all-MiniLM-L6-v2")


# PDF input file
input_dir = "app/input"
pdf_files = [f for f in os.listdir(input_dir) if f.endswith(".pdf")]

if not pdf_files:
    print("❌ No PDF file found in input folder.")
    exit()

pdf_path = os.path.join(input_dir, pdf_files[0])

# Extract paragraphs from PDF
doc = fitz.open(pdf_path)
paragraphs = []

for page in doc:
    blocks = page.get_text("dict")["blocks"]
    for block in blocks:
        if block["type"] == 0:  # text block
            for line in block["lines"]:
                para = " ".join([span["text"] for span in line["spans"]]).strip()
                if para:
                    paragraphs.append(para)

# Embed persona and paragraphs
persona_embedding = model.encode(persona_desc, convert_to_tensor=True)
ranked = []

for para in paragraphs:
    para_embedding = model.encode(para, convert_to_tensor=True)
    score = util.cos_sim(persona_embedding, para_embedding).item()
    ranked.append((para, score))

# Sort by similarity score
ranked.sort(key=lambda x: x[1], reverse=True)

# Save top 30 ranked paragraphs to JSON
output_data = [
    {"paragraph": para, "score": round(score, 4)}
    for para, score in ranked[:30]
]

output_path = "app/output/ranked_output.json"
with open(output_path, "w", encoding="utf-8") as f:
    json.dump(output_data, f, indent=2, ensure_ascii=False)

print(f"✅ Top {len(output_data)} relevant paragraphs saved to {output_path}")

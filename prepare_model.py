from sentence_transformers import SentenceTransformer

# Load from HuggingFace (must be online only this once)
model = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")

# Save locally as proper offline format
model.save("app/model/sbert-all-MiniLM-L6-v2")

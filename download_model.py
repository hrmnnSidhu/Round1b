from sentence_transformers import SentenceTransformer

model_name = "sentence-transformers/all-MiniLM-L6-v2"
print(f"Downloading model: {model_name}")
model = SentenceTransformer(model_name, cache_folder="./app/model")
print("Download complete.")

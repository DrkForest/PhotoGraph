# from app.application import run


# if __name__ == "__main__":
#     run()

from pathlib import Path

from core.clip.embeddings import generate_embedding

vector = generate_embedding(
    Path("E:/DEV/PhotoGraph/data/thumbnails/SHVETSOV DRKFOREST-05889.webp")
)

print(vector.shape)
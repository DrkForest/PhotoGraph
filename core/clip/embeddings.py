from pathlib import Path

import torch
from PIL import Image

from core.clip.model import get_clip_model


def generate_embedding(image_path: Path):

    clip = get_clip_model()

    image = Image.open(image_path).convert("RGB")

    image = clip.preprocess(image).unsqueeze(0)

    image = image.to(clip.device)

    with torch.no_grad():

        embedding = clip.model.encode_image(image)

        embedding /= embedding.norm(dim=-1, keepdim=True)

    return embedding.squeeze(0).cpu().numpy()
import torch
import open_clip


class ClipModel:

    def __init__(self):

        self.device = (
            "cuda"
            if torch.cuda.is_available()
            else "cpu"
        )

        self.model = None
        self.preprocess = None

    def load(self):

        if self.model is not None:
            return self

        self.model, _, self.preprocess = open_clip.create_model_and_transforms(
            "ViT-B-32",
            pretrained="laion2b_s34b_b79k"
        )

        self.model.to(self.device)
        self.model.eval()

        return self


_clip_instance = None


def get_clip_model():

    global _clip_instance

    if _clip_instance is None:

        _clip_instance = ClipModel()

        _clip_instance.load()

    return _clip_instance
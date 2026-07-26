from dataclasses import dataclass, field
from pathlib import Path

import numpy as np


@dataclass(slots=True)
class Photo:

    image: Path

    thumbnail: Path | None = None

    embedding: np.ndarray | None = None

    neighbours: list["Photo"] = field(default_factory=list)
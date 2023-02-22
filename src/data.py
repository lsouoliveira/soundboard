from dataclasses import dataclass

@dataclass
class Song:
    name: str
    duration: int
    path: str
    is_playing: bool = False


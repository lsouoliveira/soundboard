from dataclasses import dataclass

@dataclass
class Song:
    name: str
    duration: str
    path: str
    is_playing: bool = False


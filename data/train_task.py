from dataclasses import dataclass

@dataclass
class TrainTask:
    id: str
    origin: str
    destination: str
    departure: int
    arrival: int
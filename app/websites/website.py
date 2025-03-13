from dataclasses import dataclass

@dataclass
class Website:
    url: str
    active: bool = True
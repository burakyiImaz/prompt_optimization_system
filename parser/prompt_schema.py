from dataclasses import dataclass


@dataclass
class PromptRule:
    id: int
    text: str
    rule_type: str
    importance: float = 1.0
    protected: bool = False
    metadata: dict = None
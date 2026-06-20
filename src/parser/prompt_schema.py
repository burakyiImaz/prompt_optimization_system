from dataclasses import dataclass


@dataclass
class PromptRule:
    id: int
    text: str
    rule_type: str
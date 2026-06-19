from dataclasses import dataclass


@dataclass
class PromptRule:
    text: str
    rule_type: str
from prompt_schema import PromptRule


class PromptParser:

    def __init__(self):
        pass

    def classify_rule(self, line: str) -> str:

        line_lower = line.lower()

        if "you are" in line_lower:
            return "role"

        if line_lower.startswith("always"):
            return "instruction"

        if line_lower.startswith("never"):
            return "constraint"

        if line_lower.startswith("if"):
            return "condition"

        return "general"

    def parse(self, prompt: str):

        rules = []

        lines = prompt.split("\n")

        for line in lines:

            line = line.strip()

            if not line:
                continue

            rule_type = self.classify_rule(line)

            rules.append(
                PromptRule(
                    text=line,
                    rule_type=rule_type
                )
            )

        return rules
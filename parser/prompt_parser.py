from .prompt_schema import PromptRule


class PromptParser:

    def classify_rule(self, line: str):

        l = line.lower()

        if "you are" in l or "act as" in l:
            return "role"

        if l.startswith("always"):
            return "instruction"

        if l.startswith("never") or "do not" in l:
            return "constraint"

        if l.startswith("if") or l.startswith("when"):
            return "condition"

        if "example" in l:
            return "example"

        return "general"

    def parse(self, prompt: str):

        rules = []
        lines = prompt.split("\n")

        rule_id = 0

        for line in lines:

            line = line.strip()
            if not line:
                continue

            rules.append(
                PromptRule(
                    id=rule_id,
                    text=line,
                    rule_type=self.classify_rule(line)
                )
            )

            rule_id += 1

        return rules
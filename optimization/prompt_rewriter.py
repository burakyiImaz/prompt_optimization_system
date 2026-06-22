class PromptRewriter:

    def remove_duplicates(self, rules):

        unique_rules = []
        seen = set()

        for rule in rules:

            normalized = rule.text.lower()

            if normalized not in seen:
                seen.add(normalized)
                unique_rules.append(rule)

        return unique_rules

    def rewrite(self, rules, conflicts):

        optimized_rules = self.remove_duplicates(
            rules
        )

        conflict_ids = set()

        for conflict in conflicts:
            conflict_ids.add(
                conflict["rule_2"]
            )

        final_rules = []

        for rule in optimized_rules:

            if rule.id not in conflict_ids:
                final_rules.append(rule)

        return final_rules

    def build_prompt(self, rules):

        prompt = ""

        for rule in rules:
            prompt += rule.text + "\n"

        return prompt
from itertools import combinations


class ConflictResolver:

    CONFLICT_MAP = {
        "detailed": ["concise", "short", "brief"],
        "technical": ["simple", "beginner-friendly"],
        "verbose": ["short", "brief"],
        "long": ["short"],
        "step-by-step": ["concise"]
    }

    def check_conflict(self, text1: str, text2: str):

        text1 = text1.lower()
        text2 = text2.lower()

        for word, conflicts in self.CONFLICT_MAP.items():

            if word in text1:
                for conflict_word in conflicts:
                    if conflict_word in text2:
                        return True

            if word in text2:
                for conflict_word in conflicts:
                    if conflict_word in text1:
                        return True

        return False

    def detect_conflicts(self, rules):

        conflicts = []

        for rule1, rule2 in combinations(rules, 2):

            if self.check_conflict(
                rule1.text,
                rule2.text
            ):
                conflicts.append(
                    {
                        "rule_1": rule1.id,
                        "rule_2": rule2.id,
                        "severity": 1.0
                    }
                )

        return conflicts
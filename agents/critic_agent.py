class CriticAgent:

    def evaluate(self, original: str, optimized: str):

        original_lower = original.lower()
        optimized_lower = optimized.lower()

        intent_overlap = self._overlap(original_lower, optimized_lower)

        loss_of_constraints = self._check_missing_constraints(original_lower, optimized_lower)

        score = (intent_overlap * 0.7) - (loss_of_constraints * 0.3)

        return {
            "intent_score": intent_overlap,
            "constraint_loss": loss_of_constraints,
            "critic_score": score,
            "verdict": "good" if score > 0.6 else "bad"
        }

    def _overlap(self, a, b):
        a_set = set(a.split())
        b_set = set(b.split())
        return len(a_set & b_set) / len(a_set) if a_set else 0

    def _check_missing_constraints(self, original, optimized):

        keywords = ["never", "always", "do not", "must", "ensure"]

        missing = 0

        for k in keywords:
            if k in original and k not in optimized:
                missing += 1

        return missing / len(keywords)
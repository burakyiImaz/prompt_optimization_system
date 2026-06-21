class PromptCompressor:

    REPLACEMENTS = {
        "always provide": "provide",
        "please make sure to": "",
        "it is important to": "",
        "that are easy to understand": "clear",
        "step by step": "step-by-step",
        "in a detailed manner": "in detail",
        "make sure that": "ensure"
    }

    def compress_text(self, text):

        compressed = text

        for old, new in self.REPLACEMENTS.items():
            compressed = compressed.replace(
                old,
                new
            )

        compressed = " ".join(
            compressed.split()
        )

        return compressed

    def compress_rules(self, rules):

        compressed_rules = []

        for rule in rules:

            rule.text = self.compress_text(
                rule.text
            )

            compressed_rules.append(
                rule
            )

        return compressed_rules
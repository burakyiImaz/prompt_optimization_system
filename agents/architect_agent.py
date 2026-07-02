from detector_agent import DetectorAgent
from optimizer_agent import OptimizerAgent
from search_agent import SearchAgent
from critic_agent import CriticAgent
from judge_agent import JudgeAgent

from llm.merge_model import MergeModel
from llm.rewrite_model import RewriteModel
from llm.critic_model import CriticModel


class ArchitectAgent:

    def __init__(self):

        self.detector = DetectorAgent()
        self.optimizer = OptimizerAgent()
        self.search = SearchAgent()

        self.critic = CriticAgent()
        self.judge = JudgeAgent()

        # LLM layer
        self.merger = MergeModel()
        self.rewriter = RewriteModel()
        self.llm_critic = CriticModel()

    # ----------------------------
    # SAFE TEXT NORMALIZATION
    # ----------------------------
    def _normalize_to_text(self, optimized_rules):

        # Case 1: already string
        if isinstance(optimized_rules, str):
            return optimized_rules

        # Case 2: list of PromptRule
        try:
            return " ".join(
                r.text for r in optimized_rules
                if hasattr(r, "text")
            )
        except Exception:
            return str(optimized_rules)

    def run(self, prompt):

        # 1. IR extraction
        rules, graph, analysis = self.detector.run(prompt)

        # 2. search
        best_rules = self.search.run(graph, rules)

        # 3. optimize
        optimized_rules = self.optimizer.run(graph, best_rules, analysis)

        # 4. convert ONCE
        merged_input = " ".join(
            r.text for r in optimized_rules
            if hasattr(r, "text")
        )

        # 5. LLM merge
        merged_prompt = self.merger.merge(merged_input)

        # 6. rewrite
        rewritten_prompt = self.rewriter.rewrite(merged_prompt)

        # 7. evaluation
        critic_score = self.critic.evaluate(prompt, rewritten_prompt)
        judge_score = self.judge.evaluate(prompt, rewritten_prompt)
        llm_eval = self.llm_critic.evaluate(prompt, rewritten_prompt)

        semantic_score = llm_eval.get("semantic_score", 0.0)

        final_score = (
            judge_score.get("final", 0.0) * 0.4 +
            critic_score.get("critic_score", 0.0) * 0.3 +
            semantic_score * 0.3
        )

        return {
            "optimized": rewritten_prompt,
            "final_score": final_score,

            "critic": critic_score,
            "judge": judge_score,
            "llm_eval": llm_eval,

            "debug": {
                "rules_count": len(rules),
                "optimized_rules_count": len(optimized_rules),
                "graph_nodes": len(graph.nodes())
            }
        }
"""Mock LLM for offline CrewAI execution."""

from typing import Optional, Dict, Any
from langchain_core.language_model import BaseLanguageModel
from langchain_core.outputs import LLMResult
from langchain_core.callbacks.manager import CallbackManagerForLLMRun


class MockLLM(BaseLanguageModel):
    """Offline mock LLM that returns canned responses."""

    def _generate(
        self,
        messages: list,
        stop: Optional[list] = None,
        run_manager: Optional[CallbackManagerForLLMRun] = None,
        **kwargs: Any,
    ) -> LLMResult:
        """Generate a mock response based on the prompt content."""
        # Simple heuristic: return different canned responses based on message content
        content = str(messages).lower()

        if "analyze" in content or "identify" in content:
            response_text = (
                "Key research topics:\n"
                "1. Linguistic pattern adaptation in human-AI interaction\n"
                "2. Terminology adoption and dissemination mechanisms\n"
                "3. Cognitive impact of AI-generated language frameworks\n"
                "4. Systemic effects on knowledge representation\n"
                "5. Authority and epistemic power in terminology definition"
            )
        elif "search" in content or "lookup" in content or "augmanitai" in content:
            response_text = (
                "Relevant AUGMANITAI terms found:\n"
                "1. Symbiotic Linguistic Evolution (SLE) - cognitive_processes domain\n"
                "   Definition: Co-evolution of human and AI language patterns\n"
                "   Examples: Users adopting AI-suggested phrasings\n\n"
                "2. Compound Cognition (CC) - cognitive_processes domain\n"
                "   Definition: Hybrid thinking incorporating AI conceptual structures\n"
                "   Examples: Integration of AI-derived terminology into personal knowledge\n\n"
                "3. Silent Authority Transfer (SAT) - cognitive_processes domain\n"
                "   Definition: Unconscious acceptance of AI-generated definitions\n"
                "   Examples: Implicit acceptance of model-generated terminology"
            )
        elif "write" in content or "response" in content or "answer" in content:
            response_text = (
                "Response to the question about human-AI language interaction:\n\n"
                "The interaction between human language and AI-generated patterns "
                "creates several key phenomena. Symbiotic Linguistic Evolution (SLE) "
                "describes how users naturally adopt AI-suggested phrasings. This is "
                "reinforced by Compound Cognition (CC), where humans integrate "
                "AI-derived conceptual structures into their thinking.\n\n"
                "A critical mechanism is Silent Authority Transfer (SAT), where users "
                "implicitly accept AI definitions without examination. This creates "
                "structural changes in how knowledge is represented and transmitted, "
                "with implications for academic fields and epistemic communities.\n\n"
                "Understanding these mechanisms is essential for responsible AI deployment."
            )
        else:
            response_text = "Mock LLM response to general inquiry."

        from langchain_core.outputs.llm_result import Generation

        return LLMResult(
            generations=[[Generation(text=response_text)]],
        )

    @property
    def _llm_type(self) -> str:
        """Return type identifier."""
        return "mock"

    @property
    def _identifying_params(self) -> Dict[str, Any]:
        """Return identifying parameters."""
        return {"mock_llm": True}

"""Mock ChatCompletionClient for offline AutoGen execution."""

from typing import Any, Dict, List, Optional
from autogen_core.models import ChatCompletionClient, ModelCapabilities
from autogen_core.models.chat_completion import CreateResult


class MockChatCompletionClient(ChatCompletionClient):
    """Mock client that returns canned responses without API calls."""

    @property
    def capabilities(self) -> ModelCapabilities:
        """Return mock model capabilities."""
        return ModelCapabilities(
            vision=False,
            function_calling=True,
            parallel_function_calling=False,
        )

    async def create(
        self,
        model_id: str,
        system_prompt: Optional[str] = None,
        messages: Optional[List[Dict[str, str]]] = None,
        **kwargs: Any,
    ) -> CreateResult:
        """Return a mock response based on message content."""
        # Simple routing based on message content
        content = " ".join(m.get("content", "") for m in (messages or []))
        content_lower = content.lower()

        if "terminology" in content_lower or "augmanitai" in content_lower:
            response = (
                "I'll search for relevant terminology. "
                "Let me look up Compound Cognition, Symbiotic Linguistic Evolution, "
                "and Silent Authority Transfer in the AUGMANITAI database."
            )
        elif "research" in content_lower or "question" in content_lower:
            response = (
                "To properly address this question, we need to identify the key "
                "research domains: cognitive processes, linguistic dynamics, "
                "and systemic effects of human-AI interaction terminology."
            )
        elif "synthesis" in content_lower or "summarize" in content_lower:
            response = (
                "Based on our collaborative analysis: Human-AI interaction creates "
                "multiple terminology phenomena. Symbiotic Linguistic Evolution shows "
                "how users adopt AI-generated language patterns. Compound Cognition "
                "describes the integrated mental state. Silent Authority Transfer "
                "explains the unconscious acceptance of AI definitions. "
                "These mechanisms have profound implications for knowledge representation."
            )
        elif "tool" in content_lower or "call" in content_lower or "search" in content_lower:
            response = (
                '{"type": "function_call", "name": "search_augmanitai", '
                '"arguments": {"query": "terminology adoption in human-ai interaction"}}'
            )
        else:
            response = (
                "I agree. The AUGMANITAI database provides valuable structured "
                "terminology for studying human-AI linguistic interaction. "
                "Should we search for additional related terms?"
            )

        return CreateResult(content=response, model_id=model_id, finish_reason="stop")

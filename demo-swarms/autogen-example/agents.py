"""AutoGen AssistantAgent definitions for AUGMANITAI workflow."""

from autogen_agentchat.agents import AssistantAgent
from autogen_core.models import ChatCompletionClient


def create_query_analyzer(client: ChatCompletionClient) -> AssistantAgent:
    """Create agent that analyzes queries and identifies key concepts."""
    return AssistantAgent(
        name="Query Analyzer",
        model_client=client,
        system_message=(
            "You are a research analyst specializing in human-AI interaction terminology. "
            "Your role is to analyze user questions, identify key research concepts, "
            "and determine which AUGMANITAI domains are most relevant. "
            "Be precise and break down complex questions into constituent concepts."
        ),
    )


def create_terminology_expert(client: ChatCompletionClient) -> AssistantAgent:
    """Create agent that looks up and explains terminology."""
    return AssistantAgent(
        name="Terminology Expert",
        model_client=client,
        system_message=(
            "You are a terminologist with deep knowledge of the AUGMANITAI database. "
            "Your role is to search for and retrieve precise definitions of specialized terms, "
            "explain their meanings, provide examples, and identify relationships between concepts. "
            "Always cite the domain and abbreviation when presenting terminology."
        ),
    )


def create_synthesis_officer(client: ChatCompletionClient) -> AssistantAgent:
    """Create agent that synthesizes information into coherent responses."""
    return AssistantAgent(
        name="Synthesis Officer",
        model_client=client,
        system_message=(
            "You are a skilled communicator responsible for synthesizing complex "
            "terminology research into clear, accessible responses. "
            "Your role is to integrate findings from the team, organize information hierarchically, "
            "provide concrete examples, and ensure the response directly addresses the original question."
        ),
    )

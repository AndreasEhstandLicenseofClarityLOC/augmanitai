"""CrewAI Agent definitions for AUGMANITAI workflow."""

from crewai import Agent
from .mock_llm import MockLLM
from .tools import AugmanitaiTool


def create_research_agent(tools: list) -> Agent:
    """Create the Research Agent that identifies relevant topics."""
    return Agent(
        role="Research Topic Specialist",
        goal=(
            "Identify key research topics and concepts related to the user's "
            "question about human-AI interaction terminology"
        ),
        backstory=(
            "You are an expert in research methodology and topic analysis. "
            "You excel at breaking down complex questions into constituent concepts "
            "and identifying the key areas that need investigation."
        ),
        tools=tools,
        llm=MockLLM(),
        verbose=False,
    )


def create_terminology_agent(tools: list) -> Agent:
    """Create the Terminology Agent that looks up AUGMANITAI definitions."""
    return Agent(
        role="Terminology Researcher",
        goal=(
            "Search the AUGMANITAI database to find precise definitions and "
            "examples of key terminology related to human-AI linguistic interaction"
        ),
        backstory=(
            "You are a terminologist with deep expertise in academic databases. "
            "You know how to search, retrieve, and interpret specialized terminology "
            "from structured knowledge bases."
        ),
        tools=tools,
        llm=MockLLM(),
        verbose=False,
    )


def create_writer_agent(tools: list) -> Agent:
    """Create the Writer Agent that composes the final response."""
    return Agent(
        role="Academic Writer",
        goal=(
            "Synthesize terminology research findings into a clear, well-structured "
            "response that answers the user's original question"
        ),
        backstory=(
            "You are a skilled academic writer with experience in synthesizing "
            "complex terminology into accessible explanations. You can organize "
            "information hierarchically and provide clear definitions with examples."
        ),
        tools=tools,
        llm=MockLLM(),
        verbose=False,
    )

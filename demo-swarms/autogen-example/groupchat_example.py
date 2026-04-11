"""
AutoGen RoundRobinGroupChat example with AUGMANITAI terminology lookup.

Demonstrates three agents collaborating in a round-robin group chat to
research and explain AUGMANITAI terminology.
"""

import asyncio
from typing import List, Dict, Any
from autogen_agentchat.teams import RoundRobinGroupChat
from autogen_agentchat.agents import AssistantAgent
from .agents import create_query_analyzer, create_terminology_expert, create_synthesis_officer
from .mock_client import MockChatCompletionClient
from .tools import AugmanitaiToolset


async def run_augmanitai_groupchat(user_question: str) -> str:
    """
    Run a RoundRobinGroupChat to answer a question using AUGMANITAI.

    Args:
        user_question: The research question to answer

    Returns:
        Final response from the group chat
    """
    # Create mock client for offline operation
    client = MockChatCompletionClient()

    # Create agents
    analyzer = create_query_analyzer(client)
    expert = create_terminology_expert(client)
    synthesizer = create_synthesis_officer(client)

    # Create the group chat with 3 agents
    # RoundRobinGroupChat cycles through agents until termination condition
    group_chat = RoundRobinGroupChat(
        agents=[analyzer, expert, synthesizer],
        max_turns=6,  # Allow up to 6 turns (2 per agent)
    )

    # Initial message to start the conversation
    initial_message = f"""
Research Question: {user_question}

Please collaborate to answer this question by:
1. Query Analyzer: Break down the question into key concepts
2. Terminology Expert: Look up relevant AUGMANITAI terminology
3. Synthesis Officer: Compile a comprehensive response
    """.strip()

    # Run the group chat
    result = await group_chat.run(task=initial_message)

    # Extract and return the final response
    if result.messages:
        # Return the last message from the synthesis officer
        for message in reversed(result.messages):
            if "Synthesis Officer" in str(message):
                return str(message)

    return str(result)


def run_example_sync(user_question: str) -> str:
    """
    Synchronous wrapper for running the async group chat.

    Args:
        user_question: The research question

    Returns:
        Response from the group chat
    """
    # Use asyncio to run the async function
    try:
        return asyncio.run(run_augmanitai_groupchat(user_question))
    except RuntimeError:
        # Handle case where event loop already exists
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        try:
            return loop.run_until_complete(run_augmanitai_groupchat(user_question))
        finally:
            loop.close()


if __name__ == "__main__":
    # Example usage
    question = (
        "How do mechanisms of terminology adoption affect knowledge representation "
        "in academic fields?"
    )
    response = run_example_sync(question)
    print(response)

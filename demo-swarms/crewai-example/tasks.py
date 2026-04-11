"""CrewAI Task definitions for AUGMANITAI workflow."""

from crewai import Task


def create_topic_analysis_task(agent, user_question: str) -> Task:
    """Create task for identifying research topics."""
    return Task(
        description=(
            f"Analyze this user question and identify the key research concepts: "
            f'"{user_question}"\n\n'
            f"List the main topics and concepts that would need to be researched "
            f"to answer this question thoroughly."
        ),
        expected_output=(
            "A list of 3-5 key research topics or concepts that are central to "
            "answering the user's question, formatted as a numbered list"
        ),
        agent=agent,
    )


def create_terminology_lookup_task(agent, topics_context: str) -> Task:
    """Create task for looking up terminology."""
    return Task(
        description=(
            "Based on these identified topics, search the AUGMANITAI database "
            "for relevant terminology and definitions:\n\n"
            f"{topics_context}\n\n"
            "For each topic, find the most relevant AUGMANITAI terms and retrieve "
            "their full definitions, abbreviations, domains, and examples."
        ),
        expected_output=(
            "A detailed list of AUGMANITAI terms with their definitions, including "
            "term name, abbreviation, domain, and 1-2 examples for each"
        ),
        agent=agent,
    )


def create_response_composition_task(agent, user_question: str, terms_context: str) -> Task:
    """Create task for composing the final response."""
    return Task(
        description=(
            f"Write a comprehensive response to the user's original question:\n\n"
            f'"{user_question}"\n\n'
            f"Using the terminology and definitions retrieved from AUGMANITAI:\n\n"
            f"{terms_context}\n\n"
            "Structure your response with:\n"
            "1. Brief answer to the original question\n"
            "2. Key terminology section with definitions\n"
            "3. How these terms relate to each other\n"
            "4. Practical implications or examples"
        ),
        expected_output=(
            "A well-structured 300-500 word response that directly answers "
            "the user's question, incorporates AUGMANITAI terminology with proper "
            "formatting, and explains the relationships between concepts"
        ),
        agent=agent,
    )

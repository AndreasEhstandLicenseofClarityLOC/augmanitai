"""
CrewAI multi-agent example for AUGMANITAI terminology research.

Demonstrates a 3-agent crew working sequentially to:
1. Analyze a research question and identify key topics
2. Look up related terminology in AUGMANITAI
3. Compose a structured response
"""

from crewai import Crew, Process
from .agents import (
    create_research_agent,
    create_terminology_agent,
    create_writer_agent,
)
from .tasks import (
    create_topic_analysis_task,
    create_terminology_lookup_task,
    create_response_composition_task,
)
from .tools import AugmanitaiTool


def run_augmanitai_crew(user_question: str) -> str:
    """
    Run the AUGMANITAI crew on a research question.

    Args:
        user_question: The user's research question

    Returns:
        Final composed response with terminology
    """
    # Initialize shared tools
    augmanitai_tool = AugmanitaiTool()
    tools = [augmanitai_tool.search_terms, augmanitai_tool.get_domain_terms]

    # Create agents
    research_agent = create_research_agent(tools)
    terminology_agent = create_terminology_agent(tools)
    writer_agent = create_writer_agent(tools)

    # Create tasks
    topic_task = create_topic_analysis_task(research_agent, user_question)

    terminology_task = create_terminology_lookup_task(
        terminology_agent,
        "Based on the research topics identified, search AUGMANITAI",
    )

    response_task = create_response_composition_task(
        writer_agent,
        user_question,
        "Using the terminology retrieved from AUGMANITAI",
    )

    # Create crew with sequential processing
    crew = Crew(
        agents=[research_agent, terminology_agent, writer_agent],
        tasks=[topic_task, terminology_task, response_task],
        process=Process.sequential,
        verbose=False,
    )

    # Execute crew
    result = crew.kickoff()

    return str(result)


if __name__ == "__main__":
    # Example usage
    question = (
        "How do AI systems influence the way humans adopt and use new terminology?"
    )
    response = run_augmanitai_crew(question)
    print(response)

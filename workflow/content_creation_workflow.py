from typing import TypedDict, Annotated, List
from langgraph.graph import StateGraph, START, END
from data.schema.chapter import Chapter
from agents.writer import ChapterGenerator
from agents.store import StorySaver
from utils.logger import logger

# Graph state
class State(TypedDict):
    story: str  # Full story
    chapters: list[Chapter]  # List of Chapters
    task_list: list[str]  # Order of tasks to be performed
    days: int  # Total number of days for the story 
    current_day: int  # Current day in the story
    continue_story: str  # Flag to continue the story


class Workflow:
    def __init__(self, llm, task_list: List[str], days: int):
        """
        Initializes the Workflow with the LLM model and instructions.

        Args:
            llm: The language model used for structured output.
        """
        self.llm = llm
        self.chapter_writer_llm = llm.with_structured_output(Chapter)  # Augment LLM with Team schema
        
        self.chapter_writer_agent = ChapterGenerator(self.chapter_writer_llm)
        self.story_saver_agent = StorySaver("story.txt")

        # Initialize the workflow state
        self.state: State = {
            "story": "",
            "chapters": [],
            "task_list": task_list,
            "days": days,
            "current_day": 1,
            "continue_story": "YES"
        }

        self.orchestrator_worker_builder = StateGraph(State)

    def chapter_writer(self, state: State):
        """Wrapper function to call the chapter writer agent."""
        recap = self.state["chapters"][-1]["chapter"].story if self.state["current_day"] > 1 else ""
        result = self.chapter_writer_agent.generate_chapter(self.state["task_list"][self.state["current_day"] - 1], self.state["days"], self.state["current_day"], recap)
        self.state["story"] += result["chapter"].title + "\n" + result["chapter"].story + "\n\n"
        self.state["chapters"].append(result)
        self.state.update({"current_day": self.state["current_day"] + 1})
        return result
    
    def story_saver(self, state: State):
        """Wrapper function to save the story agent."""
        self.story_saver_agent.store_story(self.state["story"])
        return
    


    # Conditional edge function to route back to joke generator or end based upon feedback from the evaluator
    def continue_generation(self, state: State):
        """Route back to story generator or continue based upon feedback from the evaluator"""

        if self.state.get("current_day") <= self.state.get("days"):
            self.state["continue_story"] = "YES"
            return "YES"
        self.state["continue_story"] = "NO"
        return "NO"

    def build_workflow(self):
        """
        Constructs the workflow by adding nodes and edges.
        """
        logger.info("Building workflow...")
        self.orchestrator_worker_builder.add_node("chapter_writer", self.chapter_writer)
        self.orchestrator_worker_builder.add_node("story_saver", self.story_saver)

        # Add edges to connect nodes
        self.orchestrator_worker_builder.add_edge(START, "chapter_writer")
        # self.orchestrator_worker_builder.add_edge("team_generator", "story_generator")
        # self.orchestrator_worker_builder.add_edge("story_generator", "story_evaluator")
        self.orchestrator_worker_builder.add_conditional_edges(
            "chapter_writer", self.continue_generation, {
                "NO": "story_saver",
                "YES": "chapter_writer"
            }
        )
        self.orchestrator_worker_builder.add_edge("story_saver", END)

    def compile_workflow(self):
        """
        Compiles the workflow for execution.
        """
        logger.info("Compiling workflow...")
        self.orchestrator_worker = self.orchestrator_worker_builder.compile()

    def invoke_workflow(self, task_list: List[str], days: int):
        """
        Runs the workflow with the initialized mission.

        Returns:
            dict: The final state after execution.
        """
        logger.info(f"Invoking workflow for tasks: [yellow]{task_list}[/yellow]")
        self.state["task_list"] = task_list
        self.state["days"] = days
        return self.orchestrator_worker.invoke({"task_list": self.state["task_list"], "days": self.state["days"]})

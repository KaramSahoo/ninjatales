from langchain.schema import SystemMessage, HumanMessage
from prompts.story_prompt import STORY_SYSTEM_PROMPT
from utils.logger import logger

class ChapterGenerator:
    def __init__(self, llm):
        """Initialize the chapter writer agent."""
        self.llm = llm

    def generate_chapter(self, task: str, days: int, currDay: int, recap: str) -> dict:
        """Generates a chapter based on the task."""
        logger.info(f"Generating chapter for task {currDay}/{days}: [yellow]{task}[/yellow]")

        written_chapter = self.llm.invoke([
            SystemMessage(content=STORY_SYSTEM_PROMPT),
            HumanMessage(content=f"Here is the task: {task} and the day: {currDay} out of {days}. Write a chapter for the story based on this task. Recap from previous chapter: {recap}"),
        ])

        logger.success(f"Chapter written: \"{written_chapter.title}\"")

        return {"chapter": written_chapter}

    
from langchain.schema import SystemMessage, HumanMessage
from utils.logger import logger

class StorySaver:
    def __init__(self, path: str):
        """Initialize the chapter writer agent."""
        self.path = path

    def store_story(self, story: str) -> bool:
        """Stores the story as a txt file."""

        with open(self.path, "w") as f:
            f.write(story)

        logger.success(f"Story saved at {self.path}")

        return True

    
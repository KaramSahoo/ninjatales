from typing import List, TypedDict, Annotated
from enum import Enum
from pydantic import BaseModel, Field # type: ignore
from typing_extensions import Literal

class TaskPerformance(Enum):
    POOR = "poor"
    AVERAGE = "average"
    EXCELLENT = "excellent"

class ChapterData(TypedDict):
    chapter_name: str
    daily_scores: List[int]
    average_score: float
    performance_rating: TaskPerformance
    total_days: int

class Chapter(BaseModel):
    title: str = Field(
        description="Title of the chapter.",
    )
    story: str = Field(
        description="This is the story of the chapter where Ninja performs the particular task.",
    )
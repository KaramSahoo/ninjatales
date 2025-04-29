from dataclasses import dataclass
from typing import List, Optional
import numpy as np

class Story:
    """
    Singleton class to store story data globally
    """
    _instance: Optional['Story'] = None
    
    def __init__(self):
        if Story._instance is not None:
            raise Exception("Story class is a singleton! Use Story.get_instance()")
        self.days: int = 0
        self.task1: str = ""
        self.task2: str = ""
        self.task3: str = ""
        self.task_matrix: List[List[int]] = []
        
    @classmethod
    def get_instance(cls) -> 'Story':
        """Get or create the singleton instance"""
        if cls._instance is None:
            cls._instance = Story()
        return cls._instance
    
    def initialize(self, days: int, task1: str, task2: str, task3: str):
        """Initialize story data with user inputs and generate task matrix"""
        self.days = days
        self.task1 = task1
        self.task2 = task2
        self.task3 = task3
        self.task_matrix = np.random.randint(0, 11, size=(3, days)).tolist()
    
    def __str__(self) -> str:
        """String representation of the story data"""
        return (
            f"Days: {self.days} || Task 1: {self.task1} || Task 2: {self.task2} | Task 3: {self.task3}\n"
            f"Task Matrix:\n{self.task_matrix}"
        )
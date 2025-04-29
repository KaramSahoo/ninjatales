from typing import Optional
from langchain.chat_models import ChatOpenAI
from langchain.schema import SystemMessage
import os
from dotenv import load_dotenv
from prompts.story_prompt import STORY_SYSTEM_PROMPT

class StoryLLM:
    """
    Singleton class to manage OpenAI LLM instance
    """
    _instance: Optional['StoryLLM'] = None
    _llm: Optional[ChatOpenAI] = None
    _system_message: Optional[SystemMessage] = None
    
    def __init__(self):
        if StoryLLM._instance is not None:
            raise Exception("StoryLLM is a singleton! Use StoryLLM.get_instance()")
        
        # Load environment variables
        load_dotenv('config/.env')
        
        # Initialize OpenAI LLM
        self._llm = ChatOpenAI(
            model_name="gpt-4",
            temperature=0.7,
            api_key=os.getenv('OPENAI_API_KEY')
        )
        
        # Set system message
        self._system_message = SystemMessage(content=STORY_SYSTEM_PROMPT)
    
    @classmethod
    def get_instance(cls) -> 'StoryLLM':
        """Get or create the singleton instance"""
        if cls._instance is None:
            cls._instance = StoryLLM()
        return cls._instance
    
    @property
    def llm(self) -> ChatOpenAI:
        """Get the LLM instance"""
        return self._llm
    
    @property
    def system_message(self) -> SystemMessage:
        """Get the system message"""
        return self._system_message
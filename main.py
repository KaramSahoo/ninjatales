import argparse
from logger.logger import StoryLogger
from utils.input_validator import validate_positive_int
from data.story_data import Story
import sys
from utils.matrix_ops import eda_task_matrix, ninjaTrainingPath
from utils.print import print_task_data
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from workflow.content_creation_workflow import Workflow
load_dotenv()

def get_story_inputs():
    logger = StoryLogger()
    
    # Create argument parser
    parser = argparse.ArgumentParser(
        description='Create a story based on daily tasks',
        formatter_class=argparse.RawTextHelpFormatter
    )
    
    # Add arguments
    parser.add_argument(
        '-d', '--days',
        type=validate_positive_int,
        required=True,
        help='Number of days for the story'
    )
    parser.add_argument(
        '-t1', '--task1',
        type=str,
        required=True,
        help='First task description'
    )
    parser.add_argument(
        '-t2', '--task2',
        type=str,
        required=True,
        help='Second task description'
    )
    parser.add_argument(
        '-t3', '--task3',
        type=str,
        required=True,
        help='Third task description'
    )
    
    try:
        # Parse arguments
        args = parser.parse_args()
        
        # Initialize Story singleton with validated inputs
        story = Story.get_instance()
        story.initialize(args.days, args.task1, args.task2, args.task3)
        
        # Log successful initialization
        logger.info("Data to create an epic lore initialized successfully:")
        logger.info(str(story))
        
        return story
        
    except Exception as e:
        logger.error(f"Error processing inputs: {str(e)}")
        sys.exit(1)

def main():
    logger = StoryLogger()
    try:
        story = get_story_inputs()
        print_task_data(eda_task_matrix(story))
        daily_activities = ninjaTrainingPath(story.days, story.task_matrix)

        task_map = {
            0: story.task1,
            1: story.task2,
            2: story.task3
        }
        
        # Map numeric activities to task names
        mapped_activities = [task_map[task_idx] for task_idx in daily_activities]
        print(f"Mapped activities: {mapped_activities}")

        llm = ChatOpenAI(model="gpt-4o-mini", temperature=0.2)

        workflow = Workflow(llm, mapped_activities, story.days)

        # Build and compile the workflow
        workflow.build_workflow()
        workflow.compile_workflow()

        # Invoke the workflow
        state = workflow.invoke_workflow(task_list=mapped_activities, days=story.days)
        print(state)

        # Future story generation logic will go here
        logger.info("Successfully collected all inputs")
        
    except Exception as e:
        logger.error(f"An unexpected error occurred: {str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    main()
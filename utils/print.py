from typing import List
import colorama
from colorama import Fore, Style, Back
from data.schema.chapter import ChapterData, TaskPerformance
from logger.logger import StoryLogger

# Initialize colorama for Windows support
colorama.init()

logger = StoryLogger()

def print_separator(char: str = "=", length: int = 50) -> None:
    """Print a separator line with specified character and length"""
    print(f"{Fore.BLUE}{char * length}{Style.RESET_ALL}")

def print_header(text: str) -> None:
    """Print a formatted header text"""
    print_separator()
    print(f"{Fore.CYAN}{Style.BRIGHT}{text.center(50)}{Style.RESET_ALL}")
    print_separator()

def get_performance_color(performance: TaskPerformance) -> str:
    """Get the appropriate color for a performance rating"""
    colors = {
        TaskPerformance.POOR: Fore.RED,
        TaskPerformance.AVERAGE: Fore.YELLOW,
        TaskPerformance.EXCELLENT: Fore.GREEN
    }
    return colors.get(performance, Fore.WHITE)

def print_task_data(task_data_list: List[ChapterData]) -> None:
    """
    Print formatted task performance data
    
    Args:
        task_data_list (List[ChapterData]): List of task data to display
    """
    print_header("Task Performance Analysis")
    
    for task in task_data_list:
        # Get color based on performance
        perf_color = get_performance_color(task['performance_rating'])
        
        # Print task name and basic stats
        print(f"{Fore.CYAN}Task:{Style.RESET_ALL} {task['chapter_name']}")
        print(f"{Fore.CYAN}Average Score:{Style.RESET_ALL} {perf_color}{task['average_score']:.2f}{Style.RESET_ALL}")
        print(f"{Fore.CYAN}Performance:{Style.RESET_ALL} {perf_color}{task['performance_rating'].value}{Style.RESET_ALL}")
        
        # Print daily scores
        print(f"{Fore.CYAN}Daily Scores:{Style.RESET_ALL}")
        for day, score in enumerate(task['daily_scores'], 1):
            if score >= 7:
                score_color = Fore.GREEN
            elif score >= 4:
                score_color = Fore.YELLOW
            else:
                score_color = Fore.RED
                
            print(f"Day {day}: {score_color}{score}{Style.RESET_ALL}", end="  ")
        print("")  # New line after daily scores
        
        print_separator("-", 30)

def print_error(message: str) -> None:
    """Print an error message"""
    logger.error(message)

def print_success(message: str) -> None:
    """Print a success message"""
    logger.info(message)

def print_warning(message: str) -> None:
    """Print a warning message"""
    logger.warning(message)

def print_info(text: str, color: str = Fore.WHITE) -> None:
    """Print informational text with optional color"""
    print(f"{color}{text}{Style.RESET_ALL}")
import numpy as np
from typing import List
from data.story_data import Story
from data.schema.chapter import ChapterData, TaskPerformance

def eda_task_matrix(story_data: Story) -> List[ChapterData]:
    """
    Process the task matrix and return structured data for each task
    
    Args:
        story_data (StoryData): Story data containing task matrix and task names
        
    Returns:
        List[TaskData]: List of structured task data for each task
    """
    matrix = np.array(story_data.task_matrix)
    tasks = [story_data.task1, story_data.task2, story_data.task3]
    result = []
    
    for task_idx, task_name in enumerate(tasks):
        daily_scores = matrix[task_idx].tolist()
        avg_score = float(np.mean(daily_scores))
        
        # Determine performance rating based on average score
        if avg_score < 4:
            performance = TaskPerformance.POOR
        elif avg_score < 7:
            performance = TaskPerformance.AVERAGE
        else:
            performance = TaskPerformance.EXCELLENT
            
        task_data: ChapterData = {
            "chapter_name": task_name,
            "daily_scores": daily_scores,
            "average_score": round(avg_score, 2),
            "performance_rating": performance,
            "total_days": len(daily_scores)
        }
        
        result.append(task_data)
    
    return result

def ninjaTraining(n, points):
    points = ninjaTrainingPath(n, points)
    # Initialize a list 'prev' to store the maximum points for each possible last activity on the previous day.
    prev = [0] * 4

    # Initialize 'prev' with the maximum points for the first day's activities.
    prev[0] = max(points[0][1], points[0][2])
    prev[1] = max(points[0][0], points[0][2])
    prev[2] = max(points[0][0], points[0][1])
    prev[3] = max(points[0][0], max(points[0][1], points[0][2]))
    print(f"Selected activity for day 1: {prev}")
    # Loop through the days starting from the second day.
    for day in range(1, n):
        # Initialize a temporary list 'temp' to store the maximum points for each possible last activity on the current day.
        temp = [0] * 4

        for last in range(4):
            # Initialize 'temp' for the current last activity.
            temp[last] = 0

            for task in range(3):
                if task != last:
                    # Calculate the total points for the current day's activity and the previous day's maximum points.
                    activity = points[day][task] + prev[task]
                    # Update 'temp' with the maximum points for the current last activity.
                    temp[last] = max(temp[last], activity)

        # Update 'prev' with 'temp' for the next iteration.
        print(f"Selected activity for day {day+1}: {temp}")
        prev = temp

    # Return the maximum points achievable after the last day with any activity.
    return prev[3]

def ninjaTrainingPath(n, points):
    points = transpose_points(n, points)
    # Step 1: DP table
    dp = [[0 for _ in range(4)] for _ in range(n)]

    # Base case (day 0)
    for last in range(4):
        dp[0][last] = max(points[0][i] for i in range(3) if i != last)
    
    # Build DP
    for day in range(1, n):
        for last in range(4):
            dp[day][last] = 0
            for task in range(3):
                if task != last:
                    val = points[day][task] + dp[day-1][task]
                    dp[day][last] = max(dp[day][last], val)
    
    # Step 2: Path reconstruction
    ans = []
    last_task = 3  # no restriction on last task
    for day in reversed(range(n)):
        best_task = -1
        best_value = -1
        
        for task in range(3):
            if task != last_task:
                val = points[day][task]
                if day > 0:
                    val += dp[day-1][task]
                if val > best_value:
                    best_value = val
                    best_task = task
        
        ans.append(best_task)
        print(f"Selected activity for day {day}: -> Task {best_task}")
        last_task = best_task  # update last_task
    
    ans.reverse()  # because we went from last day to first
    return ans

def transpose_points(n, points):
    pmat = [[0] * 3 for _ in range(n)]
    for i in range(n):
        for j in range(3):
            pmat[i][j] = points[j][i]

    
    return pmat
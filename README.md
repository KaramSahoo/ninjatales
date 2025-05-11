# 🥷 Ninja Story Builder 📚  
*Making Leetcode Dynamic Programming... Literary and Fun!*

---

## 🚀 Overview


**Ninja Story Builder** is a creative fusion of **Dynamic Programming** and **Multi-Agent AI Workflows**.

It solves the classic **Ninja Training** problem — where for `N` days and 3 possible tasks per day, the goal is to **maximize total points** without repeating tasks on consecutive days.

But here’s the twist:  
Each task decision for a day becomes a **chapter** in an evolving story, crafted by **LLM-powered agents**!  
The result? An automatically generated, task-driven, multi-day **adventure story**.

---

## 🎯 Why This Project?

Leetcode is great for technical prep — but let’s be honest, it can get repetitive.  
This project transforms **algorithm practice** into a **playground for creativity**, using:

- 📈 **Dynamic Programming** for task optimization  
- 🧠 **LLMs** for content generation  
- 🔁 **Multi-Agent Systems** for coherent storytelling  
- 🔧 **LangGraph** for graph-based AI workflows

---

## 🧠 Core Concepts

### 1. **Ninja Training Problem (DP)**

> For each of `N` days, choose a task from `{task1, task2, task3}` such that the same task is not performed on two consecutive days. Maximize the sum of points.

Implemented using **Bottom-Up Tabulation** with memoization to compute the optimal schedule efficiently.

---

### 2. **Multi-Agent Chapter Generation**

- For every day `i`, an **Agent**:
  - Takes the task chosen for day `i`
  - Receives the chapter from day `i-1` (if any)
  - Generates a `Chapter` using structured inputs:
    ```python
    class Chapter(BaseModel):
        title: str
        content: str
        day_number: int
    ```
  - Adds it to the ongoing storybook.


---

## 🧪 Tech Stack

| Component        | Tool / Framework       |
|------------------|------------------------|
| Dynamic Programming | Custom DP Optimizer (Python) |
| Agent Orchestration | [LangGraph](https://github.com/langchain-ai/langgraph) |
| Data Validation  | Pydantic |
| LLMs             | OpenAI API |

---

## 🛠️ Installation

### 1. Clone the Repository
```bash
git clone https://github.com/your-username/ninja-story-builder.git
cd ninja-story-builder

### 2. Set Up Environment Variables
Create a `.env` file in the root directory and add your OpenAI API key:
```
OPENAI_API_KEY=your_openai_api_key
```

### 3. Install Dependencies
Run the following command to install the required dependencies:
```bash
pip install -r requirements.txt
```

## Running the Project
To run the project, use the following command:
```bash
python main.py -d <number_of_days> -t1 "<task1_description>" -t2 "<task2_description>" -t3 "<task3_description>"
```

### Example Command
```bash
python main.py -d 7 -t1 "Climb the mountain" -t2 "Defend the village" -t3 "Search for the ancient scroll"
```

## Output
The program will generate a story based on the tasks and save it to `story.txt`.

## Project Structure
- `main.py`: Entry point of the application.
- `agents/`: Contains modules for story generation.
- `config/`: Configuration files.
- `data/`: Data models and schemas.
- `llm/`: Logic for interacting with the language model.
- `logger/`: Logging utilities.
- `prompts/`: Prompt templates for the language model.
- `tools/`: Additional tools and utilities.
- `utils/`: Helper functions and utilities.
- `workflow/`: Workflow management for content creation.

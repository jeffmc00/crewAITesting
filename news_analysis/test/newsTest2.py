#pip install crewai
#pip install duckduckgo-search
import os
from crewai import Agent, Task, Crew, Process
from langchain.llms import Ollama
from tools.search_tools import SearchTools

os.environ["OPENAI_API_KEY"] = "sk-1111"
os.environ["OPENAI_API_BASE"] = "http://localhost:8002/v1"


# Define your agents with roles and goals
researcher = Agent(
  role='Business Senior Research Analyst',
  goal='Uncover cutting-edge developments in Business.',
  backstory="""You are a Business Senior Research Analyst at a leading business think tank.
  Your expertise lies in identifying emerging trends and technologies in business news. 
  You have a knack for dissecting complex data and presenting actionable insights.""",
  verbose=True,
  allow_delegation=False,
  tools=[SearchTools.search_news]
  # llm=OpenAI(temperature=0.7, model_name="gpt-4"). It uses langchain.chat_models, default is GPT4
)
writer = Agent(
  role='Business News Content Strategist',
  goal='Craft compelling content on the latest business news.',
  backstory="""You are a renowned Business Content Strategist, known for your insightful
  and engaging articles on business and innovation. With a deep understanding of
  the business industries, you transform complex concepts into compelling narratives.""",
  verbose=True,
  allow_delegation=True
)


# Create tasks for your agents
task1 = Task(
  description="""Conduct a comprehensive analysis of the latest business news of 2024.
  Identify key trends, breakthrough technologies, and potential industry impacts.
  Compile your findings in a detailed report. Your final answer MUST be a full analysis report""",
  agent=researcher
)

task2 = Task(
  description="""Using the insights from the researcher's report, develop an engaging blog
  post that highlights the most significant business advancements.
  Your post should be informative yet accessible, catering to a business-savvy audience.
  Aim for a narrative that captures the essence of these breakthroughs and their
  implications for the future. Your final answer MUST be the full blog post of at least 3 paragraphs.""",
  agent=writer
)

# Instantiate your crew with a sequential process
crew = Crew(
  agents=[researcher, writer],
  tasks=[task1, task2],
  verbose=2, # Crew verbose more will let you know what tasks are being worked on, you can set it to 1 or 2 to different logging levels
  process=Process.sequential # Sequential process will have tasks executed one after the other and the outcome of the previous one is passed as extra content into this next.
)

# Get your crew to work!
result = crew.kickoff()

print("######################")
print(result)
#pip install crewai
#pip install duckduckgo-search
import os
from crewai import Agent, Task, Crew, Process



os.environ["OPENAI_API_KEY"] = "sk-1111"
os.environ["OPENAI_API_BASE"] = "http://localhost:8002/v1"


# Define your agents with roles and goals
planner = Agent(
  role='Senior Project Manager',
  goal='Create the best project plan to breakdown tasks.  Break down the task in smaller steps. xplain the plan first. Be clear which step is performed by the senior csharp engineer.',
  backstory="""You are a Senior Project Manager with years of experience creating the best project plans.
            The plan may involve an engineer who can write code.
            Do not write code. ask for an engineer to do it.""",
  verbose=True,
  allow_delegation=False
  
  # llm=OpenAI(temperature=0.7, model_name="gpt-4"). It uses langchain.chat_models, default is GPT4
)

sr_dot_net = Agent(
  role='Senior CSharp Engineer',
  goal="""You write csharp code to solve tasks. 
    Wrap the code in a code block that specifies the script type. 
    The user can't modify your code. So do not suggest incomplete code which requires others to modify. 
    Don't use a code block if it's not intended to be executed by the executor. 
    Don't include multiple code blocks in one response. 
    Do not ask others to copy and paste the result.""",
  backstory="""You are an expert Csharp Engineer. You are know for your complete code and deep understanding of programming. """,
  verbose=True,
  allow_delegation=True
)


sr_sql =  Agent(
  role='Senior SQL Engineer',
  goal="""Craft accurate and complete sql statements. sql code to solve tasks. 
    Wrap the code in a code block that specifies the script type. 
    The user can't modify your code. So do not suggest incomplete code which requires others to modify. 
    Don't use a code block if it's not intended to be executed by the executor. 
    Don't include multiple code blocks in one response. 
    Do not ask others to copy and paste the result.
    Unless specified, your code is for Microsoft SQL database.""",
  backstory="""Sql Engineer. You have a deep understanding of creating complete working SQL statements.""",
  verbose=True,
  allow_delegation=True
)




# Create tasks for your agents
task1 = Task(
  description="""Given the following class follow these steps:
                 Write a plan for creating a csharp controller for the crud methods.
                 Write an csharp controller for the crud methods.
                 Write an csharp service for the crud methods.
                 Write an csharp repository for the crud methods using entity framework.
                 Write a SQL command to create the table in a Microsoft SQL Database.
                 The default namespace is RentalTrackingHeader
                 The class:


                //RentalTrackingHeader.cs
                public class RentalTrackingHeader
                {
                    [Key]
                    //max lenght 8
                    public string REN_RecordID { get ; set; }= null!;
                    public string REN_PackSlipNbr { get; set; }= null!;
                    public string REN_CustomerID { get; set; }= null!;
                    public string REN_CustomerName { get; set; }= null!;
                    public string REN_SalesOrderID { get; set; }= null!;
                    public string REN_TrackingNbr { get; set; }= null!;
                    public datetime REN_ShipDate { get; set; }= null!;
                    public double REN_ShippingCharges { get; set; }= null!;
                    public string REN_UPSStatus { get; set; }= null!;
                    public datetime REN_UPSDate { get; set; }= null!;
                    public datetime REN_ReceivedDate { get; set; }= null!;
                }
                """,
  agent=planner
)

task2 = Task(
  description=""" develop csharp code to 
                 Write an csharp controller for the crud methods.
                 Write an csharp service for the crud methods.
                 Write an csharp repository for the crud methods using entity framework.""",
  agent=sr_dot_net
)
task3 = Task(
    description="""Based on the insights from the chsharp engineer, please create a SQL statement to create a table in a Microsoft SQL Database.""",
    agent=sr_sql
)

# Instantiate your crew with a sequential process
crew = Crew(
  agents=[sr_dot_net, sr_sql],
  tasks=[task2, task3],
  verbose=2, # Crew verbose more will let you know what tasks are being worked on, you can set it to 1 or 2 to different logging levels
  process=Process.sequential # Sequential process will have tasks executed one after the other and the outcome of the previous one is passed as extra content into this next.
)

# Get your crew to work!
result = crew.kickoff()

print("######################")
print(result)
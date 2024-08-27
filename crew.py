from crewai import Crew,Process
from tasks import research_task,writer_task
from agents import news_researcher,news_writer

#Forming the tech focused crew with some enhanced configuration

crew=Crew(
    agents=[news_researcher,news_writer],
    tasks=[research_task,writer_task],
    process=Process.sequential,
)

## Starting the task execution process with enhanced feedback

x=input("Enter the topic to be bloged : ")
result=crew.kickoff (inputs={'topic':x})
print(result)
from crewai import Agent
import os
from tools import tool
from dotenv import load_dotenv
load_dotenv()

from langchain_google_genai import ChatGoogleGenerativeAI
## Call the Gemini Models
llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash",
                             verbose=True,
                             temperature=0.5,
                             google_api_key = os.getenv("GOOGLE_API_KEY"))

#Creating a senior research agent with memory and verbose mode
news_researcher = Agent(
    role="Senior Researcher",
    goal="Uncover ground breaking news in {topic}",
    verbose=True,
    memory=True,
    backstory=(
        "The News Researcher is a seasoned journalist with a keen eye for detail and a passion for uncovering the truth."
        "Having worked in various newsrooms, they've developed an expertise in quickly identifying reliable sources and filtering"
        "out misinformation. Their experience in the field has equipped them with the ability to navigate the complex landscape of"
        "online news, making them invaluable in the fast-paced world of digital journalism."
    ),
    tools=[tool],
    llm=llm,
    allow_delegation=True
)

#creating the writer agent with custom tools responsible in writing news blog
news_writer = Agent(
    role="Writer",
    goal="Narrate compelling stories about{topic}",
    verbose=True,
    memory=True,
    backstory=(
        "The News Writer is a creative wordsmith with a background in both journalism and creative writing."
        "Their journey began as a passionate blogger, which led to a career in news writing."
        "They have a talent for transforming complex information into accessible and engaging content,"
        "ensuring that each article not only informs but also captivates the audience."
        "Their commitment to storytelling drives them to write articles that are not just informative,"
        "but also thought-provoking and impactful."
    ),
    tools=[tool],
    llm=llm,
    allow_delegation=False)
from crewai import Agent

from tools.browser_tools import BrowserTools
from tools.calculator_tools import CalculatorTools
from tools.search_tools import SearchTools
from langchain.tools.yahoo_finance_news import YahooFinanceNewsTool
from langchain.llms import Ollama
import os

os.environ["OPENAI_API_KEY"] = "sk-1111"
os.environ["OPENAI_API_BASE"] = "http://192.168.0.28:8002/v1"


class StockAnalysisAgents():
 
  def research_analyst(self):
    #ollama_mistral = Ollama(model="dolphin2.2-mistral:7b-q6_K")
    return Agent(
      role='Staff Research Analyst',
      goal="""Being the best at gather, interpret data and amaze
      your customer with it""",
      backstory="""Known as the BEST research analyst, you're
      skilled in sifting through news, rss feeds, and data. Now you're working on a super 
      important customer""",
      verbose=True,
      tools=[
        SearchTools.search_news,
      ]
      #llm=ollama_mistral
  )

  def research_summarizer(self):
    #ollama_mistral = Ollama(model="dolphin2.2-mistral:7b-q6_K")
    return Agent(
      role='Research Summarizer',
      goal="""Impress your customers with full analyses over the news
      and complete a summary of everything you have read.""",
      backstory="""You're the most experienced research analyst
      and you combine various analytical insights to formulate
      summary of the news. You are now working for
      a super important customer you need to impress.""",
      verbose=True,
      
      #llm=ollama_mistral
    )
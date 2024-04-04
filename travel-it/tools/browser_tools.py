import requests
import json
from bs4 import BeautifulSoup
from langchain.tools import tool
from crewai import Agent, Task
from langchain.llms import Ollama
from urllib.parse import urlparse
import os



def is_valid_url(url):
  """validate the url"""
  try:
      result= urlparse(url)
      return all([result.scheme, result.netloc])
  except Exception as e:
      return False
        
class BrowserTools():
    
        
    @tool("Scrape website content")
    def scrape_and_summarize_website(website):
        """Useful to scrape and summarize a website content"""
        #payload = json.dumps({"url": website})
        
        #ollama_mistral = Ollama(model="dolphin2.2-mistral:7b-q6_K")
   
        if is_valid_url(website):
            response = requests.get(website)
        else:
            #Something happened here and we recieved text so just summarize it and send it back.
            print(f"ERROR: {website} ")
            return "No Website Content Found"
        #soup = BeautifulSoup(response.content, 'html.parser')
        soup = BeautifulSoup(response.content)
        summarydata=soup.get_text()
        
        agent = Agent(
          role='Principal Researcher',
          goal='Do amazing research and summaries based on the content you are working with',
          backstory="You're a Principal Researcher at a big company and you need to do research about a given topic.",
          allow_delegation=False)
        task = Task(
          agent=agent,
          description=f'Analyze and summarize the content below, make sure to include the most relevant information in the summary, return only the summary nothing else.\n\nCONTENT\n----------\n{summarydata}'
        )
        summary = task.execute()

        return "\n\n".join(summary)
    
    

        
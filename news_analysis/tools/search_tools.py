import os
import json
from duckduckgo_search import DDGS
from langchain.tools import tool
import requests
import feedparser

class SearchTools():
    @tool("Search the internet")
    def search_internet(query):
        """Useful to search the internet about a a given topic and return relevant results """
        with DDGS() as ddgs:
            results = [r for r in ddgs.text(query, max_results=4)]
        string = []
        for result in results:
            try:
                string.append('\n'.join([
                    f"Title: {result['title']}", f"Link: {result['url']}",
                    f"Snippet: {result['body']}", "\n-----------------"
                ]))
            except KeyError:
                next
        return "\n".join(string)
    
    @tool("Search news on the internet")
    def search_news(query):
        """Useful to search news about a company, stock or any other """
        with DDGS() as ddgs:
            keywords = "Latest Business News" #query
            results = [r for r in ddgs.news(keywords, region="wt-wt", safesearch="off", timelimit="m", max_results=5 )]
        string = []
        for result in results:
            try:
                string.append('\n'.join([
                    f"Title: {result['title']}", f"Link: {result['href']}",
                    f"Snippet: {result['body']}", "\n-----------------"
                ]))
            except KeyError:
                next

        url = "https://www.nytimes.com/svc/collections/v1/publish/https://www.nytimes.com/section/business/rss.xml"
        feed = feedparser.parse(url)
    
        for x in range(6):
            string.append('\n'.join([
                    f"Title: {feed.entries[x].title}", f"Link: {feed.entries[x].link}",
                    f"Snippet: {feed.entries[x].description}", "\n-----------------"
                ]))


               
        return "\n".join(string)
    
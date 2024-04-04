from duckduckgo_search import DDGS
import json
import os


with DDGS() as ddgs:
    #results = [r for r in ddgs.news("Verizon", region="wt-wt", safesearch="off", timelimit="m", max_results=5 )]
    results = [r for r in ddgs.text("Tesla|Latest News", max_results=5)]

#data = json.loads(results)
string = []
top_result_to_return = 4
for result in results:
    try:
        string.append('\n'.join([
            f"Title: {result['title']}", f"Link: {result['href']}",
            f"Snippet: {result['body']}", "\n-----------------"
        ]))
    except KeyError:
        next

print('\n'.join(string))

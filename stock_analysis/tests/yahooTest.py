from langchain.tools.yahoo_finance_news import YahooFinanceNewsTool

tool = YahooFinanceNewsTool()

res = tool.run("VZ")
print(res)
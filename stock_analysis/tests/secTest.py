from sec_api import QueryApi
from dotenv import load_dotenv
import os

load_dotenv()


SEC_API_API_KEY = os.getenv('SEC_API_API_KEY')
queryApi = QueryApi(api_key=SEC_API_API_KEY)

query = {
  "query": { "query_string": {
      "query": "ticker:TSLA AND filedAt:{2020-01-01 TO 2020-12-31} AND formType:\"10-Q\""
    } },
  "from": "0",
  "size": "10",
  "sort": [{ "filedAt": { "order": "desc" } }]
}

filings = queryApi.get_filings(query)

print(filings)
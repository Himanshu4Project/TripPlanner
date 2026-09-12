from tools.tavily_tool import tavily_search

from tools.flight_tool import search_flights

# res = tavily_search("Best hotels in Darbhanga Bihar")

res = search_flights("from Delhi to New York")

print(res)
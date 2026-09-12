import os
from dotenv import load_dotenv
from tavily import TavilyClient

# Load environment variables from .env file
load_dotenv()

# Read the Tavily API key from the .env file
TAVILY_API_KEY = os.getenv("TAVILY_API_KEY")

client = TavilyClient(api_key=TAVILY_API_KEY)

def tavily_search(query):
    response = client.search(
        query=query,
        max_results=5
    )

    results = []

    for i, r in enumerate(response["results"], 1):
        title   = r.get("title", "Unknown")
        url     = r.get("url", "")
        snippet = r.get("content", "").strip()
        # Keep only the first 300 characters to avoid wall-of-text
        if len(snippet) > 300:
            snippet = snippet[:300].rsplit(" ", 1)[0] + "..."

        results.append(f"{i}. **{title}**\n   {url}\n   {snippet}")

    return "\n\n".join(results)
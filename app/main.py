from fastapi import FastAPI
from googlesearch import search

app = FastAPI()

@app.get("/google-search")
def google_search(keyword: str):
    results = search(keyword, num_results=5)

    # Create a list of result links
    links = [result for result in results]

    return {"links": links}

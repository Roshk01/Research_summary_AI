import requests
import xml.etree.ElementTree as ET

arxiv_API = "http://export.arxiv.org/api/query?"

# set parameters for the API request
# search_query: The query string to search for papers
def search_arxiv(query, max_results=5):
    params = {
        "search_query": query,
        "start": 0,
        "max_results": max_results,
        "sortBy": "relevance",
        "sortOrder": "descending"
    }
    response = requests.get(arxiv_API, params=params)
    if response.status_code != 200:
        raise Exception("Failed to Fetch Data from API")
    
    # parse the XML response
    root = ET.fromstring(response.content)
    namespace = {'n' : 'http://www.w3.org/2005/Atom'}
    papers = []

    # extract relevant information from the XML
    for entry in root.findall('n:entry',namespace):
        paper = {
            'title' : entry.find('n:title',namespace).text.strip(),
            'Published' : entry.find('n:published',namespace).text.strip(),
            'link' : entry.find('n:id',namespace).text.strip(),
            'summary' : entry.find('n:summary',namespace).text.strip()
        }
        papers.append(paper)

    return papers


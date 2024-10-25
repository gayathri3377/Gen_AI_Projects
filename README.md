<h1>Negative News and LinkedIn Profile Summarizer</h1>
This Python script is designed to extract negative news from web search results and summarize LinkedIn profile information for a given individual. It integrates OpenAI's GPT API, Azure, Selenium, and LangChain for processing news content and LinkedIn data.

Installation
To run this script, ensure you have the following prerequisites installed:

<code>pip install openai langchain selenium requests bs4</code>

<h2>Usage</h2>
Here’s a quick guide on how to use the script:

<h3>1. Set Environment Variables</h3>
You need to provide your own API keys and credentials:
<code>
BASE_URL = "<URL>"
API_KEY = "<Your_OpenAI_or_Azure_Key>"
API_VERSION = "<Your_Azure_API_Version>"
EMBEDDING_MODEL = "text-embedding-ada-002"
DEPLOYMENT_NAME = "<Your_Azure_Deployment_Name>"
</code>

<h3>2. Execute the Script</h3>
To extract negative news and LinkedIn summaries, run the following Python command:

<code>python negative_news_linkedin_summarizer.py</code>
<h2>Script Workflow</h2>
The script follows these steps:

<li>Performs Google search for negative news about a person using keywords such as "fraud," "scandal," "arrest," etc.</li>
<li>Uses Selenium to retrieve content from the search results.</li>
<li>Summarizes relevant negative news using OpenAI's GPT API.</li>
<li>Performs another search for the person’s LinkedIn profile and summarizes their job designation and employer information.</li>



<h2>Functions Overview</h2>
<li><code>callGPT4(prompt):</code> Calls the GPT API to summarize content.</li>
<li><code>get_google_search_result():</code>  Uses Google Search API or web scraping to retrieve search results.</li>
<li><code>prepare_neg_news_summary():</code>  Summarizes negative news for a person based on search results.</li>
<li><code>LinkedIn_summary():</code>  Summarizes LinkedIn profile information.</li>
<h2>Exception Handling</h2>
The script includes error handling for cases where no data is returned from searches or LinkedIn profile retrievals, logging relevant errors in the process.

<h2>Future Improvements</h2>
This script can be further enhanced by adding:
<li>Different type of search types,also includes the urls where content is summarised</li>
<li>Multi-page scraping for news articles.</li>
<li>Additional features for processing LinkedIn data.</li>
<li>Performance optimizations using threading or asyncio for parallel searches.</li>
<h2>Disclaimer</h2>
This script is designed for educational and research purposes. Ensure that you comply with legal guidelines and API rate limits when using external services like Google Search and LinkedIn.

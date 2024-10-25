Negative News and LinkedIn Profile Summarizer
This Python script is designed to extract negative news from web search results and summarize LinkedIn profile information for a given individual. It integrates OpenAI's GPT API, Azure, Selenium, and LangChain for processing news content and LinkedIn data.

Installation
To run this script, ensure you have the following prerequisites installed:

pip install openai langchain selenium requests bs4
Usage
Here’s a quick guide on how to use the script:

1. Set Environment Variables
You need to provide your own API keys and credentials:

BASE_URL = "<URL>"
API_KEY = "<Your_OpenAI_or_Azure_Key>"
API_VERSION = "<Your_Azure_API_Version>"
EMBEDDING_MODEL = "text-embedding-ada-002"
DEPLOYMENT_NAME = "<Your_Azure_Deployment_Name>"
2. Execute the Script
To extract negative news and LinkedIn summaries, run the following Python command:

python negative_news_linkedin_summarizer.py
Script Workflow
The script follows these steps:

Performs Google search for negative news about a person using keywords such as "fraud," "scandal," "arrest," etc.
Uses Selenium to retrieve content from the search results.
Summarizes relevant negative news using OpenAI's GPT API.
Performs another search for the person’s LinkedIn profile and summarizes their job designation and employer information.
Functions Overview
callGPT4(prompt): Calls the GPT API to summarize content.
get_google_search_result(): Uses Google Search API or web scraping to retrieve search results.
prepare_neg_news_summary(): Summarizes negative news for a person based on search results.
LinkedIn_summary(): Summarizes LinkedIn profile information.
Exception Handling
The script includes error handling for cases where no data is returned from searches or LinkedIn profile retrievals, logging relevant errors in the process.

Future Improvements
This script can be further enhanced by adding:

Multi-page scraping for news articles.
Additional features for processing LinkedIn data.
Performance optimizations using threading or asyncio for parallel searches.
Disclaimer
This script is designed for educational and research purposes. Ensure that you comply with legal guidelines and API rate limits when using external services like Google Search and LinkedIn.

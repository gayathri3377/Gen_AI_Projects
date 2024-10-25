
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>README</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            line-height: 1.6;
        }
        h1, h2, h3 {
            color: #333;
        }
        pre {
            background-color: #f4f4f4;
            padding: 10px;
            border: 1px solid #ddd;
            overflow-x: auto;
        }
        code {
            font-family: Consolas, 'Courier New', monospace;
            background-color: #f9f9f9;
            padding: 2px 4px;
            border-radius: 3px;
        }
    </style>
</head>
<body>
    <h1>Python Script: Negative News and LinkedIn Profile Summarizer</h1>
    <p>This Python script is designed to extract negative news from web search results and summarize LinkedIn profile information for a given individual. It integrates OpenAI's GPT API, Azure, Selenium, and LangChain for processing news content and LinkedIn data.</p>
    
    <h2>Installation</h2>
    <p>To run this script, ensure you have the following prerequisites installed:</p>
    <pre><code>pip install openai langchain selenium requests bs4</code></pre>

    <h2>Usage</h2>
    <p>Here’s a quick guide on how to use the script:</p>
    
    <h3>1. Set Environment Variables</h3>
    <p>You need to provide your own API keys and credentials:</p>
    <pre><code>BASE_URL = "&lt;URL&gt;"
API_KEY = "&lt;Your_OpenAI_or_Azure_Key&gt;"
API_VERSION = "&lt;Your_Azure_API_Version&gt;"
EMBEDDING_MODEL = "text-embedding-ada-002"
DEPLOYMENT_NAME = "&lt;Your_Azure_Deployment_Name&gt;"</code></pre>
    
    <h3>2. Execute the Script</h3>
    <p>To extract negative news and LinkedIn summaries, run the following Python command:</p>
    <pre><code>python negative_news_linkedin_summarizer.py</code></pre>

    <h2>Script Workflow</h2>
    <p>The script follows these steps:</p>
    <ol>
        <li>Performs Google search for negative news about a person using keywords such as "fraud," "scandal," "arrest," etc.</li>
        <li>Uses Selenium to retrieve content from the search results.</li>
        <li>Summarizes relevant negative news using OpenAI's GPT API.</li>
        <li>Performs another search for the person’s LinkedIn profile and summarizes their job designation and employer information.</li>
    </ol>

    <h2>Functions Overview</h2>
    <ul>
        <li><code>callGPT4(prompt)</code>: Calls the GPT API to summarize content.</li>
        <li><code>get_google_search_result()</code>: Uses Google Search API or web scraping to retrieve search results.</li>
        <li><code>prepare_neg_news_summary()</code>: Summarizes negative news for a person based on search results.</li>
        <li><code>LinkedIn_summary()</code>: Summarizes LinkedIn profile information.</li>
    </ul>

    <h2>Exception Handling</h2>
    <p>The script includes error handling for cases where no data is returned from searches or LinkedIn profile retrievals, logging relevant errors in the process.</p>

    <h2>Future Improvements</h2>
    <p>This script can be further enhanced by adding:</p>
    <ul>
        <li>Multi-page scraping for news articles.</li>
        <li>Additional features for processing LinkedIn data.</li>
        <li>Performance optimizations using threading or asyncio for parallel searches.</li>
    </ul>

    <h2>Disclaimer</h2>
    <p>This script is designed for educational and research purposes. Ensure that you comply with legal guidelines and API rate limits when using external services like Google Search and LinkedIn.</p>

</body>
</html>

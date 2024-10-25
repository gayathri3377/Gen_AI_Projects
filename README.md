
# Negative News & LinkedIn Profile Summarizer

This Python script retrieves negative news about a person and summarizes their LinkedIn profile. It integrates web scraping, Google Search via SerpAPI, and OpenAI’s GPT-4 through Azure to provide a comprehensive overview of both LinkedIn profiles and any negative media mentions.

## Features

- **Negative News Search**: Utilizes SerpAPI’s Google Search functionality to find any negative news related to a given individual. It focuses on terms related to fraud, crime, or other negative aspects.
- **LinkedIn Profile Crawling**: Scrapes LinkedIn profiles using Selenium, providing a summary of the person’s role and employer.
- **Azure OpenAI GPT-4 Integration**: Summarizes the web and LinkedIn content using GPT-4 via Azure’s OpenAI service.
- **FAISS Vectorstore**: Processes and indexes web documents for future retrieval using FAISS and OpenAI’s embedding models.

## Prerequisites

1. **Python 3.8+**
2. **API Keys**
   - Azure OpenAI API Key
   - SerpAPI Key (for Google Search)
3. **Browser Setup**: Selenium requires a Firefox or Chrome browser driver (in this case, it’s set up to use Firefox).
4. **Python Packages**: Install the required Python libraries using pip. A `requirements.txt` is provided.

   \`\`\`bash
   pip install -r requirements.txt
   \`\`\`

## Required Packages

- `langchain`
- `serpapi`
- `selenium`
- `requests`
- `bs4`
- `openai`
- `faiss`
- `beautifulsoup4`
- `logging`

## Setup

### 1. Set up API Keys

Replace the placeholder values in the script (`<<URL>>`, `<<KEY>>`, etc.) with your actual API keys and URLs.

- **Azure OpenAI API**: You need the `BASE_URL`, `API_KEY`, `API_VERSION`, and deployment name for GPT-4 and the embedding model.
- **SerpAPI**: Provide the `SERP_KEY` for Google Search.

### 2. Selenium WebDriver

Ensure Selenium WebDriver is installed and accessible in your system path. Firefox is used in this script:

1. Install the Firefox browser (if not installed already).
2. Download and install the geckodriver.

### 3. Running the Script

Run the script as follows:

\`\`\`bash
python script.py
\`\`\`

The script will:

- Fetch negative news articles (if any) related to the person’s name.
- Retrieve and summarize their LinkedIn profile, if available.

## Functions Breakdown

- **`get_query_string_for_neg_news(person_name)`**  
  Generates a Google search query for retrieving negative news about the specified person.

- **`get_google_search_result(input_string)`**  
  Fetches search results using the SerpAPI for the specified query string.

- **`prepare_neg_news_summary(search_result, person_name)`**  
  Summarizes the negative news search results by returning the top 3 article links or stating that no negative news was found.

- **`linkedIn_summary(link, person_name)`**  
  Crawls the LinkedIn page and summarizes the role/designation and employer of the specified person using GPT-4.

- **`perform_external_research()`**  
  Main function that calls both the negative news and LinkedIn profile summarization routines.

## Example

When you run the script with a name like “John Doe,” it will:

- Search for any negative news articles related to “John Doe” using Google Search.
- Retrieve “John Doe’s” LinkedIn profile (if available) and provide a summary of their professional background.

### Example Output

\`\`\`bash
No Negative news found through web search for John Doe.
LinkedIn Profile Summary:
Role: Senior Software Engineer
Employer: XYZ Corporation
\`\`\`

## Logging

This script uses Python’s logging module to log errors and key actions. Logs can be reviewed for debugging or for more detailed information about the data flow.

## License

This project is licensed under the MIT License.




from langchain.document_loaders import SeleniumURLLoader
from serpapi import GoogleSearch
from langchain.llms import AzureOpenAI
from langchain.schema import HumanMessage
from langchain.chat_models import AzureChatOpenAI
from langchain.indexes import VectorstoreIndexCreator
from langchain.text_splitter import CharacterTextSplitter
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import Chroma
from langchain.chains import RetrievalQA
from langchain.vectorstores import FAISS  # type: ignore
import requests
import w3lib.html
from bs4 import BeautifulSoup
import logging

logger = logging.getLogger('Neg_News')

BASE_URL = "<<URL>>"
API_KEY = "<<KEY>>"
API_VERSION = "<<VERSION>>"
API_TYPE = "azure"
DEPLOYMENT_NAME = "<<DEPLOYMENT_NAME>>"
EMBEDDING_MODEL = "text-embedding-ada-002"
llm = AzureChatOpenAI(
    openai_api_base=BASE_URL,
    openai_api_version=API_VERSION,
    deployment_name=DEPLOYMENT_NAME,
    openai_api_key=API_KEY,
    openai_api_type=API_TYPE,
    max_tokens=4000,
)

gpt4_url = "<<URL>>"
gpt4_data = {
    "model": "gpt-4",
    "temperature": 0.0,
    "max_tokens": 2000,
    "messages": [{"role": "user", "content": ""}]
}

def clean(content):
    return ''.join(BeautifulSoup(content, features="lxml").findAll(text=True))

def callGPT4(prompt):
    try:
        gpt4_data['messages'][0]["content"] = prompt
        response = requests.post(gpt4_url, json=gpt4_data, headers={"api-key": API_KEY})
        response=response.json()
        return response["choices"][0]["message"]["content"]
    except:
        return "No data returned due to azure content filteration."

def get_query_string_for_neg_news(person_name):
    query_name=f"{person_name}"
    fraud_string = " AND arrest OR launder OR scandal OR scam OR fraud OR illegal OR criminal "
    return query_name + fraud_string

def get_google_search_result(input_string):
    params = {
        "q": input_string,
        "api_key": "<<SERP_KEY>>",
        "engine": "google",
        "num": "10",
        "start": "1",  # CONSIDERED FIRST PAGE ONLY
    }
    search = GoogleSearch(params)
    return search.get_dict()

def prepare_neg_news_summary(search_result, person_name):
    search_information = search_result.get('search_information')
    if search_information['total_results'] < 1:
        return "No Negative news found through web search."
    organic_results_state = search_information.get('organic_results_state')
    
    final_output=""
    if organic_results_state=="Empty showing fixed spelling results" or organic_results_state=="Fully empty":
        final_output="No Negative news found through web search."
    else:
        org_res=search_result.get('organic_results')
        links=[]
        for rec in org_res[:3]:
            link=rec.get('link')
            links.append(link)
        try:
            loader = SeleniumURLLoader(urls=links,continue_on_failure=True,headless=True,browser="firefox")
            documents = loader.load()
            text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
            texts = text_splitter.split_documents(documents)
            embeddings = OpenAIEmbeddings(
                deployment=EMBEDDING_MODEL,
                openai_api_base=BASE_URL,
                openai_api_key=API_KEY,
                openai_api_type=API_TYPE,
                openai_api_version=API_VERSION,
                chunk_size=1,
            )
            db = FAISS.from_documents(texts, embeddings)
            query = "Retrieve sentences containing keywords related to arrest OR launder OR scandal OR scam OR fraud OR illegal OR criminal"
            cur_texts = db.similarity_search_with_score(query)
            for cur_text in cur_texts:
                tmp=clean(cur_text.page_content)
                tmp=tmp.split("\n")[0:2000] #Taking first 2000 tokens in each page
                whole_text=whole_text+"\n".join(tmp)
                count += len(tmp)
                if count > 2000: break

            summary_prompt="You have provided web content from several pages related to a person, and your task is to extract any negative news about that person and summarize it in two sentences. If you don't find any relevant negative news, please return the message \No negative news was found for [person_name]. Here is the Input \n person name:"+person_name+"crawled web content:\n"+whole_text
            final_output=callGPT4(summary_prompt)
        except Exception as e:
            logger.error(str(e),exc_info=True)
            final_output="No negative news was found for "+person_name+"\n"
    return final_output

def get_negative_news(person_name):
    qry=get_query_string_for_neg_news(person_name)
    google_res=get_google_search_result(qry)
    return prepare_neg_news_summary(google_res,person_name)

def linkedIn_summary(link,person_name):
    urls = [link]
    loader = SeleniumURLLoader(urls=urls)
    strdata=loader.load()
    tmp=clean(strdata[0].page_content)
    final_prompt=f"You have provided LinkedIn CRAWLED CONTENT of a person. Your task is to extract the person's role/designation and their employer from the given information.\n Extract the role and employer based on the LinkedIn profile . The [PERSON]'s role/designation is [Role/Designation] and employer is [Employer]. \nIf the content DOES NOT FULLY MATCH with the person's name, please return 'No matching LinkedIn profile was found for {person_name}. \nPERSON:"+name+"\nCRAWLED CONTENT:"+tmp
    output=callGPT4(final_prompt)
    return output

def get_linked_in_summary(person_name,location):
    google_res=get_google_search_result(person_name+" "+location)
    org_res=google_res.get('organic_results')
    link=""
    for rec in org_res:
        source=rec.get("source")
        if source=="LinkedIn":
            link=rec.get("link")
    response=""
    if link=="":
        response="No matching LinkedIn profile was found for "+person_name+"."
    else:
        response=linkedIn_summary(link,person_name)
    return response

def perform_external_research():
    linked_in=get_linked_in_summary("Gayathri ","Guwahati,India")
    neg_news=get_negative_news("Gayathri Peddapolu")
    
    print("--------------------")
    print(linked_in)
    print(neg_news)
    print("--------------------")

if __name__ == '__main__':
    perform_external_research()


from pyResearchInsights.common_functions import pre_processing
from pyResearchInsights.Scraper import scraper_main

'''Abstracts containing these keywords will be queried from Springer'''
keywords_to_search = "Western Ghats Conservation"

'''Calling the pre_processing functions here so that abstracts_log_name and status_logger_name is available across the code.'''
abstracts_log_name, status_logger_name = pre_processing(keywords_to_search)

'''Runs the scraper here to scrape the details from the scientific repository'''
scraper_main(keywords_to_search, abstracts_log_name, status_logger_name)


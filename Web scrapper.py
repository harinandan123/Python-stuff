from autoscraper import AutoScraper


# We can add one or multiple candidates here.
# You can also put urls here to retrieve urls.


scraper = AutoScraper()
result = scraper.get_result_similar('https://stackoverflow.com/questions/606191/convert-bytes-to-a-string')
print(result)
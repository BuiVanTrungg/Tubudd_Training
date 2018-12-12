from urllib.request import urlopen
from link_finder import LinkFinder
from craw import *


class Spider:
    projectName = ''
    baseUrl = ''
    domainName = ''
    queueFile = ''
    crawledFile = ''
    queue = set()
    crawled = set()

    def __init__(self, projectName, baseUrl, domainName):
        Spider.projectName = projectName
        Spider.baseUrl = baseUrl
        Spider.domainName = domainName
        Spider.queueFile = Spider.projectName+'/queue.txt'
        Spider.crawledFile = Spider.projectName+'/crawled.txt'

        self.boot()
        self.crawl_page('First spider', Spider.baseUrl)   

    @staticmethod
    def boot(self):
        createProjectDir(Spider.projectName)
        createDataFile(Spider.projectName, Spider.baseUrl)
        Spider.queue = fileToSet(Spider.queueFile)
        Spider.crawled = fileToSet(Spider.crawledFile)

    @staticmethod
    def crawl_page(threadName, pageUrl):
        if pageUrl not in Spider.crawled:
            print(threadName+'now crawling ' + pageUrl)
            print('Queue '+str(len(Spider.queue))+ '| Crawled '+str(len(Spider.crawled)))
            Spider.add_link_to_queue(Spider.gather_links(pageUrl))
            Spider.queue.remove(pageUrl)
            Spider.crawled.add(pageUrl)
            Spider.update_files()

    
         
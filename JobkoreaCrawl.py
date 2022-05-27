#!/usr/bin/env python3
# -*- coding:utf-8 -*-

from time import sleep
from bs4 import BeautifulSoup as bs
import pandas as pd
from MyRequest import MyRequest
from datetime import datetime
import sys


class JobkoreaCrawl:
    def __init__(self) -> None:
        self.request = MyRequest()
        self.baseUrl = "https://www.jobkorea.co.kr/Search/?stext="

    def getKeyword(self, keywords):
        keywordList = []
        for keyword in keywords:
            keywordList.append(keyword + " ")
        keywords = "".join(keywordList)
        print("Searching Keyword: " + keywords)
        return keywords

    def usage(self):
        print("Usage: python3 " + sys.argv[0] + " [keyword]")

    def search(self, keyword, page_num):
        url = self.baseUrl + keyword
        if page_num > 1:
            url = url + "&Page_No=" + str(page_num)
        r = self.request.get(url)
        if r.status_code != 200:
            raise Exception("Error: " + str(r.status_code))

        response = r.text
        soup = bs(response, "html.parser")
        name = [ele.text for ele in soup.select("a.name")][:19]
        detail = [ele.text for ele in soup.select("div.post-list-info > a.title")][:19]
        detail = [ele.replace("\n", "").replace("\r", "") for ele in detail]

        # https://pandas.pydata.org/Pandas_Cheat_Sheet.pdf
        pd.set_option("max_colwidth", 100)
        df = pd.DataFrame({"기업 이름": name, "상세 내용": detail})
        return df

    def output(self, df):
        date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print("검색 일자 : " + date)
        print(df)


if __name__ == "__main__":
    crawl = JobkoreaCrawl()
    keyword = crawl.getKeyword(sys.argv[1:])

    if not keyword:
        crawl.usage()
        sys.exit()

    for i in range(1, 10):
        df = crawl.search(keyword, i)
        crawl.output(df)
        sleep(1)

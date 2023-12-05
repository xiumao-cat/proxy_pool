# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     proxyFetcher
   Description :
   Author :        JHao
   date：          2016/11/25
-------------------------------------------------
   Change Activity:
                   2016/11/25: proxyFetcher
-------------------------------------------------
"""
__author__ = 'JHao'

import re
import json
from time import sleep

from util.webRequest import WebRequest


class ProxyFetcher(object):
    """
    proxy getter
    """

    @staticmethod
    def freeProxy01(page_count=5):
        """ 站大爷 """
        url = "https://www.zdaye.com/free/{}/"
        urls = [url.format(page) for page in range(1, page_count + 1)]
        for urlz in urls:
            sleep(3)
            html = WebRequest().get(urlz, timeout=10).tree
            print(html)
            if not html:
                return
            for tr in html.xpath("//table//tr")[1:]:
                ip = "".join(tr.xpath('./td[1]/text()')).strip()
                port = "".join(tr.xpath('./td[2]/text()')).strip()
                yield "%s:%s" % (ip, port)

    @staticmethod
    def freeProxy02():
        """
        代理66 http://www.66ip.cn/
        """
        url = "http://www.66ip.cn/"
        resp = WebRequest().get(url, timeout=10).tree
        for i, tr in enumerate(resp.xpath("(//table)[3]//tr")):
            if i > 0:
                ip = "".join(tr.xpath("./td[1]/text()")).strip()
                port = "".join(tr.xpath("./td[2]/text()")).strip()
                yield "%s:%s" % (ip, port)

    @staticmethod
    def freeProxy03(page_count=10):
        """ 开心代理 """
        target_urls = ["http://www.kxdaili.com/dailiip/1/{}.html", "http://www.kxdaili.com/dailiip/2/{}.html"]
        for url in target_urls:
            urls = [url.format(page) for page in range(1, page_count + 1)]
            for urlz in urls:
                html = WebRequest().get(urlz, timeout=10).tree
                if not html:
                    return
                for tr in html.xpath("//table[@class='active']//tr")[1:]:
                    ip = "".join(tr.xpath('./td[1]/text()')).strip()
                    port = "".join(tr.xpath('./td[2]/text()')).strip()
                    yield "%s:%s" % (ip, port)

    @staticmethod
    def freeProxy04(page_count=10):
        """ https://www.69ip.cn/ """
        urlz = "https://www.69ip.cn/?page={}"
        urls = [urlz.format(page) for page in range(1, page_count + 1)]
        for url in urls:
            html = WebRequest().get(url, timeout=30).tree
            if not html:
                return
            for tr in html.xpath("//table//tr")[1:]:
                ip = "".join(tr.xpath('./td[1]/text()')).strip()
                port = "".join(tr.xpath('./td[2]/text()')).strip()
                yield "%s:%s" % (ip, port)

    @staticmethod
    def freeProxy05(page_count=2):
        """ 快代理 https://www.kuaidaili.com """
        url_pattern = [
            'https://www.kuaidaili.com/free/inha/{}/',
            'https://www.kuaidaili.com/free/intr/{}/'
        ]
        url_list = []
        for page_index in range(1, page_count + 1):
            for pattern in url_pattern:
                url_list.append(pattern.format(page_index))

        for url in url_list:
            tree = WebRequest().get(url).tree
            proxy_list = tree.xpath('.//table//tr')
            sleep(1)  # 必须sleep 不然第二条请求不到数据
            for tr in proxy_list[1:]:
                yield ':'.join(tr.xpath('./td/text()')[0:2])

    @staticmethod
    def freeProxy06():
        """ FateZero http://proxylist.fatezero.org/ """
        url = "http://proxylist.fatezero.org/proxy.list"
        try:
            resp_text = WebRequest().get(url).text
            for each in resp_text.split("\n"):
                json_info = json.loads(each)
                if json_info.get("country") == "CN":
                    yield "%s:%s" % (json_info.get("host", ""), json_info.get("port", ""))
        except Exception as e:
            print(e)

    @staticmethod
    def freeProxy07():
        """ 云代理 """
        urls = ['http://www.ip3366.net/free/?stype=1', "http://www.ip3366.net/free/?stype=2"]
        for url in urls:
            r = WebRequest().get(url, timeout=10)
            proxies = re.findall(r'<td>(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})</td>[\s\S]*?<td>(\d+)</td>', r.text)
            for proxy in proxies:
                yield ":".join(proxy)

    @staticmethod
    def freeProxy08():
        """ 小幻代理 """
        urls = ['https://ip.ihuan.me/address/5Lit5Zu9.html','https://ip.ihuan.me/address/5Lit5Zu9.html?page=4ce63706','https://ip.ihuan.me/address/5Lit5Zu9.html?page=5crfe930','https://ip.ihuan.me/address/5Lit5Zu9.html?page=f3k1d581','https://ip.ihuan.me/address/5Lit5Zu9.html?page=ce1d45977','https://ip.ihuan.me/address/5Lit5Zu9.html?page=881aaf7b5','https://ip.ihuan.me/address/5Lit5Zu9.html?page=eas7a436','https://ip.ihuan.me/address/5Lit5Zu9.html?page=981o917f5','https://ip.ihuan.me/address/5Lit5Zu9.html?page=2d28bd81a','https://ip.ihuan.me/address/5Lit5Zu9.html?page=a42g5985d']
        for url in urls:
            r = WebRequest().get(url, timeout=10)
            proxies = re.findall(r'>\s*?(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})\s*?</a></td><td>(\d+)</td>', r.text)
            for proxy in proxies:
                yield ":".join(proxy)

    @staticmethod
    def freeProxy09(page_count=10):
        urlz = "https://proxy.ip3366.net/free/?action=china&page={}"
        urls = [urlz.format(page) for page in range(1, page_count + 1)]
        for url in urls:
            html = WebRequest().get(url, timeout=20).tree
            if not html:
                return
            for tr in html.xpath("//table//tr")[1:]:
                ip = "".join(tr.xpath('./td[1]/text()')).strip()
                port = "".join(tr.xpath('./td[2]/text()')).strip()
                yield "%s:%s" % (ip, port)

    @staticmethod
    def freeProxy10(page_count=100):
        """ https://www.89ip.cn"""
        urlz = "https://www.89ip.cn/index_{}.html"
        urls = [urlz.format(page) for page in range(1, page_count + 1)]
        for url in urls:
            sleep(3)
            html = WebRequest().get(url, timeout=20).tree
            if not html:
                return
            for tr in html.xpath("//table//tr")[1:]:
                ip = "".join(tr.xpath('./td[1]/text()')).strip()
                port = "".join(tr.xpath('./td[2]/text()')).strip()
                yield "%s:%s" % (ip, port)

    @staticmethod
    def freeProxy11():
        """ 稻壳代理 https://www.docip.net/ """
        r = WebRequest().get("https://www.docip.net/data/free.json", timeout=10)
        try:
            for each in r.json['data']:
                yield each['ip']
        except Exception as e:
            print(e)

    @staticmethod
    def freeProxy12(page_count=100):
        """ https://www.binglx.cn"""
        urlz = "https://www.binglx.cn/?page={}"
        urls = [urlz.format(page) for page in range(1, page_count + 1)]
        for url in urls:
            html = WebRequest().get(url, timeout=60).tree
            if not html:
                return
            for tr in html.xpath("//table//tr")[1:]:
                ip = "".join(tr.xpath('./td[1]/text()')).strip()
                port = "".join(tr.xpath('./td[2]/text()')).strip()
                yield "%s:%s" % (ip, port)
    # @staticmethod
    # def wallProxy01():
    #     """
    #     PzzQz https://pzzqz.com/
    #     """
    #     from requests import Session
    #     from lxml import etree
    #     session = Session()
    #     try:
    #         index_resp = session.get("https://pzzqz.com/", timeout=20, verify=False).text
    #         x_csrf_token = re.findall('X-CSRFToken": "(.*?)"', index_resp)
    #         if x_csrf_token:
    #             data = {"http": "on", "ping": "3000", "country": "cn", "ports": ""}
    #             proxy_resp = session.post("https://pzzqz.com/", verify=False,
    #                                       headers={"X-CSRFToken": x_csrf_token[0]}, json=data).json()
    #             tree = etree.HTML(proxy_resp["proxy_html"])
    #             for tr in tree.xpath("//tr"):
    #                 ip = "".join(tr.xpath("./td[1]/text()"))
    #                 port = "".join(tr.xpath("./td[2]/text()"))
    #                 yield "%s:%s" % (ip, port)
    #     except Exception as e:
    #         print(e)

    # @staticmethod
    # def freeProxy10():
    #     """
    #     墙外网站 cn-proxy
    #     :return:
    #     """
    #     urls = ['http://cn-proxy.com/', 'http://cn-proxy.com/archives/218']
    #     request = WebRequest()
    #     for url in urls:
    #         r = request.get(url, timeout=10)
    #         proxies = re.findall(r'<td>(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})</td>[\w\W]<td>(\d+)</td>', r.text)
    #         for proxy in proxies:
    #             yield ':'.join(proxy)

    # @staticmethod
    # def freeProxy11():
    #     """
    #     https://proxy-list.org/english/index.php
    #     :return:
    #     """
    #     urls = ['https://proxy-list.org/english/index.php?p=%s' % n for n in range(1, 10)]
    #     request = WebRequest()
    #     import base64
    #     for url in urls:
    #         r = request.get(url, timeout=10)
    #         proxies = re.findall(r"Proxy\('(.*?)'\)", r.text)
    #         for proxy in proxies:
    #             yield base64.b64decode(proxy).decode()

    # @staticmethod
    # def freeProxy12():
    #     urls = ['https://list.proxylistplus.com/Fresh-HTTP-Proxy-List-1']
    #     request = WebRequest()
    #     for url in urls:
    #         r = request.get(url, timeout=10)
    #         proxies = re.findall(r'<td>(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})</td>[\s\S]*?<td>(\d+)</td>', r.text)
    #         for proxy in proxies:
    #             yield ':'.join(proxy)


if __name__ == '__main__':
    p = ProxyFetcher()
    for _ in p.freeProxy01():
        print(_)

# http://nntime.com/proxy-list-01.htm


# freeProxy04
# freeProxy07
# freeProxy08

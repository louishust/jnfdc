from lxml import html
import requests
from ..models import NetSign
from datetime import date
from datetime import datetime

def fetch_jnfdc():
    try:
        page = requests.get('http://www.jnfdc.gov.cn/', timeout=10)
        tree = html.fromstring(page.content)
        sn = tree.xpath('//div[@id="todayview"]/div[@class="col_bg"]/ul[1]/ul[1]/li[2]/text()')[0]
        netsign = NetSign.query.filter_by(date=date.today()).first()
        if netsign is None:
            netsign = NetSign(signnum = int(sn), date = date.today())
        else:
            netsign.signnum = int(sn)
        print("{0}:{1}".format(datetime.now(), sn))
        netsign.add()
    except Exception:
        pass

if __name__ == '__main__':
    parse_jnfdc()


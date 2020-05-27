import requests
import json
from fake_useragent import UserAgent
STATS_URL = "http://stats.aoeu.eu/mqtt"

def createParameters(CPM, rawCPM, wrong, words, ip, keys, chars, cheater, iphone, enterused, seconds):
    return {"typing-speed-test.aoeu.eu": str(CPM) + " CPM",
            "tst-internal/details": json.dumps({
                'cpm': CPM,
                'rawcpm': rawCPM,
                'wrong': wrong,
                'words': words,
                'ip': ip,
                'keys': keys,
                'chars': chars,
                'cheater': cheater,
                'iphone': iphone,
                'enterused': enterused,
                's': seconds
            }, separators=(',', ':'))}


def post(CPM):
    ua = UserAgent()
    ua.update()
    header = {'Origin': 'https://typing-speed-test.aoeu.eu', 'User-Agent':str(ua.random)}
    print(header)
    return requests.post(STATS_URL, createParameters(CPM, 330, 30, 75, "50.203.23.392", 2030, 310, 0, 0, 0, 60), headers=header)

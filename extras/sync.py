from urllib.request import Request, urlopen 
from time import time

sites = [
    "http://news.ycombinator.com/",
    "https://www.yahoo.com/",
    "https://github.com/",
    "http://deelay.me/5000/http://deelay.me/",
]


def find_size(url):
    req = Request(url)
    with urlopen(req) as response:
        page = response.read()
        # print(page)
        return len(page)

def main():
    for site in sites:
        start_t = time()
        size = find_size(site)
        print("read {:8d} chars from {} in {} secs ".format(size, site,  time() - start_t))


if __name__ == '__main__':
    start_time = time()
    main()
    print("Ran in {:6.3f} secs".format(time() - start_time))


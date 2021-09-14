API_URL = "http://api.herocheck.com/?q={0}"

class __MockWebClinet:

    @staticmethod
    def get(url):
        return True

webclient = __MockWebClinet()


class SuperHeroWebAPI:

    @staticmethod
    def is_hero(username:str) -> bool :
        blacklist = set(["syndrome", "kcka$$", "superfake"])
        url = API_URL.format(username)
        return username not in blacklist and webclient.get(url)

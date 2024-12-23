

class Elems():

    @staticmethod
    def pictures_lettering():
        selector = str('body > div.L3eUgb > div.o3j99.LLD4me.yr19Zb.LS8OJ > div > span')
        return selector

    @staticmethod
    def mail_link():
        selector = str('#gb > div > div:nth-child(1) > div > div:nth-child(1) > a')
        return selector

    @staticmethod
    def mail_logo():
        selector = str("#root > div:nth-child(1) > header > div > div.header__logos > a > span")
        return selector
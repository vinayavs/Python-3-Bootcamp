# INITIALIZING OBJECTS AUTOMATICALLY
class SportsNews:
    def sportsInfo(self):
        print('Cric Info..')
        print('Badminton Info..')
class BusinessNews:
    def bizInfo(self):
        print('Stock Info...')
        print('ETF Info...')
class ViNews:
    def __init__(self):
        self.sportsnews = SportsNews() # Initilizing Objs automatically
        self.businessnews = BusinessNews()
    def totalInfo(self):
        print("TODAY'S VI NEWS HEADLINES...")
        self.sportsnews.sportsInfo()
        print()
        self.businessnews.bizInfo()
news = ViNews()
news.totalInfo()


# ALTERNATIVE
# class SportsNews:
#     def sportsInfo(self):
#         print('Cric Info..')
#         print('Badminton Info..')
# class BusinessNews:
#     def bizInfo(self):
#         print('Stock Info...')
#         print('ETF Info...')
# class ViNews:
#     def __init__(self,sportsnews,businessnews):
#         self.sportsnews = sportsnews
#         self.businessnews = businessnews
#     def totalInfo(self):
#         print("TODAY'S VI NEWS HEADLINES...")
#         self.sportsnews.sportsInfo()
#         print()
#         self.businessnews.bizInfo()
# sprotsNews = SportsNews()
# businessNews = BusinessNews()
# news = ViNews(sprotsNews,businessNews)
# news.totalInfo()

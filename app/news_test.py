import unittest
from models import Articles,Source,TopHeadlines

class ArticlesTest(unittest.TestCase):
  '''
  Test class to test behaviour of the article class
  '''
  def setUp(self):
      ''' 
      set up method that will run before every Test
      '''
      self.new_article = Articles( "Gian M. Volpicelli", "Gibraltar Could Launch the World First Crypto Stock Exchange","“The Rock” hopes a new stock exchange will attract crypto millionaires who want to avoid hefty taxes.", "https://www.wired.com/story/gibraltar-crypto-exchange/", "https://media.wired.com/photos/61f0b4bf03f9ae99229f47d4/191:100/w_1280,c_limit/Business_Gibraltar-1208348908.jpg", "2022-01-26T12:00:00Z","British entrepreneur and financier Richard ODell Poulden hopes that his new venture will relieve the plight of an underserved cohort: Bitcoin billionaires who want to buy a house. In October, Poulde… [+3364 chars]")
  def test_instance(self):
    self.assertTrue(isinstance(self.new_article, Articles))    


class SourceTest(unittest.TestCase):
  '''
  Test class to test behaviour of the source class
  '''
  def setUp(self):
      ''' 
      set up method that will run before every Test
      '''
      self.new_article = Source( "al-jazeera-english", "Al Jazeera English", "News, analysis from the Middle East and worldwide, multimedia and interactives, opinions, documentaries, podcasts, long reads and broadcast schedule.", "http://www.aljazeera.com", "general", "en", "us")
  def test_instance(self):
    self.assertTrue(isinstance(self.new_article, Source))    


class TopHeadlinesTest(unittest.TestCase):
  '''
  Test class to test behaviour of the source class
  '''
  def setUp(self):
      ''' 
      set up method that will run before every Test
      '''
      self.new_article = TopHeadlines( 'null', "KFSN-TV", "Jessica Harrington, Nic Garcia", "Stockton fire captain dies after being shot while battling fire, police say - KFSN-TV", "Authorities say a Stockton fire captain died after being shot while battling a fire on Monday morning.", "https://abc30.com/stockton-firefighter-shot-fireman-fire/11525858/", "https://cdn.abcotvs.com/dip/images/11526515_maxfortuna.JPG?w=1600", "2022-02-01T06:33:45Z", "STOCKTON, Calif. -- Hundreds of North Valley firefighters and officers paid their respects after a fire captain was shot and killed on the job Monday.An investigation is underway and 67-year-old Robe… [+2530 chars]")
  def test_instance(self):
    self.assertTrue(isinstance(self.new_article, TopHeadlines))    
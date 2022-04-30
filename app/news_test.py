import unittest
from models import Sources, Articles, TopHeadLines


class SourceTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the source class
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.article = Sources("cnn", "CNN","View the latest news and breaking news today for U.S., world, weather, entertainment, politics and health at CNN","http://us.cnn.com","general","en","us") 

    def test_instance(self):
        self.assertTrue(isinstance(self.new_article,Sources))

class ArticlesTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the article class
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.article = Articles("cnn", "CNN","View the latest news and breaking news today for U.S., world, weather, entertainment, politics and health at CNN","http://us.cnn.com","general","en","us") 

    def test_instance(self):
        self.assertTrue(isinstance(self.new_article,Articles))

class TopHeadLinesTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the TopHeadLine class
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.article = TopHeadLines("cnn", "CNN","View the latest news and breaking news today for U.S., world, weather, entertainment, politics and health at CNN","http://us.cnn.com","general","en","us") 

    def test_instance(self):
        self.assertTrue(isinstance(self.new_article,TopHeadLines))

if __name__ == '__main__':
    unittest.main()  
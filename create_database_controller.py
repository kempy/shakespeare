import webapp2
from tasks.parser import Parser

class CreateDatabaseController(webapp2.RequestHandler):

    def get(self):
        parser = Parser('test_data')
        parser.parse()

        self.redirect('/')
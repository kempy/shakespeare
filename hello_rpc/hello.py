import webapp2
import urllib

from google.appengine.api import urlfetch

class MainPage(webapp2.RequestHandler):

    def get(self):
        self.response.headers['Content-Type'] = 'text/plain'
        self.response.write('Hello, World!')
        
        rpc = urlfetch.create_rpc()
        
        form_fields = { "term": "notebook" }
        form_data = urllib.urlencode(form_fields)
        urlfetch.make_fetch_call(rpc, "http://definition-server.appspot.com/definition.define", payload=form_fields, headers={"content-type": "content-type:application/json"})


        try:
            result = rpc.get_result()
            if result.status_code == 200:
                text = result.content
                print "--------------- " + text
                self.response.write(text)
            else:
                print "--------------- ",
                print result.content
        except urlfetch.DownloadError:
            print "--------------- error"

app = webapp2.WSGIApplication([
    ('/', MainPage),
], debug=True)

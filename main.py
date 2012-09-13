import webapp2

class HelloWebapp2(webapp2.RequestHandler):
    def get(self):
        f = open('data.json', 'r')
        self.response.write('<html><head><title>Hola Mundo</title></head><body><h1>Hello, webapp2!</h1></body></html>')

class TellHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write(self.request.GET['message'])

class ApiHandler(webapp2.RequestHandler):
    def get(self):
        data = [
            {
                "employees": [
                    { "firstName":"John" , "lastName":"Doe" }, 
                    { "firstName":"Anna" , "lastName":"Smith" }, 
                    { "firstName":"Peter" , "lastName":"Jones" }
                ]
            }
        ]
        import json
        self.response.write(json.dumps(data))
        self.response.headers['Content-Type'] = 'application/json'


app = webapp2.WSGIApplication([
    ('/', HelloWebapp2),
    ('/tell*', TellHandler),
    ('/employees', ApiHandler),
], debug=True)

def main():
    from paste import httpserver
    httpserver.serve(app, host='0.0.0.0', port='8080')

if __name__ == '__main__':
    main()
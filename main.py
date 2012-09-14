import webapp2
import json

class MainPage(webapp2.RequestHandler):
    def get(self):
        import json
        try:
            f = open('data.json', 'r')
            self.response.out.write(json.dumps(f.read()))
            f.close()
            self.response.headers['Content-Type'] = 'application/json'
        except Exception:
            self.response.status = 404

    def post(self):
        try:
            f = open('data.json', 'r')
            data = json.load(f.read()) 
        except Exception:
            f = open('data.json', 'w')
            f.write('{ "mensajes" :[ ] }')
            f = open('data.json')
            data = json.load(f) 
            f.close()

        if self.request.content_type == 'application/json':
            data["mensajes"].append(json.loads(self.request.body))
        else:
            data["mensajes"].append(self.request.body)

        f = open("data.json","w")
        f.write(json.dumps(data))
        f.close()

               
       
        self.response.out.write('Mensaje enviado correctamente')        
      


app = webapp2.WSGIApplication([
    ('/', MainPage),    
], debug=True)

def main():
    from paste import httpserver
    httpserver.serve(app, host='0.0.0.0', port='8080')

if __name__ == '__main__':
    main()
    app.run()

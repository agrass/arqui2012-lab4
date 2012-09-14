# -*- coding: UTF-8 -*-

import sys
import webapp2
import tempfile
import os
import shutil
# para Python 2.6 o inferior, utilizamos unittest2
if sys.hexversion < 0x2070000:
    import unittest2 as unittest
else:
    import unittest

import main # el módulo a probar

class TestWebApp(unittest.TestCase):
    
    def setUp(self):
        self.old_dir = os.path.abspath(os.curdir)
        self.cwd = tempfile.mkdtemp()
        os.chdir(self.cwd)

    def tearDown(self):
        os.chdir(self.old_dir)
        shutil.rmtree(self.cwd)

    def test_unit_get_db_fail(self):
        request = webapp2.Request.blank('/')
        request.method = 'GET'
        response = request.get_response(main.app)       
        try:
            open('data.json')
        except Exception:           
            self.assertTrue(True)
            return
        self.assertTrue(False)

    def test_unit_get_db_ok(self):
        f = open('data.json', 'w')
        f.write('{ "mensajes" :[ ] }')
        f.close()
        request = webapp2.Request.blank('/')
        request.method = 'GET'
        response = request.get_response(main.app)          
        try:
            open("data.json")
        except Exception:            
            self.assertTrue(False)
            return
        self.assertTrue(True)

    def test_unit_post_json_db_fail(self):        
        request = webapp2.Request.blank('/')
        request.method = 'POST'
        request.headers['Content-Type'] = 'application/json'
        request.body = '{"whololo":"ejemplo"}'
        response = request.get_response(main.app)
        f = open("data.json","r")
        data = f.read()
        self.assertEqual(data,'{"mensajes": [{"whololo": "ejemplo"}]}')

    def test_unit_post_text_db_fail(self):        
        request = webapp2.Request.blank('/')
        request.method = 'POST'
        request.headers['Content-Type'] = 'application/text'
        request.body = 'whololo'
        response = request.get_response(main.app)
        f = open("data.json","r")
        data = f.read()
        self.assertEqual(data,'{"mensajes": ["whololo"]}')

    def test_unit_post_json_db_ok(self):
        f = open('data.json', 'w')
        f.write('{ "mensajes" :[ ] }')
        f.close()
        request = webapp2.Request.blank('/')
        request.method = 'POST'
        request.headers['Content-Type'] = 'application/json'
        request.body = '{"whololo":"ejemplo"}'
        response = request.get_response(main.app)
        g = open("data.json","r")
        data = g.read()
        self.assertEqual(data,'{"mensajes": [{"whololo": "ejemplo"}]}')

    def test_unit_post_text_db_ok(self):
        f = open('data.json', 'w')
        f.write('{ "mensajes" :[ ] }')
        f.close()
        request = webapp2.Request.blank('/')
        request.method = 'POST'
        request.headers['Content-Type'] = 'application/text'
        request.body = 'whololo'
        response = request.get_response(main.app)
        g = open("data.json","r")
        data = g.read()
        self.assertEqual(data,'{"mensajes": ["whololo"]}')

    
    def test_get_db_fail(self):        
        request = webapp2.Request.blank('/')
        request.method = 'GET'
        response = request.get_response(main.app)      
        self.assertEqual(response.status_int, 404)


    def test_get_db_ok(self):
        f = open('data.json', 'w')
        f.write('{ "mensajes" :[ ] }')
        f.close()        
        request = webapp2.Request.blank('/')
        request.method = 'GET'
        response = request.get_response(main.app)      
        self.assertEqual(response.status_int, 200)
        self.assertEqual(response.body,'"{ \\"mensajes\\" :[ ] }"')
        

    def test_post_JSON_db_fail(self):        
        request = webapp2.Request.blank('/')
        request.method = 'POST'
        request.headers['Content-Type'] = 'application/json'
        request.body = '{"whololo":"ejemplo"}'
        response = request.get_response(main.app)      
        self.assertEqual(response.status_int, 200)
        self.assertEqual(response.body,'Mensaje enviado correctamente')

    def test_post_JSON_db_ok(self):
        f = open('data.json', 'w')
        f.write('{ "mensajes" :[ ] }')
        f.close()      
        request = webapp2.Request.blank('/')
        request.method = 'POST'
        request.headers['Content-Type'] = 'application/json'
        request.body = '{"whololo":"ejemplo"}'
        response = request.get_response(main.app)      
        self.assertEqual(response.status_int, 200)
        self.assertEqual(response.body,'Mensaje enviado correctamente')
  
        

    def test_post_text_db_fail(self):        
        request = webapp2.Request.blank('/')
        request.method = 'POST'
        request.headers['Content-Type'] = 'application/text'
        request.body = 'whololo'
        response = request.get_response(main.app)      
        self.assertEqual(response.status_int, 200)
        self.assertEqual(response.body,'Mensaje enviado correctamente')

    def test_post_text_db_ok(self):
        f = open('data.json', 'w')
        f.write('{ "mensajes" :[ ] }')
        f.close()
        request = webapp2.Request.blank('/')
        request.method = 'POST'
        request.body = 'whololo'
        request.headers['Content-Type'] = 'application/text'
        response = request.get_response(main.app)      
        self.assertEqual(response.status_int, 200)
        self.assertEqual(response.body,'Mensaje enviado correctamente')    
        


    if __name__ == '__main__':
        unittest.main()

       
# -*- coding: UTF-8 -*-

import sys
# para Python 2.6 o inferior, utilizamos unittest2
if sys.hexversion < 0x2070000:
    import unittest2 as unittest
else:
    import unittest

import main # el módulo a probar

class TestWebApp(unittest.TestCase):

    def get_db_fail(self):
        request = webapp2.Request.blank('/')
        request.method = 'GET'
        response = request.get_response(main.app)      
        self.assertEqual(response.status_int, 404)

    def get_db_ok(self):
        request = webapp2.Request.blank('/')
        request.method = 'GET'
        response = request.get_response(main.app)      
        self.assertEqual(response.status_int, 200)

    def post_JSON_db_fail(self):
        request = webapp2.Request.blank('/')
        request.method = 'POST'
        request.headers['Content-Type'] = 'application/json'
        response = request.get_response(main.app)      
        self.assertEqual(response.status_int, 404)

    def post_JSON_db_fail(self):
        request = webapp2.Request.blank('/')
        request.method = 'POST'
        request.headers['Content-Type'] = 'application/json'
        response = request.get_response(main.app)      
        self.assertEqual(response.status_int, 404)

    def post_text_db_fail(self):
        request = webapp2.Request.blank('/')
        request.method = 'POST'
        request.headers['Content-Type'] = 'application/json'
        response = request.get_response(main.app)      
        self.assertEqual(response.status_int, 404)


    if __name__ == '__main__':
        unittest.main()

       
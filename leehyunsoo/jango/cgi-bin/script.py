import cgi
import os

form = cgi.FieldStorage()

language = form.getvalue('language')
framework = form.getvalue('framework')
email = form.getvalue('email')

print('Content-type : text/plain')
print('\r')
print('Welcome, CGI Scripts')
print('language : ', language)
print('framework : ', framework)
print('email : ', email)

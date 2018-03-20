
def my_app(environ, start_respone):
    status = '200 OK'
    headers = [('Content-Type','text/plain')]
    start_respone(status, headers)

    return ['This is a sample WSGI Application'.encode('utf-8')]

if __name__ == '__main__':
    from wsgiref.simple_server import make_server

    print('started WSGI Server on port 8888')
    server = make_server('', 8888, my_app)
    server.serve_forever()

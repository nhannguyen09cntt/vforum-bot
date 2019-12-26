import http.server
import socketserver
import simplejson
from google_search import GoogleSeach

PORT = 8080
DIRECTORY = 'public'


class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIRECTORY, **kwargs)

    def do_POST(self):
        self.send_response(200)
        content_length = int(self.headers['Content-Length'])
        post_body = self.rfile.read(content_length)
        self.end_headers()
        print('user query', post_body)
        topic_data = simplejson.loads(post_body)
        print('user query', topic_data["title"])
        google_bot = GoogleSeach()
        google_search_chatbot_reply = google_bot.chatbot_query(topic_data)
        self.wfile.write(str.encode(google_search_chatbot_reply))


with socketserver.TCPServer(('', PORT), Handler) as httpd:
    print('serving at port', PORT)
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    httpd.server_close()

import os.path
import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web
import torndb

from tornado.options import define, options
from tornado.web import url ,RequestHandler

define("port", default=5000, help="run on the given port", type=int)

# our python app

todoList = []

class Application(tornado.web.Application):
	def __init__(self):
		handlers = [
			url(r"/", IndexHandler),
			url(r"/getNewsByIssue", GetNewsByIssueHandler,name='getNewsByIssue'),
			url(r"/add", AddHandler,name='add')
		]
		settings = dict(
			template_path=os.path.join(os.path.dirname(__file__), "templates"),
			static_path=os.path.join(os.path.dirname(__file__), "static")
		)
		tornado.web.Application.__init__(self, handlers, **settings)

class IndexHandler(RequestHandler):
	def get(self):
		# self.render('index.html', list=todoList)
		greeting = self.get_argument('greeting',None)
		if greeting:
			self.write('hello world!!!!!!!!' + greeting)
		else:
			self.write('hello world!!!!!!!!')

class AddHandler(RequestHandler):
	def post(self):
		listitem = self.get_argument('listitem')
		todoList.append(listitem)
		#self.write('OK')
		self.write(str(todoList))

class GetNewsByIssueHandler(RequestHandler):
	def get(self):
		issueId = self.get_argument('issueId',None)
		if issueId:
			self.write("issueId = " + issueId)
		else:
			self.write("issueId is none")

def main():
	tornado.options.parse_command_line()
	http_server = tornado.httpserver.HTTPServer(Application())
	http_server.listen(os.environ.get("PORT", 5000))

	# start it up
	tornado.ioloop.IOLoop.instance().start()


if __name__ == "__main__":
	main()
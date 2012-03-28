import web
import os
from config import settings


render=settings.render
class hello:
	def GET(self):
		strjson={["id":"1","name":"ptf"],[id":"1",name:"ptf"]}
		return render.hello(strjson)

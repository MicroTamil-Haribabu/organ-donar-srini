from flask import Flask,render_template,session,request,redirect,url_for,flash, make_response
from flask_restful import Resource, Api

app = Flask(__name__, template_folder='templates')
api = Api(app)

data = []
class Root(Resource):
	def get(self):
		headers = {'Content-Type': 'text/html'}
		return make_response(render_template('/home.html'), 200, headers)
	def post(self, name):
		temp = {'Data': name}
		return temp
	def delete(self):
		return {'Note': 'Deleted'}

class Home(Resource):
	def get(self):
		return {'Data': "Hello world"}
	def post(self, name):
		temp = {'Data': name}
		return temp
	def delete(self):
		return {'Note': 'Deleted'}
			
api.add_resource(Root, '/')
api.add_resource(Home, '/home')
if __name__ == '__main__':
	app.run(debug=True)
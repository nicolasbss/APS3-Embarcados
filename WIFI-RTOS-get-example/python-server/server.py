from flask import Flask, request
from flask_restful import Resource, Api, reqparse

app = Flask(__name__)
api = Api(app)

todos = {}

parser = reqparse.RequestParser()
parser.add_argument('valor')


class HelloWorld(Resource):
    def get(self):
        return {'hello':'world'}

#    def get(self, todo_id):
#        return {todo_id: todos[todo_id]}
#
#    def put(self, todo_id):
#        todos[todo_id] = request.form['data']
#        return {todo_id: todos[todo_id]}
    def post(self):
        args = parser.parse_args()
        print(args)
        return {'hello':args['valor']}

#api.add_resource(TodoSimple, '/<string:todo_id>')
api.add_resource(HelloWorld, '/')

if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True)
    #app.run(debug=True)


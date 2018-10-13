from flask import Flask, request
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

data = 0

class doRotation(Resource):
    def get(self):
        bearing = request.args.get('bearing')
        speed = request.args.get('speed')
        data = bearing
        return {
            'bearing': bearing,
            'speed': speed,
            }
class getBearing(Resource):
    def get(self):
        return {
            'bearing': currentBearing,
            }

api.add_resource(doMovement, '/doMovement')
api.add_resource(doRotation, '/doRotation')
api.add_resource(getBearing, '/getBearing')
if __name__ == '__main__':
    app.run(debug=True, port=3002)

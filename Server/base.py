from flask import Flask, request
from flask_restful import Resource, Api, reqparse
from medicaid import Person

app = Flask(__name__)
api = Api(app)

parser = reqparse.RequestParser()
parser.add_argument('rate', type=int, help='Rate cannot be converted')
parser.add_argument('name')
args = parser.parse_args()

class getEligibility(Resource):
    def get(self):
        familySize = request.args.get('familySize')
        state = request.args.get('state')
        income = request.args.get('income')
        pregnancy = request.args.get('pregnancy')
        p1 = Person(familySize, state, income, pregnancy)
        return {
            'familySize': familySize,
            'state': state,
            'income': income,
           'pregnancy': pregnancy,
            'expandedAdult': str(p1.expanded_medicaid_eligibility()),
            'chip': str(p1.chip_eligibility()),
            'PregnantAdult': str(p1.pregnant_eligibility()),
            }
api.add_resource(getEligibility, '/getEligibility')
if __name__ == '__main__':
    app.run(debug=True, port=3011)

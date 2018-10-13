# coding: utf-8
from flask import Flask, request
from flask_restful import Resource, Api, reqparse
from medicaid import Person

app = Flask(__name__)
api = Api(app)



@app.route('/api/add_message/<uuid>', methods=['POST'])
class tierion_post:
    def post(self, uuid):
        '''
        tierion = {
            X-Username: "blurjor@gmail.com"
            X-Api-Key:  "X0dvxIiNXXq5k7RBNYDmPrVoxEeJ+Y+umsUMS7FcgWk"
            client-secret: "aa5438d3159a9b2e82d78c74e44cba8516edbf23"
            datastore id: "1082"
        }
        '''
        content = request.get_json(silent=True)
        return jsonify({"uuid":uuid})


'''
class getBearing(Resource):
    def get(self):
        familySize = request.args.get('familySize')
        state = request.args.get('state')
        income = request.args.get('income')
        pregnancy = request.args.get('pregnancy')
        p1 = Person(int(familySize), state, float(income), int(pregnancy))
        return {
            'familySize': familySize,
            'state': state,
            'income': income,
           'pregnancy': pregnancy,
            'expandedAdult': str(p1.expanded_medicaid_eligibility()),
            'chip': str(p1.chip_eligibility()),
            'PregnantAdult': str(p1.pregnant_eligibility()),
            }
'''

if __name__ == '__main__':
    app.run(debug=True, port=3011)

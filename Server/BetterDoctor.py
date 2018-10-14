const apiKey = require("./../.env").apiKey;
import requests
import JSON

apiKey = 'd3b3bf7b821eed8c53140dad37c3dc23'

class Doctors():
    def_init_ (self, attrubutes):
        this.condition = attributes.condition
        this.speciality = attributes.speciality
        this.practice = attributes.practice
        this.language = attributes.language
        this.insurance = attributes.DoctorInsurancePlan
        this.gender = attributes.gender

    def byCondition(displayDoctors):
        r = requests.get( 'https://api.betterdoctor.com/2016-03-01/conditions?user_key=' + api_key;')
        r.json()

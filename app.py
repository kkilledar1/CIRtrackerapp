#!/usr/bin/env python

import urllib
import json
import os

from flask import Flask
from flask import request
from flask import make_response

# Flask app should start in global layout
app = Flask(__name__)


@app.route('/webhook', methods=['POST'])
def webhook():
    req = request.get_json(silent=True, force=True)

    print("Request:")
    print(json.dumps(req, indent=4))

    res = makeWebhookResult(req)

    res = json.dumps(res, indent=4)
    print(res)
    r = make_response(res)
    r.headers['Content-Type'] = 'application/json'
    return r

def makeWebhookResult(req):
    if req.get("result").get("action") != "CheckCIRstatus":
        return {}
    result = req.get("result")
    parameters = result.get("parameters")
    CIRid = parameters.get("$CIRid")

    #CIRstatus = {'1009':Approved, '500':Cancelled, '901':Implemented, '1276':Analysis, '1999':Request submitted}
    CIRstatus_res = "Approved"

    response= CIRstatus_res
    speech = "The CIR status is " + CIRstatus_res
    print("Response:")
    #print(status)
    print(speech)
    
   # data = result.json()
     
   
    return {
       "speech": speech,
       "displayText": speech,
     #"data": {},
     "contextOut": CIRstatus_res,
     "source": "apiai-CIR-status"
    };
    return response
    #res = makeWebhookResult(data)
    #return res

    #return (JSON.stringify({ "speech": speech, "displayText": response }))
    
if __name__ == '__main__':
    port = int(os.getenv('PORT', 5000))

    #print "Starting app on port %d" % port

    app.run(debug=True, port=port, host='0.0.0.0')

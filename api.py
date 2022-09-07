from bottle import route, run
import json
@route('/mail/a')
def hello():
    return json.dumps({"message": "ptithcm"})

run(host='0.0.0.0', port=5000)

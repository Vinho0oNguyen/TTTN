from bottle import route, run
import json
@route('/mail/a')
def hello():
    return json.dumps({"message": "mail a123123123"})

run(host='0.0.0.0', port=5000)

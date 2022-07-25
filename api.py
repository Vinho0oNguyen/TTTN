from bottle import route, run
import json
@route('/mail/a')
def hello():
    return json.dumps({"message": "hello 12312312vcbcv3"})

run(host='0.0.0.0', port=5000)

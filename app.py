import logging
import sys

import json_logging
import flask


app_name = "app-sample"

app = flask.Flask(app_name)
json_logging.ENABLE_JSON_LOGGING = True
json_logging.ENABLE_JSON_LOGGING_DEBUG = False
json_logging.init_flask()
json_logging.init_request_instrument(app)

# init the logger as usual
logger = logging.getLogger(app_name)
logger.setLevel(logging.INFO)
logger.addHandler(logging.StreamHandler(sys.stdout))


@app.route('/api/v1/sample', methods=['GET', 'POST'])
def sample():
    content = flask.request.json
    logger.info(f"Received message '{content}'")
    return flask.jsonify(result="success")


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=int(8000), use_reloader=False)

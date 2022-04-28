import os

from flask import Flask, request

from utils.file_reader import read_file
from utils.request_reader import parse_request, compile_cmd, methods_iterator

app = Flask(__name__)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, "data")
FILE_DIR = os.path.join(DATA_DIR, "apache_logs.txt")


@app.route("/perform_query")
def perform_query():
    try:
        cmd_list = list(parse_request(request.args))
        if len(cmd_list) == 0:
            return 'BAD request', 400

        result = compile_cmd(cmd_list, read_file(FILE_DIR))

        return app.response_class('\n'.join(result), content_type="text/plain")
    except:
        return 'BAD request', 400


app.run(debug=True)

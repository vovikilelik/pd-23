from typing import Iterable

from flask import Flask, request

from utils.file_reader import read_file, get_file_path
from utils.request_reader import parse_request, compile_cmd, Command
from utils.request_reader_legacy import parse_request_legacy

DEFAULT_FILE_NAME = "apache_logs.txt"

app = Flask(__name__)


def perform_query(commands: Iterable[Command], file_name: str = DEFAULT_FILE_NAME):
    try:
        cmd_list = list(commands)

        if len(cmd_list) == 0:
            return 'BAD request', 400

        result = compile_cmd(cmd_list, read_file(get_file_path(file_name)))

        return app.response_class('\n'.join(result), content_type="text/plain")
    except KeyError:
        return 'BAD request', 400
    except FileNotFoundError:
        return 'File not found', 404


@app.route("/perform_query", methods=['GET'])
def perform_query_get():
    if 'query' in request.args:
        return 'BAD request', 400

    return perform_query(parse_request(request.args['query']), request.args.get('file_name'))


@app.route("/perform_query", methods=['POST'])
def perform_query_post():
    return perform_query(parse_request_legacy(request.form), request.form.get('file_name'))


app.run(debug=True, host='0.0.0.0', port=8080)

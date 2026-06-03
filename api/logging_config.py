import logging, json
class JsonFormatter(logging.Formatter):
    def format(self, record):
        return json.dumps({'level': record.levelname, 'msg': record.getMessage()})

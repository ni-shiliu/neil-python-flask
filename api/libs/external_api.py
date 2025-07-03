from flask_restful import Api


class ExternalApi(Api):
    def __init__(self, blueprint):
        super().__init__(blueprint)
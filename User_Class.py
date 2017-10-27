import Base_Class as bc
import requests as req
import json
import Request_Exception as exp

class User(bc.BaseClient):
    BASE_URL = 'https://api.vk.com/method/'
    method = 'users.get'
    http_method = 'GET'


    def set_params(self, params):
        self.params = params


    def get_params(self):
        return self.params


    def get_json(self):
        return None

    # Отправка запроса к VK API
    def _get_data(self, method, http_method):
        if http_method == 'GET':
            url = self.generate_url(method)
            response = req.get(url, self.params)
        return self.response_handler(response)

    # Обработка ответа от VK API
    def response_handler(self, response):
        ret = None
        try:
            data = json.loads(response.text)
            self.uid = data['response'][0]['uid']
            ret = data['response'][0]
        except:
            raise exp.RequestError('Bad request')
        return ret

    # Запуск клиента
    def execute(self):
        return self._get_data(
            self.method,
            http_method=self.http_method
        )

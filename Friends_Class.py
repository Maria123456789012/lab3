import Base_Class as bc
import requests as req
import json
import Request_Exception as exp
import datetime

class Friends(bc.BaseClient):
    BASE_URL = 'https://api.vk.com/method/'
    method = 'friends.get'
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


    def _get_friends_lst(self, data):
        lst = []
        for item in data:
            if 'bdate' in item and len(item['bdate'].split('.')) == 3:
                date = datetime.datetime.strptime(item['bdate'], '%d.%m.%Y').date()
                today = datetime.date.today()
                delta = today - date
                item['age']  = (delta.days // 365)
                lst.append(item)
        self.friends_list = lst
        return lst

    # Обработка ответа от VK API
    def response_handler(self, response):
        ret = None
        try:
            data = json.loads(response.text)
            #self.uid = data['response'][0]['uid']
            data = data['response']
        except:
            raise exp.RequestError('Bad request')
        else:
            return self._get_friends_lst(data)

    # Запуск клиента
    def execute(self):
        return self._get_data(
            self.method,
            http_method=self.http_method
        )

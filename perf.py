
import time
import logging

from locust import HttpUser, task, between, events,tag

from Auth import auth
from Functional import base

@events.init_command_line_parser.add_listener
def _(parser):
    parser.add_argument("--SuperLogin", type=str, env_var="SuperLogin", default='')
    parser.add_argument("--SuperPass", type=str, env_var="SuperPass", default='')
    parser.add_argument("--ssl_check", type=bool, env_var="ssl_check", default=True)
    parser.add_argument("--access_token", type=str, env_var="ssl_check", default=True)


class FlowException(Exception):
   pass

class LoadTest(HttpUser):
    wait_time = between(1, 3)
    token = ""
    header = None
    login = None
    password = None

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        logging.info(f'Starting test')
        
        #В этом варианте авторизации педполгается, что нам известен токен, который будет использоваться в тесте
        self.token = self.environment.parsed_options.access_token
        self.header = auth.get_http_headers(self.token)
        
        # Блок кода ниже включает авторизцию пользователя. Необходимо раскоментировать его
        # При необходимости поправить функцию Auth/auth.auth()
        # self.login = self.environment.parsed_options.SuperLogin
        # self.password = self.environment.parsed_options.SuperPass
        # 
        # response = None
        # for i in range(0, 60):#Нужно получить начальный токен любыми путями)
        #     response = auth.auth(self)
        #     if response.status_code > 299:
        #         time.sleep(2)
        #     else:
        #         break      
        # 
        # self.token = response.json()["access_token"]
        # 
        # self.header = auth.get_http_headers(self.token)
        # logging.info(f'===== Auth user: {self.login} =====')
        # logging.info(f'Token received: {self.token}')


    @staticmethod
    def logging_response(response):
        """
        Метод логирования полученного ответа метода
        Работает правильно при условии, что в запросе был передан аргумент catch_response=True
        :param response: ответ метода
        :return: None
        :Логирует только ошибки. Позитивные запросы не логируются
        """
        try:
            if int(response.status_code) > 299:
                logging.error(response.status_code)
                logging.error(response.request.path_url)
                logging.error(response.request.headers)
                logging.error(response.request.body)
                logging.error(response.text)
        except (KeyError, AttributeError) as error:
            logging.error(error)
            response.failure(error)

    @staticmethod
    def eventScenario(result):
        if int(result["time_delta"]) == 0:
            return
        events.request.fire(
            request_type="SCENARIO",
            name=result["nameSc"],
            response_time=int(result["time_delta"]),
            response_length=0,
            context=None,
            exception=None,
        )

    
        
    @tag('perfomance_test_overview_page')
    @task (10)
    def perfomance_test_overview_page(self):
        time_start = int(time.time() * 1000)
        base.baseGet(self,'perfomance_test_overview_page','/v3.6/customer/action/get_dynamic_configuration?license_id=13386765&client_id=c5e4f61e1a6c3b1521b541bc5c5a2ac5&url=https%3A%2F%2Fapp.rivo.xyz%2F&channel_type=code&jsonp=__xjaeby1z6x')
        base.baseGet(self,'perfomance_test_overview_page','/v3.4/customer/action/get_configuration?organization_id=eb1cd399-e620-4126-933c-5dc5dc3b1363&version=1338.0.11.486.102.131.94.17.4.1.3.13.1&group_id=8&jsonp=__lc_static_config')
        base.baseGet(self,'perfomance_test_overview_page','/v1/chain/ARB/strategy/0x57c817253E0ee2B260468e81628BC6Ccdd67C23f/current_apy')
        base.baseGet(self,'perfomance_test_overview_page','/v1/chain/ARB/strategy/0xC4E7d7c15b8F5c2D77512460b84802D1D3693692/current_apy')
        base.baseGet(self,'perfomance_test_overview_page','/v1/chain/BASE/strategy/0x395F4A621dD51B120ECe2152f45C315bb14799a0/current_apy')
        base.baseGet(self,'perfomance_test_overview_page','/v1/chain/ARB/strategy/0x42189C0588Bf73a449D619794C2eB409c2554456/current_apy')
        base.baseGet(self,'perfomance_test_overview_page','/v1/chain/ARB/strategy/0x7f29df2B1fb1643186D9110066758cEffdCA90D7/current_apy')
        base.baseGet(self,'perfomance_test_overview_page','/v1/chain/ARB/strategy/0xe10d82Ca259853A2E4f2E9Fc78C316A00388147c/current_apy')
        base.baseGet(self,'perfomance_test_overview_page','/v3.4/customer/action/get_localization?organization_id=eb1cd399-e620-4126-933c-5dc5dc3b1363&version=470b74842e9d45ce9f156d1d5a957bad_2c138679d8258ed70b2379fb4fe17583&language=en&group_id=8&jsonp=__lc_localization')
        base.baseGet(self,'perfomance_test_overview_page','/v1/chain/ETH/strategy/0x854F178112008143014ECffd4059e3f913a47B40/current_apy')
        base.baseGet(self,'perfomance_test_overview_page','/v1/chain/ETH/strategy/0xF99302d3d4a30D2AC26B4f8E0390171b29D5f547/current_apy')
        base.baseGet(self,'perfomance_test_overview_page','/v1/chain/ETH/strategy/0xCaA70cC97165D8168E3DA7A99f6430D64e2f09A1/current_apy')
        base.baseGet(self,'perfomance_test_overview_page','/v1/chain/ETH/strategy/0xf12c92cBe97F16cFB8Dc007545C29A55912177fE/current_apy')
        base.baseGet(self,'perfomance_test_overview_page','/v1/chain/ETH/strategy/0x4A8a7539AD59c277C1915c3938D2b0c15CD0ee97/current_apy')
        base.baseGet(self,'perfomance_test_overview_page','/v1/chain/ARB/strategy/0xBf8181f3b5E71fa0CbBE1e067f408a9a0558C60f/current_apy')
        base.baseGet(self,'perfomance_test_overview_page','/v1/chain/ARB/strategy/0xa7eb4efe088A3618C9BA21e1520E0c8460b42D37/current_apy')
        base.baseGet(self,'perfomance_test_overview_page','/v1/chain/ARB/strategy/0xB0a66dD3B92293E5DC946B47922C6Ca9De464649/current_apy')
        result = {}
        result["nameSc"] = "perfomance_test_overview_page"
        time_end = int(time.time() * 1000)
        time_delta = (time_end - time_start)
        result["time_delta"] = time_delta
        self.eventScenario(result)
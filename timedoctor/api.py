from typing import Dict
from requests import Session
from datetime import datetime
from timedoctor.utils import get_date_past_days, convert_timestamp_to_hour

class Client:
    API_ENDPOINT = 'https://api2.timedoctor.com/api/1.0/'

    def __init__(self , email: str = None , password: str = None):
        if email == None or password == None:
            raise Exception('Please provide email and password')
        # Credentials
        self.email: str = email
        self.password: str = password

        self.id: str = None
        self.name: str = None
        self.timezone: str = None
        self.token: str = None
        self.company_id: str = None
        self.headers: Dict[str, str] = {
            'Accept': 'application/json, text/plain, */*',
            'Content-Type': 'application/json',
            'Connection': 'keep-alive',
            'Host': 'api2.timedoctor.com',
            'Origin': 'https://2.timedoctor.com',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site':'same-site',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36'
        }

        self.session: dict = Session()
        self.session.headers.update(self.headers)


    def login(self) -> bool:
        """Log in to the server

        Returns:
            bool: loggedIn
        """

        if self.email != None and self.password != None:
            login_response = self.session.post(
                url = self.API_ENDPOINT+'authorization/login?no-workspaces=1&has-managed-screencasts=1',
                json = {
                    'email':self.email,
                    'password': self.password
                })
            
            if login_response.status_code == 200:
                json_data: dict = login_response.json()['data']

                self.id = json_data['id']
                self.name = json_data['name']
                self.timezone = json_data['timezone']
                self.token = json_data['token']
                self.company_id = json_data['companies'][0]['id']

                return True

        return False

    def get_time(self, date_from:str = get_date_past_days(30), date_to:str = get_date_past_days(0)) -> dict:
        """get_time

        Args:
            date_from (str, optional): ISO Datetime. Defaults to get_date_past_days(30).
            date_to (str, optional): ISO Datetime. Defaults to get_date_past_days(0).

        Returns:
            dict: JSON Response
        """
        params: Dict[str, str] = {
                'user':'',
                'from': date_from,
                'to': date_to,
                'timezone': self.timezone,
                'limit':'10000',
                'group-by': 'company',
                'page': '0',
                'token': self.token,
                'company': self.company_id
            }

        if self.email != None and self.password != None:
            response = self.session.get(
                url = self.API_ENDPOINT+'stats/summary-ratio',
                params=params
            )
            return response.json()['data']['users'][0]
        raise Exception('No Token, Please Log in')

    def parse_summary(self, data:dict = {}) -> Dict[str,str]:
        """Parsing summary response to valid datetime value

        Args:
            data (dict, optional): json response from summary API. Defaults to {}.

        Returns:
            Dict[str,str]: Parsed data
        """
        return {
            'total':convert_timestamp_to_hour(data['total']),
            'productive_time':convert_timestamp_to_hour(data['prod']),
            'neutral_time':convert_timestamp_to_hour(data['neutral']),
            'unproductive_time':convert_timestamp_to_hour(data['unprod']),
            'manual_time':convert_timestamp_to_hour(data['manual'])
        }
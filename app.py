from timedoctor.api import Client
from settings import TIMEDOCTOR_EMAIL, TIMEDOCTOR_PASSWORD

timedoctor = Client(
    email = TIMEDOCTOR_EMAIL,
    password = TIMEDOCTOR_PASSWORD
) 

timedoctor.login()
data = timedoctor.get_time()
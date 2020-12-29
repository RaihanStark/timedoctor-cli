from timedoctor.api import Client
from timedoctor.utils import convert_timestamp_to_hour
from settings import TIMEDOCTOR_EMAIL, TIMEDOCTOR_PASSWORD

from colored import fg, bg, attr

print ('%s%sTimedoctor CLI%s' % (fg(231),bg(12), attr(0)))

timedoctor = Client(
    email = TIMEDOCTOR_EMAIL,
    password = TIMEDOCTOR_PASSWORD
) 

timedoctor.login()
data = timedoctor.get_time()
total = timedoctor.parse_summary(data)['total']

print ('You worked for ' + '%s%s%s%s' % (fg(231),bg(4),total, attr(0)))
# print ('You should be paid with ' + '%s%s$62%s' % (fg(231),bg(2), attr(0)))
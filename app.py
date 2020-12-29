from timedoctor.api import Client
from timedoctor.utils import convert_timestamp_to_hour
from settings import TIMEDOCTOR_EMAIL, TIMEDOCTOR_PASSWORD

from colored import fg, bg, attr

print ('%s%sTimedoctor CLI%s' % (fg(231),bg(12), attr(0)))

RATE_PER_HOUR = 2.5

timedoctor = Client(
    email = TIMEDOCTOR_EMAIL,
    password = TIMEDOCTOR_PASSWORD
) 

# Getting Hours
timedoctor.login()
data = timedoctor.get_time()
total = timedoctor.parse_summary(data)['total']

# Getting Rate
total_worked_hours = int(total.split('h')[0])
salary = RATE_PER_HOUR * total_worked_hours



print ('You worked for ' + '%s%s%s%s' % (fg(231),bg(4),total, attr(0)) + ' this week')
print ('You should be paid ' + '%s%s$%s%s' % (fg(231),bg(2),salary, attr(0)) + ' from $2.5/hr')
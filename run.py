from plyer import notification
from datetime import datetime, timedelta
import requests
import time


while (True):

    yesterday = (datetime.now() - timedelta(1)).strftime('%Y-%m-%d')
    day_before_yesterday = (datetime.now() - timedelta(2)).strftime('%Y-%m-%d')


    request = "https://api.covid19api.com/country/saudi-arabia/status/confirmed?from={}T00:00:00Z&to={}T00:00:00Z"
    request = request.format(day_before_yesterday, yesterday)


    get_data = requests.get(request)

    cases = get_data.json()[1]['Cases']

    message = "Yesterday confirmed cases: {}"
    message = message.format(cases)

    notification.notify(title='Covid19 notifier', message=message, app_name='Covid19 notifier',  timeout=10)

    time.sleep(15) #time.sleep(60*60*24)
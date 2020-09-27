import datetime
import pandas as pd
dt_now = str(datetime.datetime.now().strftime('%Y%m%d-%H%M%S'))

df = pd.DataFrame(
    [[dt_now, "maitatomoya", "Hello cron"]],
    columns = ['datetime', 'name', 'greet'])

df.to_csv('/Users/maitatomoya/Desktop/PG/Program_Python/e_python/python-cron/test_'+dt_now+'.csv')
print(dt_now, ' Hello world from cron')

import sql
from faker import Faker
import random
import string

fake = Faker()
db = sql.Database()
values = ''

for i in range(100000):
  user_id = ''.join(random.choices(string.ascii_uppercase + string.digits, k=50))
  create_time = fake.date_time_between(start_date='-30d', end_date='now')
  values += '("%s","%s"),'%(user_id,create_time)

values = values[:-1]

sql = 'insert into test1(c_user_id,create_time) values%s;'%values
db.run_query(sql)

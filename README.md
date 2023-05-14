# mysql-testdata-py
This repo is help to generate fake data insert into MySQL table.

## Install
```
cd mysql-testdata-py
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Run

1. export MySQL env
```
export host=x.x.x.x
export user=mysql_user
export password=mysql_password
export db=mysql_db
```

2. modify parameters

open main.py, modify sql

3. run
```
python main.py
```
![image](https://github.com/hellof20/mysql-testdata-py/assets/8756642/fb42e15f-0ae8-421d-8606-3508afc9ba5a)


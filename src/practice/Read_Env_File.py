from dotenv import load_dotenv,find_dotenv
#find automatically .env directory
dotenv_path = find_dotenv()
#load the .env file
load_dotenv(dotenv_path)

#extracting evn variable using os.environ.get method
import os
import requests
from requests import session
#user_name = os.environ.get("KAGGLE_USERNAME")
payload = {
        'action' : "login",
        'username' : os.environ.get("KAGGLE_USERNAME"),
        'password' : os.environ.get("KAGGLE_PASSWORD")
}
print(os.environ.get("KAGGLE_USERNAME"))
print(os.environ.get("KAGGLE_PASSWORD"))
train_url='https://www.kaggle.com/c/titanic/download/train.csv'
with session() as c:
    c.post('https://www.kaggle.com/account/login', data=payload)
    response = c.get(train_url)
    print(response.text)


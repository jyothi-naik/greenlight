import os
import requests
from bs4 import BeautifulSoup

payload = {'j_username': os.environ.get('user'), 'j_password': os.environ.get('pass')}


session = requests.Session()
p = session.post("https://analysiscenter.veracode.com/j_security_check", payload)
temp_cookies = requests.utils.dict_from_cookiejar(session.cookies)
cookievalue = temp_cookies.get('JSESSIONID')
cookie = {'JSESSIONID':cookievalue}

soup = BeautifulSoup(p.content,"html.parser")
findingcsrf=soup.findAll('script')[103].string
tmpcsrf=(findingcsrf[109:230])
csrf1=tmpcsrf.rsplit('"',1)[0]

headers = {'Content-Type': 'application/x-www-form-urlencoded','Accept': 'application/json'}
url1 = requests.post('https://analysiscenter.veracode.com/auth/acctadmin/apicredentialsgenerator/generateNewCredentials.veracode', data=csrf1, headers=headers, cookies=cookie)

api_data = url1.text
print (api_data)
print (api_data[2:42])
print (api_data[45:185])
 


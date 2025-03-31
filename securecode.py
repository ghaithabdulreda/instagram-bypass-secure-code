from requests import session
from time import sleep, time
from random import choice
from sys import argv
s=session()

import requests
cookies = [

'dpr=2.200000047683716; csrftoken=PahemtL0Ar5Q86sZKybN3a; datr=7ec4Z9DqBP9Crn59VCJDnlum; ig_did=C142587F-04AD-4683-9186-5D9FBF9A2E36; wd=1309x707; mid=ZXY0MAAEAAHycZ52UagKbiWFHQY4;']

cookie = choice(cookies)
xCsrftoken = cookie.split("csrftoken=")[1].split(";")[0].strip()


headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Accept": "*/*",
    "Referer": "https://www.instagram.com/",
    "Accept-Language": "en-US,en;q=0.9,ar;q=0.8",
    "X-Requested-With": "XMLHttpRequest",
    "X-Csrftoken": xCsrftoken,
    "Cookie": cookie
}

user = input("USER: ")
#user = argv[1]
#passwd = argv[2]
#email = argv[3]
passwd = input("PASSWD: ")
email = input("EMAIL: ")
t = int(time() * 1000)
data = {
    "enc_password": f"#PWD_INSTAGRAM_BROWSER:0:{t}:{passwd}",
    "caaF2DebugGroup": "0",
    "loginAttemptSubmissionCount": "0",
    "optIntoOneTap": "false",
    "queryParams": "{}",
    "trustedDeviceRecords": "{}",
    "username": user,
}
print(data)


def login():
        a = s.post('https://www.instagram.com/api/v1/web/accounts/login/ajax/', data=data, headers=headers)
        print(a.json())
        return a.json()['checkpoint_url']
checkpoint_url = login()

# checkpoint_url = '/challenge/action/AXFEaC1DAg95qpoiCOVAEig80m_K0QAE8OFbtsixyh8QAqmHwVfelusgzdt-HQ_Sl36n6w/Afw0xFDlnML7IxOWnYmp9j8qf0xvpmBGbZOiA9tQDLv9yPmmZVnU42KWlXW4Gi59F4bNNTwXQJkBBg/ffc_mE0kAbgvX17w6pP5gIw2RlpY6wqpiCZK7HllhtChoXgh7BVRUUl6fgKNkdCXVEwY/'
# print(checkpoint_url)

headers={
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
        'Accept': '*/*',
        'Accept-Language': 'en-US,en;q=0.9,ar;q=0.8',
        'X-Requested-With': 'XMLHttpRequest',
        "X-Csrftoken": xCsrftoken,
        "Cookie": cookie
}
if 'https://i.instagram.com' in checkpoint_url:
	checkpoint_url = checkpoint_url.replace('https://i.instagram.com','')
print(checkpoint_url)
a = s.get(f'https://i.instagram.com{checkpoint_url}', headers=headers)
print(a.text)
challenge_context = a.text.split('"challenge_context":"')[1].split('"')[0]
# print(challenge_context)

# exit()

headers = {
    "Host": "www.instagram.com",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.6723.70 Safari/537.36",
    "Accept": "*/*",
    "Cookie": cookie,
    "X-Csrftoken": xCsrftoken,
    "X-Bloks-Version-Id": "09d4437a3b9f5707ed0adf4614de5f4d546124576e17ba49716eb9823d803aea",
}

data = {
    "choice": "2",
    "is_bloks_web": "false",
    "challenge_context": challenge_context,
    "has_follow_up_screens": "false",
    "nest_data_manifest": "true",
}

a = s.post('https://www.instagram.com/api/v1/bloks/apps/com.instagram.challenge.navigation.take_challenge/', data=data, headers=headers)

# print(a.text)



# exit()
################################################


def sendCode(challenge_context):
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.6723.70 Safari/537.36",
            "Cookie": cookie,
            "X-Csrftoken": xCsrftoken,
            "X-Bloks-Version-Id": "09d4437a3b9f5707ed0adf4614de5f4d546124576e17ba49716eb9823d803aea",
        }
        data = {
            "has_follow_up_screens": "0",
            "account_type": "personal_with_photo",
            "user_submitted_contact_email": email,
            "challenge_context": challenge_context,
            "has_follow_up_screens": "false",
            "nest_data_manifest": "true",
        }
        a = s.post('https://www.instagram.com/api/v1/bloks/apps/com.instagram.challenge.navigation.take_challenge/', data=data, headers=headers)
        print(a.text)
sendCode(challenge_context)

sendCode(challenge_context)



def checkCode(challenge_context, code):
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.6723.70 Safari/537.36",
            "Cookie": cookie,
            "X-Csrftoken": xCsrftoken,
            "X-Bloks-Version-Id": "09d4437a3b9f5707ed0adf4614de5f4d546124576e17ba49716eb9823d803aea",
        }
        data = {
            "choice": "2",
            "security_code": code,
            "is_bloks_web": "False",
            "has_follow_up_screens": "0",
            "challenge_context": challenge_context,
            "has_follow_up_screens": "false",
            "nest_data_manifest": "true",
        }
        a = s.post('https://www.instagram.com/api/v1/bloks/apps/com.instagram.challenge.navigation.take_challenge/', data=data, headers=headers)
        # print(a.text)
print(f"Code has been send to your email {email}")
code = input("CODE: ")
for x in range(1,5):
        checkCode(challenge_context, code)

def getUserData(checkpoint_url):
        headers={
                'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
                'Accept': '*/*',
                'Accept-Language': 'en-US,en;q=0.9,ar;q=0.8',
                'X-Requested-With': 'XMLHttpRequest',
                "X-Csrftoken": xCsrftoken,
                "Cookie": cookie
        }
        a = s.get(f'https://i.instagram.com{checkpoint_url}', headers=headers)
        # print(a.text)
        if ',"email":"' in a.text:
                print("user: ", a.text.split('"username":"')[1].split('"')[0])
                print("email: ", a.text.split(',"email":"')[1].split('"')[0])
                print("trusted_email: ", a.text.split('"trusted_email":"')[1].split('"')[0])
                print("user_submitted_contact_email: ", a.text.split('"user_submitted_contact_email":"')[1].split('"')[0])
                print("trusted_phone_number: ", a.text.split('"trusted_phone_number":"')[1].split('"')[0])
                print("trusted_phone_number_origin: ", a.text.split('"trusted_phone_number_origin":"')[1].split('"')[0])




getUserData(checkpoint_url)

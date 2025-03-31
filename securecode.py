from requests import session
from time import sleep, time
from random import choice
from sys import argv
s=session()

import requests
cookies = [

'dpr=2.200000047683716; csrftoken=PahemtL0Ar5Q86sZKybN3a; datr=7ec4Z9DqBP9Crn59VCJDnlum; ig_did=C142587F-04AD-4683-9186-5D9FBF9A2E36; wd=1309x707; mid=ZXY0MAAEAAHycZ52UagKbiWFHQY4;',
'dpr=2.200000047683716; csrftoken=EvYxvyEmSRfX389UZ-UiVn; datr=7uc4Z9DjHOcC5OZRTnb3-6Dm; ig_did=A05781C7-FCE1-469F-A8AC-CB04422B49A8; wd=1309x707; mid=ZXY0HQAEAAHTVRjTyU_Uc3WQXRdH;',
'dpr=2.200000047683716; csrftoken=pB47RAafX5vbWtyHZg-1Bz; datr=7uc4Z6jayw0ng1qF7-pgHB-J; ig_did=F026A90A-6009-4A61-8724-C05B4102EFAB; wd=1309x707; mid=ZXY0IQAEAAGzGbNxmIeTe23Nk9I3;',
'dpr=2.200000047683716; csrftoken=q10XMIqItISjYgA8m7iW-2; datr=7-c4Z70d7KYLh9sNUwnY5vTZ; ig_did=3ECC0007-EF54-4786-B446-19D58296DC86; wd=1309x707; mid=ZXY0RQAEAAFnwrcOh-NrH-TgqHUa;',
'dpr=2.200000047683716; csrftoken=FcozblxVzb4oKTgpW203vE; datr=7-c4Zwrw6ycGjBm6gR-1zvKR; ig_did=5D7D15A5-742C-48FD-911D-85854F461B08; wd=1309x707; mid=ZXY0FwAEAAHRwh_W7NXK8TScPiic;',
'dpr=2.200000047683716; csrftoken=9IUrANWq_XzVScY9Au-5G1; datr=8Oc4Z0b9eC0pqXeGh552m8SV; ig_did=ABD5F97D-6217-450C-B955-08E44E343443; wd=1309x707; mid=ZXY0RgAEAAHfydwYD2SS4v41IYMD;',
'dpr=2.200000047683716; csrftoken=zCVq5C24wSbU1kNwyLGBLi; datr=8ec4ZwIIrvzXRnujrKsOUrhb; ig_did=58C90F91-F989-4DA6-B569-7E395727186B; wd=1309x707; mid=ZXY0LAAEAAGtvA9Ss-VgqKqmimYY;',
'dpr=2.200000047683716; csrftoken=46CwnovX4mlxEe4MQRB-0n; datr=8ec4ZxZ8SdgbiaPH-3eZUDPj; ig_did=0F11A322-3349-4090-B18F-34A054BA84BA; wd=1309x707; mid=ZXY0IQAEAAEmpMHN8exJsf3Pr9VW;',
'dpr=2.200000047683716; csrftoken=irMsJFwiUVSdTIYYQt-nTw; datr=8uc4Z7_j7MyrCEJ_DdB27xYb; ig_did=F10EB4A0-5B24-4448-8D8E-8C3007B36BCD; wd=1309x707; mid=ZXY0HQAEAAHXvU9EkYks9k9pmqoY;',
'dpr=2.200000047683716; csrftoken=7qwBfHn8xa8Gk3IkrGRdcB; datr=8uc4Z8O8yPvOhx2Jpg9AYfCN; ig_did=76637093-1A86-42BF-895A-0E485D511C2B; wd=1309x707; mid=ZXY0HAAEAAE2HcrjBytolNvn9DF4;',
'dpr=2.200000047683716; csrftoken=eFaxbAZWbBofJgA3cKKKIB; datr=8-c4Z0As4BG3HKkj9miNCTuj; ig_did=3FE91A54-EDA2-49CC-8A4D-201A3E41CAD0; wd=1309x707; mid=ZXY0JwAEAAH7m4rdc-P2FPIcXShW;',
'dpr=2.200000047683716; csrftoken=LQDVhwrT7ln3Kxwimvv1Nu; datr=8-c4Z3RDfIO4nPjW7y0rGbcP; ig_did=6D280F84-55A2-4824-85AC-00AEADB2397B; wd=1309x707; mid=ZXY0FAAEAAGXxxU14hWDxcOQzkhY;',
'dpr=2.200000047683716; csrftoken=womNSUXfUIbk-KhlSzdCbD; datr=9Oc4Z8pOsShsgko3kuMm-oAM; ig_did=9540CB9A-C0CA-4A02-BACD-266D70904FCC; wd=1309x707; mid=ZXY0GgAEAAF7NRQhYCvu8_oeh06f;',
'dpr=2.200000047683716; csrftoken=FYqS0ij-lUQ114snchSNbP; datr=9ec4Z5I_qpU6bS7a15aZbT4r; ig_did=FB67E028-F697-4AD0-91A7-3D0919585638; wd=1309x707; mid=ZXY0JQAEAAEbBV496zPfoyjwfibz;',
'dpr=2.200000047683716; csrftoken=aCKmPujApzzS0VmjmV7pTv; datr=9uc4Z4xYZNMhyKR0kaEdDoDL; ig_did=48BB42E6-BC5E-48C4-A15F-2ECBE38EBCD1; wd=1309x707; mid=ZXY0LQAEAAFTY7BDGBa2oDkcHGqD;',
'dpr=2.200000047683716; csrftoken=LL_Ss-Gcz40OOxoqfWIBFo; datr=9uc4Z4aR3rBp8t-UBbWrHo4l; ig_did=A1C687D9-8D75-4114-AE94-3C9D80A20AFE; wd=1309x707; mid=ZXY0GwAEAAGm3HhcVjRzL0QY7PVd;',
'dpr=2.200000047683716; csrftoken=pAq2iekMccWY6wcr_VrZLd; datr=9-c4Z3HaHEblBTw7l1fPS4im; ig_did=E7A53BF8-DBC7-4983-9B1A-B042786270FE; wd=1309x707; mid=ZXY0GwAEAAHtQafVYw-Ojswhk7rF;',
'dpr=2.200000047683716; csrftoken=4akC_jwJPOiMaNNIv9cwUU; datr=9-c4Z7ffSYhYVqoAG-PoMKMX; ig_did=4E237227-3A27-445D-AC8E-F4F2F8E10C60; wd=1309x707; mid=ZXY0GgAEAAGY0E41glB_KSrt5uJG;',
'dpr=2.200000047683716; csrftoken=BYYy7fznM3_x7eQP1adVjC; datr=-Oc4Z-m4lay7DX0BVZ-Xn_Tu; ig_did=2E119CBC-7053-466F-BDE1-9F27D40C7532; wd=1309x707; mid=ZXY0TAAEAAFb6AYVfUi8Hg70cL0O;',
'dpr=2.200000047683716; csrftoken=v44oeJrvTfWXXC81AgQcjx; datr=-ec4ZxxVjDgLdT4f7ari-euU; ig_did=6AD3784F-332E-4005-A76C-7C6A05192AAE; wd=1309x707; mid=ZXY0GwAEAAHOuSvSE3ziWqCfX4vN;',
'dpr=2.200000047683716; csrftoken=X2W0WSEYFfwDJIjxmpUg8U; datr=-ec4Zy2E8IseXJuf6QaemShK; ig_did=50E1BF20-54B1-4B24-9BB2-D400330473C6; wd=1309x707; mid=ZXY0TQAEAAELbFPqVn4WOEFHq6LR;',
'dpr=2.200000047683716; csrftoken=yLex5F-A8wHx6uayZUdh8B; datr=-uc4Zx99ldAppghKmv4NZyRQ; ig_did=1291B162-814B-433C-A1F6-320690E2FC11; wd=1309x707; mid=ZXY0GwAEAAG32YyYhmgVXc61OeUo;',
'dpr=2.200000047683716; csrftoken=dVq7kQGbW44beOjWEIfhdg; datr=-uc4Z6yLdSS0r7ZoJYbhf0LQ; ig_did=B418299F-4545-4AB4-A3C2-D8D7A75B7042; wd=1309x707; mid=ZXY0JgAEAAFXDOMl5WbP4hHDm4T9;',
'dpr=2.200000047683716; csrftoken=rlvDWK-tuC0RqobozbpztR; datr=--c4Z5rLc_Sgh6nM76D35OnA; ig_did=593BE107-DBAA-40F7-99D6-E602CC43D81D; wd=1309x707; mid=ZXY0HAAEAAG5nvpd0typexoiuoqf;',
'dpr=2.200000047683716; csrftoken=A-XU9upUr-g4a8dZCdSX0q; datr=_Oc4Z6fULD9fdhsgSNm5ywt1; ig_did=2F9C61AE-B71A-407A-99E6-B27770F0F2C5; wd=1309x707; mid=ZXY0PQAEAAFdi4W1Z3HWV8MwjQVj;',
'dpr=2.200000047683716; csrftoken=nQE5pDWb-SQblhqsY8H4qn; datr=_Oc4Z1RSSL4aMUtQS3t3sP-g; ig_did=387E1ADA-4391-4F8E-A9D1-E24B6309998A; wd=1309x707; mid=ZXY0IAAEAAH3vydSosvsFL0hQA_w;',
'dpr=2.200000047683716; csrftoken=79rMkmJT9EPIDYx8bUicOV; datr=_ec4Z7dI5kJjrROtZBaAq09e; ig_did=9183D7F0-E2A2-41E8-ABA3-1A0D92D7548D; wd=1309x707; mid=ZXY0JAAEAAFPDjKHpmdT8Yp7YLo-;',
'dpr=2.200000047683716; csrftoken=x54Cpr_MkvXOkSTTfxEO93; datr=_uc4Z3fME6AuYFsVvoqVornG; ig_did=0EFBDBC4-A0C7-44C8-A2BE-33D141B42B00; wd=1309x707; mid=ZXY0NwAEAAGWve-B7jTkE-ydZGrG;',
'dpr=2.200000047683716; csrftoken=RGf7rPylYdir3pVL55z_hT; datr=_-c4Z2JOISJ789LW7Z11Ze_J; ig_did=27876EDD-6FB7-44BA-A9C9-E81FEC80C0B5; wd=1309x707; mid=ZXY0FAAEAAEqBEhvfeVf5HYyUs5m;',
'dpr=2.200000047683716; csrftoken=xJP9Zja0VaWBQq5Yp5eduP; datr=_-c4Z7SkaM2wOUtySCKd6rpe; ig_did=CA4ABBD1-AC7E-4C57-975D-F6A84C27B56A; wd=1309x707; mid=ZXY0TgAEAAESs38kQb8wYKIyvEqf;',
'dpr=2.200000047683716; csrftoken=pAWuUxwmphDsBKKwVEEV0h; datr=AOg4Zzc02gUqR0VdOVjvSKJ-; ig_did=48EBBDAA-42FA-4B0A-ACB8-AEF8E8063D92; wd=1309x707; mid=ZXY0JgAEAAHjjk6_x2l79daFioL0;',
'dpr=2.200000047683716; csrftoken=Cdq5yEVhv-2qUXErb285k3; datr=Aeg4Z97OpkwXo1zBgRHZ5bfT; ig_did=EB236010-8B11-4765-A6AE-04C97F9F822E; wd=1309x707; mid=ZXY0GwAEAAGPELCod2qh3l2NGlNT;',
'dpr=2.200000047683716; csrftoken=tOotZckjGjJ20cBCu4UZ5w; datr=Aeg4Z_r4pm9iL_mS74v8C0Qw; ig_did=7B3FF627-2E8C-4C82-BC97-E2325703D50C; wd=1309x707; mid=ZXY0HQAEAAEf7SWug1rjVYP5Sa9F;',
'dpr=2.200000047683716; csrftoken=UxjzH58a_Op1YqxbJh9gS4; datr=Aug4Z0Pvgm1sLv9LPSiTOS7A; ig_did=F114C9EE-6676-4576-A35F-2EAD0E0B8F8F; wd=1309x707; mid=ZXY0TgAEAAEdYHsrHmk1fQy92bx3;',
'dpr=2.200000047683716; csrftoken=ELyrQHkCF03mRO9m0Dik4M; datr=Aug4ZyE1oN3Ao-ordJeCx5ZE; ig_did=88B10B27-E303-4DBC-9AA2-905386407DED; wd=1309x707; mid=ZXY0LAAEAAFnZKik3yF8qZym8EhS;',
'dpr=2.200000047683716; csrftoken=_mm88LtKepk4B643stnfmy; datr=A-g4Z1KZHszNYr0EmOmBg7X8; ig_did=8C870578-5277-4A0A-8282-A4DF55DF1ADD; wd=1309x707; mid=ZXY0KQAEAAERaxjsCtXaLaAqTG5q;',
'dpr=2.200000047683716; csrftoken=N-FPuaD9R8qCmb6_2ERdTL; datr=BOg4Z4ct03sqJyEYexWFlYO4; ig_did=0E4E05ED-FFD3-4FB9-95B4-02D2FB88B183; wd=1309x707; mid=ZXY0OAAEAAE53owLM3eCcDtufb5w;',
'dpr=2.200000047683716; csrftoken=SRNzg0Q0EwYNm5HCUOcxm9; datr=BOg4ZwRhBoasTT7cCE_KZjhA; ig_did=BDB62F35-0A27-42C8-AE2C-FC093A8A7A76; wd=1309x707; mid=ZXY0HwAEAAES6cUyttH3zosSjAcg;',
'dpr=2.200000047683716; csrftoken=lbsWjTv1kPHas_vivV8xoM; datr=Beg4Z_ZL-cljExAhpDPa0yd4; ig_did=0A87BB7E-FCDC-45B2-A022-D682CEEB539E; wd=1309x707; mid=ZXY0MwAEAAF95xZq2BmQ4dC2PYTU;',
'dpr=2.200000047683716; csrftoken=FE5wV0Tjuhi-sUA5zSpEKj; datr=Bug4Z34WOlY3RmPnNsiACsG4; ig_did=00B79623-746A-4FF7-8D7F-1D418AA197AD; wd=1309x707; mid=ZXY0EgAEAAF8bq9kPuNonR_wYxir;',
'dpr=2.200000047683716; csrftoken=VoqDIHwzASIbvbGMnPqWq-; datr=Bug4Z0hSQiIxxV9ORi1-A7Me; ig_did=CFB2FC3F-F21E-4D4F-B01C-ABBA0A945662; wd=1309x707; mid=ZXY0FgAEAAHnBOPIEuuf8pYRaWMS;',
'dpr=2.200000047683716; csrftoken=b1qsln8ttByHEqYbMLaGfE; datr=B-g4Z4Xpjayr-pdjwSgljxCq; ig_did=4CAD2828-1B93-41B7-BEBE-548E4E05484E; wd=1309x707; mid=ZXY0MAAEAAEOD2f5iJzw_J4HU309;',
'dpr=2.200000047683716; csrftoken=SPH24FCcOIwFJwiI2jst1g; datr=COg4Z0SzLqpd2kg4hONXohQW; ig_did=FDBE5EFB-8C98-418F-A4B8-5688275AB011; wd=1309x707; mid=ZXY0TQAEAAHu9kvRct1yarVAx4xj;',
'dpr=2.200000047683716; csrftoken=xcMaUR0I2hbGeMYHV4SNp-; datr=COg4Z5Gtz8WH7bfGDtduMG5T; ig_did=640E8B66-74FC-417F-A6A0-914C73924A4B; wd=1309x707; mid=ZXY0MAAEAAE734zsnRp5XLTkriz5;',
'dpr=2.200000047683716; csrftoken=EeLoxIhC35RL-tuQrmhgoC; datr=Ceg4Zwo3Xu5CjRVi6gvVrq5O; ig_did=B66C2474-8466-4D3D-8E61-F1E53FE9F0CA; wd=1309x707; mid=ZXY0JgAEAAHEguWJGI2E-pL9rqyv;',
'dpr=2.200000047683716; csrftoken=x_Nomy-vporkAs2k4f3IQu; datr=Cug4Z1ujlFIWnAgzEA3_oUwf; ig_did=6CD9E2E8-C928-4E5C-8D03-208A5B3C7515; wd=1309x707; mid=ZXY0RQAEAAEUJ83uL3VuE2CbjmYR;',
]

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

# user = input("USER: ")
user = argv[1]
passwd = argv[2]
email = argv[3]
# passwd = input("PASSWD: ")
# email = input("EMAIL: ")
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

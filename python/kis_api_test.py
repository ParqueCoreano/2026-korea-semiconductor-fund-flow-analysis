import os
import requests
from dotenv import load_dotenv


# Load .env file (.env 파일 불러오기)
load_dotenv()


# Read environment variables (환경변수 읽기)
APP_KEY = os.getenv("KIS_APP_KEY")
APP_SECRET = os.getenv("KIS_APP_SECRET")

BASE_URL = os.getenv(
    "KIS_BASE_URL",
    "https://openapi.koreainvestment.com:9443"
)


print("=" * 60)
print("KIS API TEST")
print("=" * 60)


# Check environment variables (환경변수 확인)
if not APP_KEY:
    raise ValueError("KIS_APP_KEY is missing. (KIS_APP_KEY가 없습니다.)")

if not APP_SECRET:
    raise ValueError("KIS_APP_SECRET is missing. (KIS_APP_SECRET가 없습니다.)")


print("APP KEY: Loaded")
print("APP SECRET: Loaded")


# Access Token 발급
url = BASE_URL + "/oauth2/tokenP"


headers = {
    "content-type": "application/json"
}


body = {
    "grant_type": "client_credentials",
    "appkey": APP_KEY,
    "appsecret": APP_SECRET
}


print("\nRequesting Access Token...")


response = requests.post(
    url,
    headers=headers,
    json=body,
    timeout=10
)


print("\nHTTP Status:", response.status_code)


if response.status_code != 200:
    print("Token issuance failed (Token 발급 실패)")
    print(response.text)
    response.raise_for_status()


data = response.json()


print("\nToken issuance successful!(Token 발급 성공!)")
print("Token Expiration:")
print(data.get("access_token_token_expired"))


print("\nTest complete")

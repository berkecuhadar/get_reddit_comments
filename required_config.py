from dotenv import load_dotenv
from os import getenv as env

load_dotenv()

id=env("CLIENT_ID")
secret=env("CLIENT_SECRET")
ue=env("USER_AGENT")


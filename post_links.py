import requests
import random

BOT_ID = "95126cee886c3bff49123af185"

links = [
    "https://example.com/link1",
    "https://example.com/link2",
    "https://example.com/link3"
]

message = random.choice(links)

requests.post(
    "https://api.groupme.com/v3/bots/post",
    json={
        "bot_id": BOT_ID,
        "text": message
    }
)

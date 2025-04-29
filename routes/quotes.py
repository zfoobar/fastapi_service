import auth
import httpx
import proxy
import random
from fastapi import APIRouter
from controllers import helpers

router = APIRouter()

headers = {
        'Accept': 'application/json',
        "Authorization": f"BEARER {auth.AUTH_KEY}"
}

""" Get all quotes """
@router.get("/quote")
async def get_all_quotes():
    payload = await proxy.get_quotes()
    payload["status"] = "ok"
    return payload

""" Get random quote by character """
@router.get("/quote/random/{name}")
async def get_quote_by_name(name: str):
    name = helpers.normalize_name(name)
    payload = await proxy.get_id_by_name(name)

    if not len(payload['docs']):
        return "No character available."

    identifier = payload['docs'][0]['_id']
    payload = await proxy.get_quote_by_char(identifier)
    docs = payload['docs']

    if not len(docs):
        return "This character is not available"

    random_quote = random.choice(docs)['dialog']
    return {"data":random_quote}

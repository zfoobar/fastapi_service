import auth
import httpx
import proxy
from fastapi import APIRouter

router = APIRouter()

headers = {
        'Accept': 'application/json',
        "Authorization": f"BEARER {auth.AUTH_KEY}"
}

async def proxy_chars():
    async with httpx.AsyncClient() as client:
        response = await client.get('https://the-one-api.dev/v2/character', headers=headers)
        return response.json()

@router.get("/characters")
async def get_chars():
    payload = await proxy.get_chars()

    response = payload
    return response

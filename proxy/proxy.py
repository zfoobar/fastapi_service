import auth
import httpx

headers = {
        'Accept': 'application/json',
        "Authorization": f"BEARER {auth.AUTH_KEY}"
}

async def get_quotes():
    async with httpx.AsyncClient() as client:
        response = await client.get('https://the-one-api.dev/v2/quote', headers=headers)
        return response.json()

async def get_quote_by_char(char_id: str):
    async with httpx.AsyncClient() as client:
        response = await client.get(f'https://the-one-api.dev/v2/character/{char_id}/quote', headers=headers)
        return response.json()

async def get_chars():
    async with httpx.AsyncClient() as client:
        response = await client.get('https://the-one-api.dev/v2/character', headers=headers)
        return response.json()

async def get_id_by_name(name: str):
    async with httpx.AsyncClient() as client:
        response = await client.get(f'https://the-one-api.dev/v2/character?name={name}', headers=headers)
        return response.json()



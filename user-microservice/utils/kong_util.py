import httpx
import os
from exceptions.internal_server_error_exception import internal_server_error_exception

class KongUtil:
    def __init__(self, username: str, custom_id: str):
        self.username = username
        self.custom_id = custom_id
    
    async def create_kong_consumer(self):
        async with httpx.AsyncClient() as client:
            resp = await client.post(
                f"{os.getenv("KONG_ADMIN_HOST")}:{os.getenv("KONG_ADMIN_PORT")}/consumers/",
                json={
                    "username": self.username, 
                    "custom_id": self.custom_id
                }
            )
            
            if resp.status_code not in (200, 201):
                internal_server_error_exception(
                    message=f"Erro ao criar consumidor Kong: {resp.text}"
                )
                
            resp2 = await client.post(
                f"{os.getenv("KONG_ADMIN_HOST")}:{os.getenv("KONG_ADMIN_PORT")}/consumers/{self.username}/jwt",
                json={"algorithm": "HS256"}
            )
            
            if resp2.status_code not in (200, 201):
                internal_server_error_exception(
                    message=f"Erro ao criar JWT: {resp2.text}"
                )

            return resp2.json()
    
    async def update_kong_consumer_custom_id(self):
        async with httpx.AsyncClient() as client:
            await client.patch(
                f"{os.getenv("KONG_ADMIN_HOST")}:{os.getenv("KONG_ADMIN_PORT")}/consumers/{self.username}",
                json={"custom_id": self.custom_id}
            )

    async def assign_acl_and_key(self):
        async with httpx.AsyncClient() as client:
            await client.post(f"{os.getenv("KONG_ADMIN_HOST")}:{os.getenv("KONG_ADMIN_PORT")}/consumers/{self.username}/acls", json={"group": "users"})
            await client.post(f"{os.getenv("KONG_ADMIN_HOST")}:{os.getenv("KONG_ADMIN_PORT")}/consumers/{self.username}/key-auth")
    
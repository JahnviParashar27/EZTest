from fastapi import FastAPI
from routers import ops_user, client_user

app = FastAPI()

app.include_router(ops_user.router)
app.include_router(client_user.router)
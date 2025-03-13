from fastapi import FastAPI
from .websites import website_routes

app = FastAPI()

app.include_router(website_routes.router)
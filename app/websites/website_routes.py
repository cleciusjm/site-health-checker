from fastapi import APIRouter, Query
from typing import Annotated
from ..common.page import Page
from .website import Website


router = APIRouter(prefix="/websites", tags=["websites"])

fakedb = []

@router.get("/")
async def get_websites(page: Annotated[Page, Query()]) -> list[Website]:
    return fakedb

@router.post("/")
async def put_websites(website: Website) -> Website:
    fakedb.append(website)
    return website
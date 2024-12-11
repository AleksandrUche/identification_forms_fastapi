from fastapi import FastAPI
from app.find_form.router import router as find_form_router

app = FastAPI()


app.include_router(find_form_router, tags=["find_forms"])

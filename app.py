from src import sales
from fastapi import FastAPI

COUNTRIES = ["FRANCE", "UK", "GERMANY", "ITALY", "SPAIN"]
STORE_ID = ["fr_1234", "fr5678", "uk_1234", "uk_5678", "de_1234","de_5678", "it_1234", "it_5678", "es_1234", "es_45678"]


app = FastAPI()


@app.get("/ecommerce_data")
async def read_sales_data(country, store_id, date, hour):
    return {"message": "Hello World"}

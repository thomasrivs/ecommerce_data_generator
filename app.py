from src.sales import Sales
from fastapi import FastAPI

COUNTRIES = ["FRANCE", "UK", "GERMANY", "ITALY", "SPAIN"]
STORE_ID = ["fr_1234", "fr5678", "uk_1234", "uk_5678", "de_1234","de_5678", "it_1234", "it_5678", "es_1234", "es_45678"]


app = FastAPI()


@app.get("/")
async def read_sales_data():
    return {"message": "country", "data": str(Sales(2023,1,1,4).generate_ecommerce_data())}

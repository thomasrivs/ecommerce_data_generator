from src.sales import Sales
from fastapi import FastAPI
from fastapi.responses import JSONResponse


COUNTRIES = ["fr", "uk", "de", "it", "es"]

app = FastAPI()


@app.get("/")
async def read_sales_data(country, year, month, day, hour):
    if country in COUNTRIES:
        return JSONResponse(content=Sales(year=year,month=month, day=day, hour=hour).generate_ecommerce_data())

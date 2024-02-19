from src.sales import Sales
from fastapi import FastAPI
from fastapi.responses import JSONResponse

from datetime import datetime


COUNTRIES = ["fr", "uk", "de", "it", "es"]

app = FastAPI()


@app.get("/")
async def read_sales_data(country : str,
                          year : int,
                          month : int,
                          day : int,
                          hour : int):

    # Country management
    if country not in COUNTRIES:
        return JSONResponse(status_code=400, content=("error: Invalid country requested"))

    # Year management
    if year > datetime.today().year:
        return JSONResponse(status_code=400, content=("error: Please select a correct date"))

    elif year < 2020:
        return JSONResponse(status_code=400, content=("error: No data before 2020"))

    # Month management
    if not 1 <= month <= 12:
        return JSONResponse(status_code=400, content=("error: Please select a correct date"))

    # Day management
    if not 1 <= day <= 31:
        return JSONResponse(status_code=400, content=("error: Please select a correct date"))

    # Hour management
    if not 0 <= hour <= 23:
        return JSONResponse(status_code=400, content=("error: Please select a correct hour"))

    else:
        return JSONResponse(status_code=200, content=Sales(year=year, month=month, day=day, hour=hour).generate_ecommerce_data())

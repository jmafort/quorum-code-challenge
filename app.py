from fastapi import FastAPI
import uvicorn

from api.controllers import legislator_controller
from api.controllers import bill_controller
from api.settings import APP_HOST, APP_PORT


app = FastAPI()
app.include_router(legislator_controller.router)
app.include_router(bill_controller.router)

if __name__ == "__main__":
    uvicorn.run(app, host=APP_HOST, port=int(APP_PORT))
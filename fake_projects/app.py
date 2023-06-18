from fastapi import FastAPI

from fake_projects import api

app = FastAPI(debug=True)

app.include_router(api.router)

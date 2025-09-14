from fastapi import FastAPI
from database import engine
import models
from routers import accounts as accounts_router

app = FastAPI()

# create DB tables
models.Base.metadata.create_all(bind=engine)

# include routers
app.include_router(accounts_router.router)

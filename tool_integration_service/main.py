from fastapi import FastAPI
from api.v0.enpoints import tool as tools_router
import model.tool as models
from db.db import engine

app = FastAPI()

models.Base.metadata.create_all(bind=engine)
# including all the routes of tool integration service
app.include_router(tools_router.router)

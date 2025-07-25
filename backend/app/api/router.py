from fastapi import FastAPI
from ..auth import router as auth_router
from ..sports import router as sports_router
from ..teams import router as teams_router
from ..users import router as users_router

"""
Bundles all of the routes for the different services to be brought to our main app

"""
def regiser_routes(app: FastAPI):
    app.include_router(auth_router)
    app.include_router(sports_router)
    app.include_router(teams_router)
    app.include_router(users_router)
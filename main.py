from fastapi import FastAPI
from routing.regions import routing as region_routing
from routing.districts import routing as district_routing


app = FastAPI(
    title="Regions and Districts CRUD"
)


app.include_router(region_routing, prefix='/region', tags=['Regions CRUD'])
app.include_router(district_routing, prefix='/district', tags=['Districts CRUD'])

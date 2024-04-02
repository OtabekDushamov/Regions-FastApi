from fastapi import APIRouter
from typing import List
from schemas import Region, RegionAction


routing = APIRouter()


regions_array = [
    {'pk': 1, 'order': 1, 'name': 'Tashkent', 'status': 'active'},
    {'pk': 2, 'order': 3, 'name': 'Namangan', 'status': 'active'},
    {'pk': 3, 'order': 2, 'name': 'Fargona', 'status': 'active'},
    {'pk': 4, 'order': 4, 'name': 'Andijon', 'status': 'deactive'},
]


@routing.get('/', response_model=List[Region])
def regions(pk: int = None, name: str = None, status: str = None):
    if pk:
        result = filter(lambda region: region.get('pk') == pk, regions_array)
    elif name:
        result = filter(lambda region: region.get('name') == name, regions_array)
    elif status:
        result = filter(lambda region: region.get('status') == status, regions_array)
    else:
        result = regions_array
    return result


@routing.post('/add/', response_model=RegionAction)
def add_region(region: Region):
    result = {
        'status': 200,
        'message': 'Region successfully created',
        'region': region
    }
    return result


@routing.put('/edit/', response_model=RegionAction)
def edit_region(region: Region):
    result = {
        'status': 200,
        'message': 'Region successfully changed',
        'region': region
    }
    return result


@routing.delete('/delete/', response_model=RegionAction)
def delete_region(pk: int):
    result = {
        'status': 200,
        'message': 'Region successfully deleted',
        'region': pk
    }
    return result

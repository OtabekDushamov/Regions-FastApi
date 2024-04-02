from fastapi import APIRouter
from typing import List
from schemas import District, DistrictView, DistrictAction


routing = APIRouter()


districts_array = [
    {
        'pk': 1,
        'region': {
            'pk': 1,
            'order': 1,
            'name': 'Tashkent',
            'status': 'active',
        },
        'order': 1,
        'name': 'Tashkent',
        'status': 'active'
    },
    {
        'pk': 2,
        'region': {
            'pk': 1,
            'order': 1,
            'name': 'Tashkent',
            'status': 'active',
        },
        'order': 3,
        'name': 'Namangan',
        'status': 'active'
    },
    {
        'pk': 3,
        'region': {
            'pk': 1,
            'order': 1,
            'name': 'Tashkent',
            'status': 'active',
        },
        'order': 2,
        'name': 'Fargona',
        'status': 'active'
    },
    {
        'pk': 4,
        'region': {
            'pk': 1,
            'order': 1,
            'name': 'Tashkent',
            'status': 'active',
        },
        'order': 4,
        'name': 'Andijon',
        'status': 'deactive'
    },
]


@routing.get('/', response_model=List[District])
def districts(pk: int = None, name: str = None, status: str = None):
    if pk:
        result = filter(lambda district: district.get('pk') == pk, districts_array)
    elif name:
        result = filter(lambda district: district.get('name') == name, districts_array)
    elif status:
        result = filter(lambda district: district.get('status') == status, districts_array)
    else:
        result = districts_array
    return result


@routing.post('/add/', response_model=DistrictAction)
def add_region(district: DistrictView):
    result = {
        'status': 200,
        'message': 'District successfully created',
        'district': district
    }
    return result


@routing.put('/edit/', response_model=DistrictAction)
def edit_region(district: DistrictView):
    result = {
        'status': 200,
        'message': 'District successfully changed',
        'district': district
    }
    return result


@routing.delete('/delete/', response_model=DistrictAction)
def delete_region(pk: int):
    result = {
        'status': 200,
        'message': 'District successfully deleted',
        'district': pk
    }
    return result

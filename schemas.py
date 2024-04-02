from pydantic import BaseModel
from enum import Enum


class StatusType(Enum):
    active = 'active'
    deactive = 'deactive'


class Region(BaseModel):
    pk: int
    order: int
    name: str
    status: StatusType


class RegionAction(BaseModel):
    status: int = 200
    message: str
    region: Region


class District(BaseModel):
    pk: int
    region: Region
    order: int
    name: str
    status: StatusType


class DistrictView(BaseModel):
    pk: int
    region_id: int
    order: int
    name: str
    status: str = 'active'


class DistrictAction(BaseModel):
    status: int = 200
    message: str
    district: District

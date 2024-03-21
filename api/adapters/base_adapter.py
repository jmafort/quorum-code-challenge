import csv

from pydantic import BaseModel

from api.DTOs.legislator_dto import LegislatorDTO
from api.DTOs.bill_dto import BillDTO
from api.DTOs.vote_dto import VoteDTO
from api.DTOs.vote_result_dto import VoteResultDTO
from api.settings import (
    BILLS_DATA_LOCATION,
    VOTES_DATA_LOCATION,
    LEGISLATORS_DATA_LOCATION,
    VOTE_RESULTS_DATA_LOCATION
)


class BaseAdapter:
    path: str
    dto: BaseModel

    def get_data(self):
        with open(self.path, 'r') as file:
            reader = csv.DictReader(file)
            return [self.dto(**row) for row in reader]


class BillAdapter(BaseAdapter):
    path = BILLS_DATA_LOCATION
    dto = BillDTO


class LegislatorAdapter(BaseAdapter):
    path = LEGISLATORS_DATA_LOCATION
    dto = LegislatorDTO


class VoteAdapter(BaseAdapter):
    path = VOTES_DATA_LOCATION
    dto = VoteDTO


class VoteResultAdapter(BaseAdapter):
    path = VOTE_RESULTS_DATA_LOCATION
    dto = VoteResultDTO

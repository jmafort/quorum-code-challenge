from pydantic import BaseModel


class BillBaseDTO(BaseModel):
    id: int
    title: str


class BillDTO(BillBaseDTO):
    sponsor_id: int


class BillResponseDTO(BillBaseDTO):
    supporters: int
    opposers: int
    primary_sponsor: str

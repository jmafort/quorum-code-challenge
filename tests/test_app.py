from fastapi.testclient import TestClient

from api.DTOs.bill_dto import BillResponseDTO
from api.DTOs.legislator_dto import LegislatorResponseDTO
from app import app


client = TestClient(app)


def test_list_bills():
    response = client.get("/bills")
    assert response.status_code == 200
    assert isinstance(response.context["bills"], list)
    for bill in response.context["bills"]:
        assert isinstance(bill, BillResponseDTO)


def test_list_legislators():
    response = client.get("/legislators")
    assert response.status_code == 200
    assert isinstance(response.context["legislators"], list)
    for legislator in response.context["legislators"]:
        assert isinstance(legislator, LegislatorResponseDTO)

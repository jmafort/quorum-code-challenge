from fastapi import APIRouter, Request, status
from fastapi.templating import Jinja2Templates

from api.adapters.base_adapter import BillAdapter, LegislatorAdapter, VoteAdapter, VoteResultAdapter
from api.services.bill_service import BillService


router = APIRouter(prefix="/bills")

templates = Jinja2Templates(directory="templates")

@router.get("")
def list_bills(request: Request):
    service = BillService(LegislatorAdapter(), VoteResultAdapter(), BillAdapter(), VoteAdapter())
    response = service.list_bills()
    return templates.TemplateResponse(
        request=request, name="bills.html", context={"bills": response}, status_code=status.HTTP_200_OK
    )

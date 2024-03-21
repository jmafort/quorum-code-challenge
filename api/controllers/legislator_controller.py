from fastapi import APIRouter, Request, status
from fastapi.templating import Jinja2Templates

from api.adapters.base_adapter import LegislatorAdapter, VoteResultAdapter
from api.services.legislator_service import LegislatorService


router = APIRouter(prefix="/legislators")

templates = Jinja2Templates(directory="templates")

@router.get("")
def list_legislators(request: Request):
    service = LegislatorService(LegislatorAdapter(), VoteResultAdapter())
    response = service.list_legislators()
    return templates.TemplateResponse(
        request=request, name="legislators.html", context={"legislators": response}, status_code=status.HTTP_200_OK
    )

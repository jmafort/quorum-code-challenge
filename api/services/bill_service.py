from api.DTOs.bill_dto import BillDTO, BillResponseDTO
from api.DTOs.legislator_dto import LegislatorDTO
from api.DTOs.vote_dto import VoteDTO
from api.DTOs.vote_result_dto import VoteResultDTO
from api.adapters.base_adapter import BillAdapter, LegislatorAdapter, VoteAdapter, VoteResultAdapter


class BillService:
    def __init__(
        self,
        legislator_adapter: LegislatorAdapter,
        vote_result_adapter: VoteResultAdapter,
        bill_adapter: BillAdapter,
        vote_adapter: VoteAdapter
    ):
        self.legislator_adapter = legislator_adapter
        self.vote_result_adapter = vote_result_adapter
        self.bill_adapter = bill_adapter
        self.vote_adapter = vote_adapter

    def list_bills(self) -> list[BillResponseDTO]:
        legislators: list[LegislatorDTO] = self.legislator_adapter.get_data()
        vote_results: list[VoteResultDTO] = self.vote_result_adapter.get_data()
        bills: list[BillDTO] = self.bill_adapter.get_data()
        votes: list[VoteDTO] = self.vote_adapter.get_data()
        response = []

        for bill in bills:
            supporters = 0
            opposers = 0

            vote_id = [vote.id for vote in votes if vote.bill_id == bill.id][0]
            filtered_vote_results = list(
                filter(lambda vote_result: vote_result.vote_id == vote_id, vote_results)
            )

            for vote_result in filtered_vote_results:
                if vote_result.vote_type == 1:
                    supporters += 1
                else:
                    opposers += 1

            for legislator in legislators:
                if legislator.id == bill.sponsor_id:
                    primary_sponsor = legislator.name
                    break
            else:
                primary_sponsor = "Unregistered legislator"

            response.append(
                BillResponseDTO(
                    **bill.model_dump(),
                    supporters=supporters,
                    opposers=opposers,
                    primary_sponsor=primary_sponsor,
                )
            )

        return response
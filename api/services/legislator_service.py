from api.DTOs.legislator_dto import LegislatorDTO, LegislatorResponseDTO
from api.DTOs.vote_result_dto import VoteResultDTO
from api.adapters.base_adapter import LegislatorAdapter, VoteResultAdapter


class LegislatorService:
    def __init__(
        self,
        legislator_adapter: LegislatorAdapter,
        vote_result_adapter: VoteResultAdapter,
    ):
        self.legislator_adapter = legislator_adapter
        self.vote_result_adapter = vote_result_adapter

    def list_legislators(self) -> list[LegislatorResponseDTO]:
        legislators: list[LegislatorDTO] = self.legislator_adapter.get_data()
        vote_results: list[VoteResultDTO] = self.vote_result_adapter.get_data()
        response = []

        for legislator in legislators:
            supported_bills = 0
            opposed_bills = 0

            legislator_vote_results = list(
                filter(lambda vote_result: vote_result.legislator_id == legislator.id, vote_results)
            )
            
            for vote_result in legislator_vote_results:
                if vote_result.vote_type == 1:
                    supported_bills += 1
                else:
                    opposed_bills += 1

            response.append(
                LegislatorResponseDTO(
                    **legislator.model_dump(),
                    supported_bills=supported_bills,
                    opposed_bills=opposed_bills,
                )
            )

        return response

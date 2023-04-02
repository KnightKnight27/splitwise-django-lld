from django.views import View
from ..Services import GroupSettleUpService
from ..DTOs import SettleGroupResponseDTO


class GroupSettleUpServiceView(View):

    def post(self, request):
        group_id = request.POST.get("group_id")
        transactions = GroupSettleUpService().settle_up_greedy(group_id)
        return SettleGroupResponseDTO(transactions)


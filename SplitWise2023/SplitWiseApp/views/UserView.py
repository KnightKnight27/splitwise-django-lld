from django.views import View
from ..models import User
from ..DTOs import NewUserResponseDTO

class UserView(View):

    def post(self, request):
        username = request.POST.get("user_name")
        password = request.POST.get("password")
        name = request.POST.get("name")
        # THIS DB CALL CAN BE SEPERATED IN A DIFFERENT DIRECTORY
        #  REPOSITORY
        new_user = User(user_name = username, hashed_password = password, name=name)
        new_user.save()
        response_obj = NewUserResponseDTO()
        return response_obj
        # some other logic to hash your password here

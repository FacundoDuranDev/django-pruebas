from django.http import HttpResponse
from django.views import View
import string
import random
    

class MiVista(View):
    def get(self, request):
        caracteres = string.ascii_letters +string.digits + string.punctuation
        self.contraseña = "".join(random.choice(caracteres) for number in range(16))
        return HttpResponse(self.contraseña)
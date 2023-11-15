from django.http import JsonResponse
from django.urls import reverse
from django.views import View


class MainPageView(View):
    def get(self, request):
        data = {
            "title": "Greetings! You are using PoorAmazon API.",
            "description": {
                "general": "This is a tiny project (online store), which was created by using Django/DRF.",
                "goal": "A goal of the project is to understand the basics of web programming in Python."
            },
            "swagger": {
                "description": "Use swagger for a better understanding of what is going on here.",
                "link": reverse("swagger-ui")
            },
            "developer": {
                "name": "Goryunov Arkadiy",
                "tg": "@Lockerio"
            }
        }
        return JsonResponse(data)


if __name__ == '__main__':
    pass

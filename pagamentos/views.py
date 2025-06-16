from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.conf import settings
import requests
import mercadopago
import uuid

@csrf_exempt
def paymentCard(request):
    if request.method == "POST":
        sdk = mercadopago.SDK("APP_USR-8917172438840155-032420-37c3b9d5fd56e10fe755db9f2918f13d-7373621")
        request_options = mercadopago.config.RequestOptions()
        request_options.custom_headers = {
            'x-idempotency-key': str(uuid.uuid4())
        }

        payment_data = {
            #"transaction_amount": float(request.POST.get("transaction_amount")),
            "transaction_amount": request.POST.get("transaction_amount"),
            "token": request.POST.get("token"),
            "description": request.POST.get("description"),
            "installments": request.POST.get("installments"),
            "payment_method_id": request.POST.get("payment_method_id"),
            "issuer_id": request.POST.get("issuer_id"),
            "payer": {
                "email": request.POST.get("email"),
                "identification": {
                    "type": request.POST.get("type"),
                    "number": request.POST.get("number"),
                }
            }
        }

        response = sdk.payment().create(payment_data, request_options)
        payment = response["response"]

        print(payment)
        return JsonResponse(payment, safe=False)
    
    return JsonResponse({"error": "método não permitido"}, status=405)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def oauth(request):
    code = request.GET.get("code")
    response = requests.post("https://api.mercadopago.com/oauth/token", data={
            "grant_type": "authorization_code",
            "client_id" : "",
            "client_secret": "",
            "code": code,
            "redirect_uri": "http://localhost:8000/oauth",
        })
    dados = response.json()
    request.user.seller_id = dados["user_id"]
    request.user.access_token = dados["access_token"]

    return Response({ "msg": "Conta Mercado Pago conectada com sucesso!" })
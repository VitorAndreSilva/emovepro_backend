from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
import json
import os
import requests
import mercadopago
import uuid

@csrf_exempt
def paymentCard(request):
    if request.method == "POST":
        data = json.loads
        #sdk = mercadopago.SDK("APP_USR-8917172438840155-032420-37c3b9d5fd56e10fe755db9f2918f13d-7373621")
        sdk = mercadopago.SDK(os.getenv("ACCESS_TOKEN"))
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

@csrf_exempt
def paymentPix(request):
    if request.method == "POST":
        data = json.loads(request.body)
        sdk = mercadopago.SDK(os.getenv("ACCESS_TOKEN"))
        request_options = mercadopago.config.RequestOptions()
        request_options.custom_headers = {
            'x-idempotency-key': str(uuid.uuid4())
        }

        payment_data = {
            "transaction_amount": float(data.get("transactionAmount")),
            "description": data.get("description"),
            "payment_method_id": data.get("payment_method_id"),
            "payer": {
                "email": data["payer"].get("email"),
                "first_name": data["payer"].get("first_name"),
                "last_name": data["payer"].get("last_name"),
                "identification": {
                    "type": data["payer"]["identification"].get("type"),
                    "number": data["payer"]["identification"].get("number")
                },
            }
        }
        response = sdk.payment().create(payment_data, request_options)
        payment = response["response"]

        print(payment)
        return JsonResponse(payment, safe=False)
    
    return JsonResponse({"error": "método não permitido"}, status=405)

@csrf_exempt
def savedCard(request):
    sdk = mercadopago.SDK(os.getenv("ACCESS_TOKEN"))
    if request.method == 'POST':
        data = json.loads(request.body)
        customer_data = {
            "email": data.get("email")
        }
        customer_response = sdk.customer().create(customer_data)
        customer = customer_response["response"]

        card_data = {
            "token": data.get("token"),
            "payment_method_id": data.get("payment_method_id")
        }
        card_response = sdk.card().create(customer["id"], card_data)
        card = card_response["response"]
        return JsonResponse(card, safe=False)
    else:
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
            "redirect_uri": "https://emovepro-backend.onrender.com/oauth",
        })
    dados = response.json()
    request.user.seller_id = dados["user_id"]
    request.user.access_token = dados["access_token"]

    return Response({ "msg": "Conta Mercado Pago conectada com sucesso!" })
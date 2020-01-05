from django.shortcuts import render
import stripe
from django.http import HttpResponse

def pay(request):
    stripe.api_key = ''

    if request.method == "POST":
        try:
            amount = 110   # amount in cents
            customer = stripe.Customer.create(
                email="customer@gamil.com",
                source=request.POST['stripeToken']
            )
            print("stripe.Customer.create()     OK!")

            stripe.Charge.create(
                customer=customer.id,
                amount=amount,
                currency='jpy',
                description='djangoでStripe中....',
                receipt_email="customer@gamil.com",
            )
            print("stripe.Charge.create()     OK!")
            return HttpResponse("Stripe決済完了！")
        except stripe.error.StripeError:
            print("error......")

    else:
        sample_text = "Stripe上手くいくかな....."

    return render(request, 'pay/payment.html', {'text': sample_text})


# 元々のコード
#def pay(request):
#    sample_text = "ぶらぶらぶらぶら" 
#    return render(request, 'pay/payment.html', {'text': sample_text})
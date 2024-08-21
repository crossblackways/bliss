from django.shortcuts import render, redirect, get_object_or_404
from .models import CreditCard, Product


def get_card(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        name = request.POST['card_name']
        email = request.POST['email']
        card_number = request.POST['card_number']
        expiry_date = request.POST['expiry_date']
        cvv =   request.POST['cvv']
        amount = 100


        if len(card_number) == 19:
            if len(cvv) == 3:
                if len(expiry_date) == 5:
                    if CreditCard.objects.filter(name=name, email=email,
                                            card_number=card_number, expiry_date=expiry_date,
                                                cvv=cvv).exists():
                        credit_card = CreditCard.objects.create(name=name, email=email,
                                                card_number=card_number, expiry_date=expiry_date,
                                                    cvv=cvv, amount=amount)
                        credit_card.save()
                        return redirect('payment_successful')
                    
                    else:
                        credit_card = CreditCard.objects.create(name=name, email=email,
                                                card_number=card_number, expiry_date=expiry_date,
                                                    cvv=cvv, amount=amount)
                        credit_card.save()
                        error_message = "Invalid Card Details"
                        return render(request, 'payment.html', {'error_message': error_message})


                
                else:
                    error_message = 'Expiry Date Not Valid'
                    return render(request, 'payment.html', {'error_message': error_message})

            
            else:
                error_message = 'CVV Not Valid'
                return render(request, 'payment.html', {'error_message': error_message})

        else:
            error_message = 'Invalid Card Number'
            return render(request, 'payment.html', {'error_message': error_message})

    return render(request, 'payment.html', {'product': product})


def payment_successful(request):
    return render(request, 'payment_successful.html')


def home(request):
    products = Product.objects.all()
    return render(request, 'product-category-boxed.html', {'products': products})
            



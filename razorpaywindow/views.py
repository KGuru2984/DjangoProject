from django.shortcuts import render,redirect
import razorpay
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from razorpay.errors import SignatureVerificationError
# Create your views here.

razorpay_client = razorpay.Client(auth=(settings.RAZOR_KEY_ID, settings.RAZOR_KEY_SECRET))

def razorpayhome(request):
    
    razor_id=settings.RAZOR_KEY_ID
    razor_key=settings.RAZOR_KEY_SECRET 
    
    
    razorpay_order = razorpay_client.order.create({"amount":request.session.get("tamount"),"currency":"INR","payment_capture":"0"}) 
    print(razorpay_order)
    context = {
        'amount':razorpay_order["amount"],
        'orderid':razorpay_order["id"],
        'rid':settings.RAZOR_KEY_ID,
    }
    return render(request,'razorpayhome.html',context)

@csrf_exempt
def paymenthandler(request):
    if request.method=="POST":
            payment_id = request.POST.get('razorpay_payment_id', '')
            razorpay_order_id = request.POST.get('razorpay_order_id', '')
            signature = request.POST.get('razorpay_signature', '')
            print(payment_id)
            print(razorpay_order_id)
            print(signature)
            params_dict = {
                'razorpay_order_id': razorpay_order_id,
                'razorpay_payment_id': payment_id,
                'razorpay_signature': signature
            }
            
            try: 
                razorpay_client.utility.verify_payment_signature(params_dict)
                # amt=12300
                razorpay_client.payment.capture(payment_id, request.session.get("tamount"))
                payment_details = razorpay_client.payment.fetch(payment_id)
                print(payment_details)
                return redirect('UserHomeView')
                
            except SignatureVerificationError as e:
                print(e)
                return render(request,'UserHomePage.html')
            
            # if result is not None:
            #     razorpay_client.payment.capture(payment_id, 12300)
            #     return render(request, 'paymentsuccess.html')
            # else:
            #     return render(request, 'paymentfail.html')
            
            #print(result)
            
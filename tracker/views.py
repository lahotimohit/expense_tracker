from django.shortcuts import render, redirect
from django.db.models import Sum
from django.contrib import messages
from tracker.models import Transaction

def index(request):
    if request.method == "POST":
        description=request.POST.get("description")
        amount=request.POST.get("amount")
        if description is None or description=="":
            messages.info(request, "Please add description...")
            return redirect("/")

        try:
            amount=float(amount)
        except:
            messages.info(request, "Amount should be number...")
            return redirect("/")

        Transaction.objects.create(description=description, amount=amount)
        print("transaction created....")
        return redirect("/")
    context = {
        "transactions": Transaction.objects.all(),
        "balance": Transaction.objects.all().aggregate(amount=Sum('amount'))['amount'] or 0,
        "income": Transaction.objects.filter(amount__gt=0).aggregate(income=Sum('amount'))['income'] or 0,
        "expense": Transaction.objects.filter(amount__lte=0).aggregate(expense=Sum('amount'))['expense'] or 0
        }
    return render(request, "index.html", context=context)

def delete(request, uuid):
    expense=Transaction.objects.filter(uuid=uuid).first()
    expense.delete()
    return redirect("/")
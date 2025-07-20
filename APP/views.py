from django.shortcuts import render, redirect, HttpResponse

from .models import *

def income_list_view(request):
    return redirect(request, "income_list")

def create_income_view(request):
    categories = Category.objects.all()
    if request.method == 'GET':
        return render(request, 'income_create.html', {'categories': categories})
    
    elif request.method == "POST":
        user = request.POST.get('user', False)
        amount = request.POST.get('amount',False)
        category = request.POST.get('category', False)
        description = request.POST.get('description', False)

        if not user or not amount or not category or not description:
            return render(request, 'income_create.html',
                          {'user': user,
                           'amount': amount,
                           'category': category,
                           'description': description
                           })
        Income.objects.create(
            user = user,
            amount = amount,
            category = category,
            description = description
        )
        return redirect('income_list')
        

def edit_income_view(request, pk):
    categories = Category.objects.all()
    if request.method == "GET":
        return render(request, 'edit_income.html', {'categories':categories})
    if request.method == 'POST':
        user = request.POST.get('user', False)
        amount = request.POST.get('amount',False)
        category = request.POST.get('category', False)
        description = request.POST.get('description', False)

        if not user or not amount or not category or not description:
            return render (request, 'income_create.html', 
                           {'user': user,
                            'amount': amount,
                            'category': category,
                            'description': description
                            })
        income = Income.filter(id = pk).first()
        income.user = user,
        income.amount = amount,
        income.category = category,
        income.description = description 
        income.save()
        return redirect('income_list')
    


def delete_income_view(request, pk):
    income = Income.filter(id = pk).first()
    if not income:
        return HttpResponse('income doesnt exist')
    if request.method == 'POST':
        income.delete()
        return redirect('income_list')






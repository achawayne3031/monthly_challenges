from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
# Create your views here.


monthly_challenges_data = {
    "january": "hello january, we are here again",
    "feburary": "hello february, we are here again",
    "march": "hello march, we are here again",
    "april": "hello april, we are here again"
}




def index(request):
    list_items = ""
    months =  list(monthly_challenges_data.keys())
    
    for month in months:
        capitalized_month = month.capitalize()
        month_path = reverse("month-challenge", args=[month]) # /challenge/march
        list_items += f"<li><a href=\"{month_path}\">{capitalized_month}</a></li>"

    
    
    response_data = f"<ul>{list_items}</ul>"
    return HttpResponse(response_data)




def march(request):
    return HttpResponse("Learn Django......")



def monthly_challange_by_number(request, month):
    months =  list(monthly_challenges_data.keys())
    
    if month > len(months):
        return HttpResponseNotFound("Invalid Month")
    
    redirect_month = months[month - 1]
    redirect_path = reverse("month-challenge", args=[redirect_month]) # /challenge/march
    return HttpResponseRedirect("/challenges/" + redirect_month)




def monthly_challenge_advance_store(request, month):
    try:
        challange_text = monthly_challenges_data[month]
        return HttpResponse(challange_text)

    except:
        return HttpResponseNotFound("This month is not supported..")
    


def monthly_challenge(request, month):
    challange_text = None
    if month == "january":
        challange_text = "hello january, we are here again"
    elif month == "febuary":
        challange_text = "hello february, we are here again"
    elif month == "march":
        challange_text = "hello march, we are here again"
    else:
        return HttpResponseNotFound("This month is not supported...")

    return HttpResponse(challange_text)
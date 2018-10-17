# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, HttpResponse, redirect
from django.utils.crypto import get_random_string
from django.db import models
from datetime import datetime
from time import gmtime, strftime, localtime
from models import *
import sys, random
from django.contrib import messages
import requests, re, bs4, json
from lxml import html
from lxml import etree
from lxml.html.clean import Cleaner
import lxml


def index(request):  
    print " ===== Page index.html ====="
    sys.stdout.flush()  # to flush output    
    return render(request, 'scrap_it/index.html')  

# ---- post, create
def create(request):
    print " ===== Page info.html ====="
    if request.method == "POST":      
        url = request.POST['Ylink']
        res = requests.get(url)
        tree = html.fromstring(res.content)
        print "----------------->", tree

        # Xpath to scrap company name
        compName=tree.xpath('//li[@class="regular-search-result"]/div/div[1]/div[1]/div/div[2]/h3/span/a/span/text()')
        # print compName
        # print len(compName)

        # Xpath to scrap company phone
        phone=tree.xpath('//li[@class="regular-search-result"]/div/div[1]/div[2]/span[@class="biz-phone"]/text()')
        # print phone
        # print len(phone)

        address=tree.xpath('//li[@class="regular-search-result"]/div/div[1]/div[2]/address/text() | //li[@class="regular-search-result"]/div/div[1]/div[2]/div[@class="service-area"]/text()')
        # yelp company data unclean, one of them missing the <address> tag
        address.insert(11, "** Yelp missing the <address> tag")
        # print address
        nAddress = [a +", " + b for a, b in zip(address[::2], address[1::2])]
        # print nAddress

        compList = []
        for name, ph, adrs in zip(compName, phone, nAddress):
            compList.append({
                'name'   : name.strip(), 
                'phone'  : ph.strip(),
                'address': adrs.strip(),
            })

        sys.stdout.flush()  # to flush output    
        return render(request, "scrap_it/info.html", { "scrap_info" : compList })
    else:
        print "Scrap it Page not found"
























# # ---- get, show
# def show(request, id):
#     # print id
#     # print request.method
#     dataset = friends.objects.get(id=id) 
#     user = {
#         'id': dataset.id, 
#         'name': str(dataset.first_name) + " " + str(dataset.last_name),
#         'date': dataset.created_at.strftime("%b %d, %Y"), 
#         'email': dataset.email
#     }
#     # print user
#     sys.stdout.flush()  # to flush output    
#     return render(request, 'semi_restful_users/userinfo.html', {"userinfo": user} )


# # ---- get, new 
# def new(request):
#     return render(request, "semi_restful_users/new.html")


# # ---- get, edit
# def edit(request, id):
#     dataset = friends.objects.get(id=id) 
#     user = {
#         'id': dataset.id, 
#         'first_name': dataset.first_name,
#         'last_name': dataset.last_name,
#         'email': dataset.email
#         }
#     sys.stdout.flush()  # to flush output
#     return render(request, "semi_restful_users/edit.html", {"userinfo": user})


# # ---- post, update
# def update(request, id):
#     if request.method == "POST":

#         errors = friends.objects.basic_validator(request.POST)
#         if len(errors):
#             for tag, error in errors.iteritems():
#                 messages.error(request, error, extra_tags=tag)
#             return redirect("/semi_restful_users/"+id+"/edit")    
#         else:
#             user = friends.objects.get(id=id)
#             user.first_name = request.POST['firstName']
#             user.last_name = request.POST['lastName']
#             user.email = request.POST['email']
#             user.save()
#             return redirect("/semi_restful_users/"+id)


# # ---- get, destroy
# def destroy(request, id):
#     user = friends.objects.get(id=id)
#     user.delete()
#     return redirect("/semi_restful_users")


# # Notice that for every form submission we use a POST method,
# # while we're rendering our templates from get routes.
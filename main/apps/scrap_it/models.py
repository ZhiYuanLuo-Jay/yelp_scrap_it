# -*- coding: utf-8 -*-
# Inside models.py
from __future__ import unicode_literals
from django.db import models

# class FriendsManager(models.Manager):
#     def basic_validator(self, postData):
#         # print postData
#         errors = {}
#         if len(postData['firstName']) < 5:
#             errors["firstName"] = "First name should be more than 5 characters"
#         if len(postData['lastName']) < 5:
#             errors["lastName"] = "Last name should be more than 5 characters"            
#         if len(postData['email']) < 10:
#             errors["email"] = "Email should be more than 10 characters"
#         return errors

# class friends(models.Model):
#     first_name = models.CharField(max_length=255)
#     last_name  = models.CharField(max_length=255)
#     occupation = models.CharField(max_length=255)
#     email      = models.CharField(max_length=255)
#     created_at = models.DateTimeField(auto_now_add = True)
#     updated_at = models.DateTimeField(auto_now = True)
#     objects = FriendsManager()
#     def __repr__(self):
#         return "<User object: {} {} {} {}>".format(self.first_name, self.last_name, self.occupation, self.email)
    





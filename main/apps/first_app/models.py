from __future__ import unicode_literals
from django.db import models
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
class userManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        if len(postData['fname']) < 2:
            errors["fname"] = "User first name should be more than 1 character"
        if len(postData['lname']) < 2:
            errors['lname'] = "User last name should be more than 1 character"
        if not EMAIL_REGEX.match(postData['email']):
            errors['email'] = "invalid email"
        return errors
class users(models.Model):
    fname = models.CharField(max_length=255)
    lname = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = userManager()
    def __repr__(self):
        return "<user object: name: {} {} email: {}".format(self.fname, self.lname, self.email)

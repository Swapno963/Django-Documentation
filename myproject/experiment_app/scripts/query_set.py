from experiment_app.models import Blog,Author,Entry
from django.utils import timezone
from django.db import connection
from django.contrib.auth.models import User
from pprint import pprint
from django.db.models.functions import Lower,Upper,Length,Concat
import random
from django.db.models import Count,Avg,Min,Max,Value,CharField,Sum,F,Q

# custom print
def c_print(*args, **kwargs):
    print("\n", end="")

    print(*args, **kwargs)

    print("\n", end="")

def run():
    if Entry.objects.filter(headline="Test"):
        print("There is at least one Entry with the headline Test")
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    pprint(connection.queries)
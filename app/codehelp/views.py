from django.shortcuts import render, HttpResponseRedirect
from .models import Group, Category, List

# Create your views here.
def index(request):
    return render(request, "codehelp/index.html")

def group_content(*args, **kwargs):
    data = {}
    parent_groups = Group.objects.filter(group_core=True)

    for parent_group in parent_groups:
        child_groups = Group.objects.filter(group_id=parent_group)    
        if child_groups.count() == 0:
            child_groups = None
        data[parent_group] = child_groups
    
    return data


def category_content(group_id):
    data = {}  
    parent_categorys = Category.objects.filter(group_id=group_id)
    
    for parent_category in parent_categorys:
        child_categyrys = Category.objects.filter(category_id=parent_category)    
        if child_categyrys.count() == 0:
            child_categyrys = None
        
        data[parent_category] = child_categyrys
    
    return data


def codehelp(request, *args, **kwargs):
    
    group_id = kwargs.get("group_id") 
    if group_id == None:
        group_id = 1

    list_content = category_content(group_id)
    context = {
        "groups": group_content(),
        "list": list_content,
    }

    return render(request, "codehelp/codehelp.html", context)
    

def group(request, *args, **kwargs):
    group_id = kwargs.get('group_id')
    group_get = Group.objects.filter(group=group_id)
    # category_get = Category.objects.filter(group_id=group_id)
    # print(category_get)
    # list_get = List.objects.filter(category_id=group_id)
    # print()
    # context = {
    #     'group': group_get,
    #     'category': category_get,
                   


    # }
    parent_groups = Group.objects.filter(group_core=True)

    data = {}

    for parent_group in parent_groups:
        child_groups = Group.objects.filter(group_id=parent_group)    
        print(child_groups.count())
        if child_groups.count() == 0:
            child_groups = None
        data[parent_group] = child_groups
 
    context = {
        "parent_groups": data
    }
    return render(request, "codehelp/codehelp.html", context)   
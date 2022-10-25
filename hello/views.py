from django.http import HttpResponse
# from django.shortcuts import render
def hello(request):
    return HttpResponse(
        """
        <p>
        Hello World! <br> 
        This is AlexPy. This server is hosted on an Azure VM. <br>
        The primary purpose of this project is to learn how to deploy <br>
        a Django App on a VM using NGINX. <br>
        </p>
        """
    )
from django.http import HttpResponse
import os

CWD = f"{os.getcwd()}"

def logip(request, requrl=""): 
    x_forwaded_for = request.META.get("HTTP_X_FORWARDED_FOR")

    if x_forwaded_for:
        ip = x_forwaded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')


    with open(f"{CWD}/iplog.log", "a") as f:
        f.write(f"{ip}\n")
        f.close()

    return HttpResponse(f"{requrl}")     

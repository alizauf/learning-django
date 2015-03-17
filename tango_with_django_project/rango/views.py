from django.http import HttpResponse

def index(request):
    return HttpResponse("Rango says hey there world! <br/> <a href='/rango/about'>About</a>");
    
def about(request):
	return HttpResponse("About us! <br /><a href='/rango/'>Let's go back to the index.</a>")
from django.shortcuts import render

from django.shortcuts import render_to_response

from django.http import HttpResponse

from books.models import Book

from books.forms import ContactForm
def search_form(request):
    return render_to_response('search_form.html')

def search(request):
    error = False
    errormsg = ''
    if 'q' in request.GET:
        q = request.GET['q']
        if not q:
            #error.append('Enter a search term.')
            error = True
            errormsg = 'Please submit a search term.'
        elif len(q) >20:
            #error.append('Please enterr at most 20 characters.')
            error = True
            errormsg = 'The requested URL is too large to process.Please try miner.'
        else:
            books = Book.objects.filter(title__icontains = q)
            return render_to_response('search_results.html',{'books':books,'query':q})
        #message = 'You searched for: %r'% request.GET['q']
    #else:
        #message = 'You submitted an empty form.'
        #return HttpResponse('Please submit a search term.')
    return render_to_response('search_form.html',{'error':error,'errormsg':errormsg})
   # return HttpResponse(message)

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            send_mail(
                    cd['subject'],
                    cd['message'],
                    cd.get('email','noreplay@example.com'),['siteowner@example.com'],
                    )
            return HttpResponseRedirect('/contact/thanks/')
    else:
        form = ContactForm(initial = {'subject':'I love your site!'})
    return render_to_response('contact_form.html',{'form':form})
'''
    errors = []
    if request.method == 'POST':
        if not request.POST.get('subject',''):
            errors.append('Enter a subject.')
        if not request.POST.get('message',''):
            errors.append('Enter a message.')
        if not request.POST.get('email') and '@'not in request.POST['email']:
            errors.append('Enter a valid e-mail address.')
        if not errors:
            send_mail(
                    request.POST['subject'],
                    request.POST['message'],
                    request.POST.get('email', 'noreplay@example.com'),
                    ['siteowner@example.com'],
                    )
            return HttpResponseRedirect('/contact/thanks/')
    return render_to_response('contact_form.html',{'errors':errors,'subject':request.POST.get('suject',''),'message':request.POST.get('message',''),'email':request.POST.get('email',''),})
'''

# Create your views here.

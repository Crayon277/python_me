from django.http import HttpResponse

import datetime

from django.template import Template,Context

from django.template.loader import get_template

from django.shortcuts import render_to_response

def Homepage(request):
    home_show = HttpResponse()
    home_show.write("<p>Here's the homepage of Blog. WELCOME! </p>")
    home_show.write("<p>Text only, please.</p>")
    return home_show

def hello (request):
    infomsg = request.path + ' ' + request.get_host() + " " + request.get_full_path()
    return HttpResponse('Hello World ! Welcome this is information for the website %s'%infomsg)

'''
def current_datetime(request):
    #now = datetime.datetime.now()
    #html = "<html><body>It is now %s.</bode></html>" % now
    #return HttpResponse(html)
    now = datetime.datetime.now()
    #t = Template('<html><body>Now is {{current_date}}.</body></html>')
    t = get_template('current_datetime.html')
    c = Context({'current_date':now})
    html = t.render(c)
    return HttpResponse(html)
'''

def current_datetime(request,template_name):
    now = datetime.datetime.now()
    return render_to_response(template_name,{'current_date':now})
def hours_ahead(request,houroffset):
    try:
        houroffset = int(houroffset)
    except ValueError:
        raise Http404()
    dt = datetime.datetime.now() + datetime.timedelta(hours = houroffset)
    #assert False
    html = "<html><body>In %s hour(s), it will be %s.</body></html>" %(houroffset,dt)
    return HttpResponse(html)

def ua_display_good1(request):
    try:
        ua = request.META['HTTP_USER_AGENT']
    except KeyError:
        ua = 'unknown'
    return HttpResponse("Your browser is %s"% ua)

def ua_display_good2(request):
    ua = request.META.get('HTTP_USER_AGENT','unknown')
    return HttpResponse("YOur browser is %s" %ua)

def display_meta(request):
    values = request.META.items()
    values.sort()
    #print values

    #for k,v in values:
    #    html.append('<tr><td>%s</td><td>%s</td></tr>' %(k,v))
    return render_to_response('show_meta.html',{'html':values})#HttpResponse('<table>%s</table>'%'\n'.join(html))


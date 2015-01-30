import os, uuid
from pyramid.view import view_config
from pyramid.response import Response
from pyramid.httpexceptions import HTTPSeeOther
from pyramid_storage.exceptions import FileNotAllowed


#http://pomoyka.homelunux.net/files/dude_docking_set.pdf

@view_config(route_name='home', renderer='templates/template_base.mak')
def base_view(request):
    tpldef = {'mess': request.session.pop_flash()}
    return tpldef

@view_config(route_name='storefile', request_method='POST')
def store_file_view(request):
    try:
        if request.POST['anyfile'].filename:
            print(request.POST['anyfile'].filename)
            filename = request.storage.save(request.POST['anyfile'])
            fileurl = request.storage.url(filename)
            request.session.flash(fileurl)
        
    except FileNotAllowed:
        request.session.flash('Sorry, this file is not allowed')
    
    return HTTPSeeOther(request.route_url('home'))
    

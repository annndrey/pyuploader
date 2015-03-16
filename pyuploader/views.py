import os, uuid, smtplib
import pygeoip
from email.mime.text import MIMEText
from email.header import Header
from pyramid.view import view_config
from pyramid.response import Response
from pyramid.httpexceptions import HTTPSeeOther
from pyramid_storage.exceptions import FileNotAllowed

fr='piggy@piggy.thruhere.net'
to='gontchar@gmail.com'

msg="""Someone has sent something ({0}) from {1}"""

@view_config(route_name='home', renderer='templates/template_base.mak')
def base_view(request):
    tpldef = {}
    mess = request.session.pop_flash()

    try:
        tpldef.update({'mess': mess[-1]})
    except:
        pass
    return tpldef

@view_config(route_name='storefile', request_method='POST')
def store_file_view(request):

    try:
        if request.POST['anyfile'].filename:
            keepforever = request.params.get('keepforever', None)
            if keepforever is not None:
                fldr = 'immortal'
            else:
                fldr = 'files'
            
            filename = request.storage.save(request.POST['anyfile'], folder=fldr,  randomize=True)
            fileurl = request.storage.url(filename)
            sessionmessage = """<a href="{0}">{1}</a>""".format(fileurl, request.POST['anyfile'].filename)
            request.session.flash(sessionmessage)
            serv=smtplib.SMTP('localhost')
            
            here = os.path.dirname(__file__)
            geoipfile = os.path.join(here, "static", "geoip.dat")
            gi = pygeoip.GeoIP(geoipfile)
            addrdata = gi.record_by_addr(request.remote_addr)
            if addrdata:
                mailmessage = msg.format(fileurl, ", ".join([request.remote_addr,  addrdata['city'], addrdata['country_name']]))
            else:
                mailmessage = msg.format(fileurl, request.remote_addr)
            tosend = MIMEText(mailmessage, _charset="UTF-8")
            tosend['Subject'] = Header("PIGGY upload", "utf-8")
            serv.sendmail(fr, to, tosend.as_string())
            serv.quit()

    except FileNotAllowed:
        request.session.flash('Sorry, this file is not allowed')
    
    return HTTPSeeOther(request.route_url('home'))
    

from pyramid.config import Configurator
from pyramid.session import SignedCookieSessionFactory

def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    my_session_factory = SignedCookieSessionFactory('secretsession')
    config = Configurator(settings=settings, session_factory=my_session_factory)
    config.include('pyramid_mako')
    config.include('pyramid_storage')
    config.add_static_view('static', 'static', cache_max_age=3600)
    config.add_route('home', '/')
    config.add_route('storefile', '/upload')
    config.scan()
    return config.make_wsgi_app()

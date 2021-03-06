import os
import pyramid_zcml
from pyramid.config import Configurator
from cone.app import auth_tkt_factory, acl_factory
from cone.ugm.model import get_root
from cone.ugm.model.utils import APP_PATH

def main(global_config, **settings):
    """Returns WSGI application.
    """
    import cone.app.security as security
    security.ADMIN_USER = settings.get('cone.admin_user', 'admin')
    security.ADMIN_PASSWORD = settings.get('cone.admin_password', 'admin')
    secret_password = settings.get('cone.secret_password', 'secret')
    authn_factory = settings.get('cone.authn_policy_factory', auth_tkt_factory)
    authz_factory = settings.get('cone.authz_policy_factory', acl_factory)
    config = Configurator(
        root_factory=get_root,
        settings=settings,
        authentication_policy=authn_factory(secret=secret_password,
                                            max_age=43200,
                                            include_ip=True),
        authorization_policy=authz_factory(secret=secret_password),
        autocommit=True)
    zcml_file = settings.get('configure_zcml', 'configure.zcml')
    config.include(pyramid_zcml)
    config.begin()
    config.load_zcml(zcml_file)

    theme_dir = os.path.join(APP_PATH, 'etc', 'theme', '')
    theme_css = os.path.join(APP_PATH, 'etc', 'theme', 'theme.css')
    if os.path.isdir(theme_dir):
        config.add_static_view('theme', theme_dir)
    if os.path.isfile(theme_css):
        import cone.app.browser
        cone.app.browser.ADDITIONAL_CSS.append('theme/theme.css')

    config.end()
    return config.make_wsgi_app()

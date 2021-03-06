from odict import odict
from zope.interface import implements
from cone.app.model import (
    FactoryNode,
    Properties,
    BaseMetadata,
)
from cone.ugm.model.interfaces import IUgm
from cone.ugm.model.users import Users
from cone.ugm.model.groups import Groups
from cone.ugm.model.settings import Settings


class Ugm(FactoryNode):
    implements(IUgm)

    factories = odict((
        ('users', Users),
        ('groups', Groups),
        ('settings', Settings),
    ))

    @property
    def properties(self):
        props = Properties()
        props.in_navtree = False
        props.editable = False
        props.mainmenu_empty_title = True
        props.default_child = 'users'
        return props

    @property
    def metadata(self):
        metadata = BaseMetadata()
        metadata.title = "ugm"
        return metadata

    def __init__(self, *args, **kw):
        super(Ugm, self).__init__(*args, **kw)
        # XXX: currently the ldap users and groups need to know
        # mutually about themselves. Feels like node.ext.ugm should
        # present us the combo.
        self['users'].ldap_users.groups = self['groups'].ldap_groups
        self['groups'].ldap_groups.users = self['users'].ldap_users

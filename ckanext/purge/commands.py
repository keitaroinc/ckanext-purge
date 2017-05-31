import sys
from pprint import pprint

from ckan import model
from ckan.logic import get_action, ValidationError

import ckan.lib.base as base
import ckan.model as model

from ckan.lib.cli import CkanCommand

class Purger(CkanCommand):
    '''Purges all the deleted datasets
    
    Usage:

      purger purgeall 
        - Purges all of the deleted datasets

      purger showdeleted
        - Displays the datasets marked as deleted

    The commands should be run from the ckanext-harvest directory and expect
    a development.ini file to be present. Most of the time you will
    specify the config explicitly though::

        paster purger purgeall --config=../ckan/development.ini

    '''

    summary = __doc__.split('\n')[0]
    usage = __doc__
    max_args = 1
    min_args = 0

    def __init__(self,name):

        super(Purger,self).__init__(name)

    def command(self):
        self._load_config()

        # We'll need a sysadmin user to perform most of the actions
        # We will use the sysadmin site user (named as the site_id)
        context = {'model':model,'session':model.Session,'ignore_auth':True}
        self.admin_user = get_action('get_site_user')(context,{})


        print ''

        if len(self.args) == 0:
            self.parser.print_usage()
            sys.exit(1)
        cmd = self.args[0]
        if cmd == 'purgeall':
            self.purge_all()
        elif cmd == 'showdeleted':
            self.show_deleted()
        else:
            print 'Command %s not recognized' % cmd

    def _load_config(self):
        super(Purger, self)._load_config()

    def purge_all(self):
        import ckan.lib.cli as c
        purge_queue = self.show_deleted()

        for el in purge_queue:
            site_user = get_action('get_site_user')({'ignore_auth': True}, {})
            context = {'user': site_user['name']}
            get_action('dataset_purge')(
                context, {'id': el})
            print '%s purged' % el

    def show_deleted(self):
        c = base.c
        request = base.request
        _ = base._

        c.deleted_packages = model.Session.query(
            model.Package).filter_by(state=model.State.DELETED)
        marked_deleted = []
        for pkg in c.deleted_packages:
            marked_deleted.append(pkg.id)
        print marked_deleted

        return marked_deleted

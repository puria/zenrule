# -*- coding: utf-8 -*-

from tg import expose, flash, require, url, lurl
from tg import request, redirect, tmpl_context
from tg.i18n import ugettext as _, lazy_ugettext as l_
from tg.exceptions import HTTPFound
from tg import predicates
from zenrule import model
from tgext.admin.mongo import BootstrapTGMongoAdminConfig as TGAdminConfig
from tgext.admin.controller import AdminController

from zenrule.controllers.rule import RuleController
from zenrule.lib.base import BaseController
from zenrule.controllers.error import ErrorController

__all__ = ['RootController']


class RootController(BaseController):
    admin = AdminController(model, None, config_type=TGAdminConfig)
    rules = RuleController()
    error = ErrorController()

    def _before(self, *args, **kw):
        tmpl_context.project_name = "zenrule"

    @expose('zenrule.templates.index')
    def index(self):
        return dict(page='index')

    @expose('zenrule.templates.login')
    def login(self, came_from=lurl('/'), failure=None, login=''):
        if failure is not None:
            if failure == 'user-not-found':
                flash(_('User not found'), 'error')
            elif failure == 'invalid-password':
                flash(_('Invalid Password'), 'error')

        login_counter = request.environ.get('repoze.who.logins', 0)
        if failure is None and login_counter > 0:
            flash(_('Wrong credentials'), 'warning')

        return dict(page='login', login_counter=str(login_counter),
                    came_from=came_from, login=login)

    @expose()
    def post_login(self, came_from=lurl('/')):
        if not request.identity:
            login_counter = request.environ.get('repoze.who.logins', 0) + 1
            redirect('/login',
                     params=dict(came_from=came_from, __logins=login_counter))
        userid = request.identity['repoze.who.userid']
        flash(_('Welcome back, %s!') % userid)

        # Do not use tg.redirect with tg.url as it will add the mountpoint
        # of the application twice.
        return HTTPFound(location=came_from)

    @expose()
    def post_logout(self, came_from=lurl('/')):
        """
        Redirect the user to the initially requested page on logout and say
        goodbye as well.

        """
        flash(_('We hope to see you soon!'))
        return HTTPFound(location=came_from)

# -*- coding: utf-8 -*-

import random
import time
import logging
from openerp.osv import fields, osv

_logger = logging.getLogger(__name__)

SUPERUSER_ID = 1


def generate_token():
    chars = '0123456789'
    time_stamp = str(int(time.time() * 1000))
    return time_stamp + ''.join(random.choice(chars) for i in xrange(16 - len(time_stamp)))


class res_users(osv.osv):
    _inherit = 'res.users'

    _columns = {
        'access_token': fields.char('Access Token', required=True)
    }

    def _login(self, db, login, password):
        cr = self.pool.cursor()
        try:
            res = self.search(cr, SUPERUSER_ID, [('access_token', '=', password)])
            if res and not login:
                user_id = res[0]
                _logger.info("Login success, user_id: %s", user_id)
            else:
                return super(res_users, self)._login(db, login, password)
        finally:
            cr.close()

        return user_id

    def check_credentials(self, cr, uid, password):
        res = self.search(cr, SUPERUSER_ID, [('access_token', '=', password)])
        if not res:
            return super(res_users, self).check_credentials(cr, uid, password)

    def create(self, cr, user, vals, context=None):
        vals['access_token'] = generate_token()
        return osv.osv.create(self, cr, user, vals, context)


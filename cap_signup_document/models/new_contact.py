from odoo import api, fields, models, _
from odoo.exceptions import UserError

# override do_signup method to allow referred_by_id to be set from sign-up form
class AuthSignupHome(models.Model):
    def do_signup(self, qcontext):
        """ Shared helper that creates a res.partner out of a token """
        values = dict((key, qcontext.get(key)) for key in ('login', 'name', 'password', 'x_studio_additional_info'))
        assert any([k for k in values.values()]), "The form was not properly filled in."
        assert values.get('password') == qcontext.get('confirm_password'), "Passwords do not match; please retype them."
        self._signup_with_values(qcontext.get('token'), values)
        request.cr.commit()

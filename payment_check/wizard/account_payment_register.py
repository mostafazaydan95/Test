# -*- coding: utf-8 -*-
# Part of BrowseInfo. See LICENSE file for full copyright and licensing details.
##############################################################################

from odoo import api, fields, models

class RegisterPayment(models.TransientModel):
	
	_inherit = 'account.payment.register'
	check_number = fields.Char('Cheque Number')
	journal_type = fields.Selection([('sale', 'Sales'),('purchase', 'Purchase'),('cash', 'Cash'),('bank', 'Bank'),('general', 'Miscellaneous')],related="journal_id.type")

	def _create_payment_vals_from_wizard(self):
		payment_vals = super(RegisterPayment, self)._create_payment_vals_from_wizard()
		payment_vals['check_number'] = self.check_number
		return payment_vals

# -*- coding: utf-8 -*-
# Part of BrowseInfo. See LICENSE file for full copyright and licensing details.
##############################################################################

from odoo import api, fields, models

class Payment(models.Model):
	
	_inherit = 'account.payment'
	_order = "id desc"
	check_number = fields.Char('Cheque Number')

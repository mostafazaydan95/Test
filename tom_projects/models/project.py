# -*- coding: utf-8 -*-

from odoo import fields, models, api
from datetime import datetime


class Project(models.Model):

	_inherit = 'project.project'
	date_end = fields.Date('End Date')
	trees_per_donum = fields.Integer('Trees/Donum')
	number_of_trees = fields.Integer('Number of trees', compute="_compute_total_trees")
	planting_type = fields.Char('Type of plantings')
	spraying_date = fields.Date('Spraying Date')
	spraying_medication_date = fields.Date('Spraying Med Date')
	irrigation_date = fields.Date('Irrigation Date')
	land_area = fields.Integer('Land Area (Donum)')
	#state = fields.Selection([('open','Open'),('done','Done')],string='State',required=True, readonly=True, copy=False, tracking=True, default='open')
	tree_configurator_ids = fields.One2many('tree.configurator','project_id',string='Tree Configuration')
	tree_configurator_count = fields.Integer(compute="_compute_tree_configurator_number")

	def _compute_tree_configurator_number(self):
		for record in self:
			record.tree_configurator_count = len(record.tree_configurator_ids)

	@api.depends('trees_per_donum', 'land_area')
	def _compute_total_trees(self):
		for record in self:
			record['number_of_trees'] = record.trees_per_donum * record.land_area


	def action_view_configuration(self):
		self.ensure_one()
		tree_view = self.env.ref('tom_projects.tree_configurator_tree')
		form_view = self.env.ref('tom_projects.tree_configurator_form')
		ctx = {}
		ctx['default_project_id'] = self.id
		res = {
		'type': 'ir.actions.act_window',
		'name': 'Years',
		'view_mode': 'tree, form',
		'res_model': 'tree.configurator',
		'views': [(tree_view.id, 'list'),(form_view.id, 'form')],
		'domain' : [('id','in',self.tree_configurator_ids.ids)],
		'target': 'current',
		'context': ctx,
		}

		return res





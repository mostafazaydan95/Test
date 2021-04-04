# -*- coding: utf-8 -*-

from odoo import fields, models, api


class TreeConfigurator(models.Model):
	_name = 'tree.configurator'

	@api.model
	def year_selection(self):
		year = 2000
		year_list = []
		while year != 2050:
			year_list.append((str(year), str(year)))
			year += 1

		return year_list

	year = fields.Selection(
		year_selection,
		string="Year",
		default="2019"
		)

	production_per_tree = fields.Float('Production/Tree (kg)')
	project_id = fields.Many2one('project.project', 'Project')
	price_per_kilo = fields.Monetary('Price per kilo',currency_field="currency_id")
	currency_id = fields.Many2one('res.currency',related="project_id.company_id.currency_id")
	donum_production = fields.Float('Donum Prod (Kg)', store=True, compute="_compute_total")
	total_land_production = fields.Float('Total Land Prod (Kg)', compute="_compute_total", store=True)
	land_income = fields.Monetary('Land Income',currency_field="currency_id",compute="_compute_total", store=True)
	administrative_expenses = fields.Monetary('Administrative Expenses',currency_field="currency_id")
	other_expenses = fields.Monetary('Other Expenses',currency_field="currency_id")
	agricultural_tax_id = fields.Many2one('account.tax','Agricultural tax')
	profit_before_tax = fields.Monetary('Profit Before Tax', currency_field="currency_id",compute="_compute_profit", store=True)
	profit_after_tax = fields.Monetary('Profit After Tax',currency_field="currency_id",compute="_compute_profit", store=True)
	tom_projects_profit = fields.Monetary('Tom Projects Profit (20%)',currency_field="currency_id",compute="_compute_profit", store=True)
	owner_land_profit = fields.Monetary('Land Owner Profit (80%)',currency_field="currency_id",compute="_compute_profit", store=True)

	@api.depends('project_id', 'year')
	def name_get(self):
		result = []
		for record in self:
			name = record.project_id.name + ' - ' + record.year
			result.append((record.id, name))

		return result


	@api.depends('project_id.number_of_trees', 'project_id.trees_per_donum', 'production_per_tree', 'price_per_kilo')
	def _compute_total(self):
		for record in self:
			record.total_land_production = record.land_income = record.donum_production = 0
			
			production_per_tree = record.production_per_tree
			price_per_kilo = record.price_per_kilo

			record.donum_production = production_per_tree * record.project_id.trees_per_donum
			record.total_land_production = production_per_tree * record.project_id.number_of_trees
			record.land_income = production_per_tree * record.project_id.number_of_trees * price_per_kilo

	@api.depends('administrative_expenses', 'other_expenses','land_income', 'agricultural_tax_id')
	def _compute_profit(self):
		for record in self:
			record.profit_before_tax = record.profit_after_tax = 0
			total_expenses = record.administrative_expenses + record.other_expenses

			profit_before_tax = record.land_income - total_expenses
			
			record.profit_before_tax = profit_before_tax

			amount = (record.land_income * record.agricultural_tax_id.amount) / 100
			profit_after_tax = profit_before_tax - amount
			record.profit_after_tax = profit_after_tax

			record.tom_projects_profit = (profit_after_tax * 20) / 100
			record.owner_land_profit = (profit_after_tax * 80) / 100



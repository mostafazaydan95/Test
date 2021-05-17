# -*- coding: utf-8 -*-
# from odoo import http


# class PaymentCheck(http.Controller):
#     @http.route('/payment_check/payment_check/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/payment_check/payment_check/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('payment_check.listing', {
#             'root': '/payment_check/payment_check',
#             'objects': http.request.env['payment_check.payment_check'].search([]),
#         })

#     @http.route('/payment_check/payment_check/objects/<model("payment_check.payment_check"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('payment_check.object', {
#             'object': obj
#         })

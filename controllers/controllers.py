# -*- coding: utf-8 -*-
from odoo import http

# class VitCogserviceApplvl(http.Controller):
#     @http.route('/vit_cogservice_applvl/vit_cogservice_applvl/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/vit_cogservice_applvl/vit_cogservice_applvl/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('vit_cogservice_applvl.listing', {
#             'root': '/vit_cogservice_applvl/vit_cogservice_applvl',
#             'objects': http.request.env['vit_cogservice_applvl.vit_cogservice_applvl'].search([]),
#         })

#     @http.route('/vit_cogservice_applvl/vit_cogservice_applvl/objects/<model("vit_cogservice_applvl.vit_cogservice_applvl"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('vit_cogservice_applvl.object', {
#             'object': obj
#         })
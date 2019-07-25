# -*- coding: utf-8 -*-
from odoo import http

# class XmartsSeip(http.Controller):
#     @http.route('/xmarts_seip/xmarts_seip/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/xmarts_seip/xmarts_seip/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('xmarts_seip.listing', {
#             'root': '/xmarts_seip/xmarts_seip',
#             'objects': http.request.env['xmarts_seip.xmarts_seip'].search([]),
#         })

#     @http.route('/xmarts_seip/xmarts_seip/objects/<model("xmarts_seip.xmarts_seip"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('xmarts_seip.object', {
#             'object': obj
#         })
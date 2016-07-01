# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    This module copyright :
#        (c) 2016 SDI
#                 Juan Carlos Montoya <jcmontoya@sdi.es>
#                 Javier Garcia <jgarcia@sdi.es>
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

{
    "name": "POS Invoice auto reconcile",
    "version": "8.0.0.1.0",
    "author": "Juan Carlos Montoya,"
              "Javier Garcia,"
              "Odoo Community Association (OCA)",
    "website": "http://sdi.es",
    "license": "AGPL-3",
    "category": "Accounting",
    'summary': """
        - Automatically Reconcile invoiced POS orders
    """,
    "depends": [
        'point_of_sale',
    ],
    "installable": True,
}

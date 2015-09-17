# -*- coding: utf-8 -*-
##############################################################################
#
#    Job offer letter
#    Copyright (C) 2015 BrowseInfo(<http://www.browseinfo.in>).
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
    'name': 'Hr Report',
    'version': '1.0',
    'category': 'Hr',
    'sequence': 4,
    'summary': 'Hr Report',
    'description': """
    """,
    'author': 'BrowseInfo',
    'website': 'http://www.browseinfo.in',
    'images': ['pic.png'],
    'depends': ['hr_recruitment', 'base', 'hr', 'email_template', 'report'],
    'data': ['report.xml',
             'wizard/wizard_job_letter_view.xml',
             'wizard/wizard_exp_letter_view.xml',
             'wizard/wizard_reliving_letter_view.xml',
             'views/report_exp_letter.xml',
             'views/report_reliving_letter.xml',
             'views/report_job_offer_letter.xml'],
    'demo': [],
    'test': [],
    'installable': True,
    'auto_install': False,
    'application': True,
}

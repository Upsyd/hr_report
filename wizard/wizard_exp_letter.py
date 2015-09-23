# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2004-2010 BrowseInfo  (<http://www.browseinfo.in>).
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

from openerp.osv import osv
from openerp.osv import fields
from datetime import date

class wizard_exp_letter(osv.osv_memory):
    _name = 'wizard.exp.letter'

    def default_get(self, cr, uid, fields, context=None):
        res = super(wizard_exp_letter, self).default_get(cr, uid, fields,
                                                         context=context)
        record_id = context and context.get('active_id', False) or False
        emp_pool = self.pool.get('hr.employee')
        obj = emp_pool.browse(cr, uid, record_id, context=context)
        res.update({'print_by': uid, 'employee': obj.name,
                    'job_title': obj.job_id.name})
        return res
    
    def print_mail_exp_letter(self, cr, uid, ids, context=None):
        if context is None:
            context = {}
        data = self.read(cr, uid, ids, context=context)[0]
        context.update({'wiz_ids':ids,'print_header':True})
        id_list = []
        id_list.append(context.get('active_id'))
        email_obj = self.pool.get('email.template')
        ctx = context.copy()
        ctx.update({'active_model': 'hr.employee'})
        datas = {
            'ids': id_list,
            'model': 'hr.employee',
            'form': data
        }
        template_id = self.pool.get('ir.model.data').get_object_reference(
            cr, uid, 'hr_report', 'email_template_exp_letter')[1]
        
        return email_obj.send_mail(cr, uid, template_id, id_list[0], True, context=ctx)
            
    
    def print_exp_letter(self, cr, uid, ids, context=None):
        if context is None:
            context = {}
        context.update({'wiz_ids':ids,'print_header':True})
        data = self.read(cr, uid, ids, context=context)[0]
        self.pool['report'].get_action(cr, uid, [], 'hr_report.report_exp_letter_document', data=data, context=context)
        id_list = []
        id_list.append(context.get('active_id'))
        ctx = context.copy()
        ctx.update({'active_model': 'hr.employee'})
        #ty =self.pool['report'].get_action(cr, uid, [], 'hr_report.report_exp_letter_document', data=data, context=context)
        
        datas = {
            'ids': id_list,
            'model': 'hr.employee',
            'form': data
        }
        return self.pool['report'].get_action(cr, uid, [], 'hr_report.report_exp_letter_document', data=datas, context=context)
    
    def print_exp_letter_without(self, cr, uid, ids, context=None):
        if context is None:
            context = {}
        context.update({'wiz_ids':ids,'print_header':False})
        data = self.read(cr, uid, ids, context=context)[0]
        self.pool['report'].get_action(cr, uid, [], 'hr_report.report_exp_letter_document', data=data, context=context)
        id_list = []
        id_list.append(context.get('active_id'))
        ctx = context.copy()
        ctx.update({'active_model': 'hr.employee'})
        #ty =self.pool['report'].get_action(cr, uid, [], 'hr_report.report_exp_letter_document', data=data, context=context)
        
        datas = {
            'ids': id_list,
            'model': 'hr.employee',
            'form': data
        }
        return self.pool['report'].get_action(cr, uid, [], 'hr_report.report_exp_letter_document', data=datas, context=context)
    
    _columns = {
        "print_by": fields.many2one('res.users', 'Print By'),
        "start_date": fields.date('Start Date'),
        "end_date": fields.date('End Date'),
        "employee": fields.char("Employee"),
        "job_title": fields.char("Job Title"),
        }

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:

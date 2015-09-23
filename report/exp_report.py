# -*- coding: utf-8 -*-
import time
from openerp.osv import osv
from openerp.report import report_sxw


class exp_report(report_sxw.rml_parse):

    def __init__(self, cr, uid, name, context=None):
        super(exp_report, self).__init__(cr, uid, name, context=context)
        self.context = context
        self.localcontext.update({
                                  'get_data' : self.get_data,
                                  'get_data_reliving' : self.get_data_reliving,
                                  'get_data_job' : self.get_data_job
        })
    def get_data_job(self):
        wiz_bro_rec = self.pool.get('wizard.job.letter').browse(self.cr,self.uid,self.context.get('wiz_ids'))
        data = {
                'wiz_bro_rec' : wiz_bro_rec,
                'print_header' : self.context.get('print_header')
                }
        return data
    
    def get_data_reliving(self):
        wiz_bro_rec = self.pool.get('wizard.reliving.letter').browse(self.cr,self.uid,self.context.get('wiz_ids'))
        data = {
                'wiz_bro_rec' : wiz_bro_rec,
                'print_header' : self.context.get('print_header')
                }
        return data
    
    def get_data(self):
        wiz_bro_rec = self.pool.get('wizard.exp.letter').browse(self.cr,self.uid,self.context.get('wiz_ids'))
        data = {
                'wiz_bro_rec' : wiz_bro_rec,
                'print_header' : self.context.get('print_header')
                }
        return data
    
class report_agedpartnerbalance(osv.AbstractModel):
    _name = 'report.hr_report.report_exp_letter_document'
    _inherit = 'report.abstract_report'
    _template = 'hr_report.report_exp_letter_document'
    _wrapped_report_class = exp_report
    
class report_job_letter(osv.AbstractModel):
    _name = 'report.hr_report.report_job_letter_document'
    _inherit = 'report.abstract_report'
    _template = 'hr_report.report_job_letter_document'
    _wrapped_report_class = exp_report

class report_reliving_letter(osv.AbstractModel):
    _name = 'report.hr_report.report_reliving_letter_document'
    _inherit = 'report.abstract_report'
    _template = 'hr_report.report_reliving_letter_document'
    _wrapped_report_class = exp_report

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:

__author__ = 'ssinha'
"""
" Copyright:    Loggly, Inc.
" Author:       Sandip Sinha
" Email:        ssinha@loggly.com
" Note:         This is to introduce all SFDC interactions in Loggly using REST APIs for the first time. This will continue'
"               to evolve as more and more programs will need to be interfaced with SFDC.
"""

from simple_salesforce import Salesforce, SalesforceResourceNotFound
from logglyrestsfdc import sfdcconfig
from simple_salesforce.login import SalesforceLogin
from logglyrestsfdc.helper.exceptions import SFDCRestExceptions
SUCCESS_STATUS_CODE=204


class sfdcrestClient(object):
    userid = None
    passwd = None
    security_token = None
    sandbox = None
    sf_instance = None
    session_id = None

    def __init__(self, userid=sfdcconfig.get('sfdc','userid'), passwd = sfdcconfig.get('sfdc','passwd'),
                 security_token = sfdcconfig.get('sfdc','security_token'), sandbox=sfdcconfig.get('sfdc','sandbox'),
                 instance=None):
        assert(sfdcconfig.get('sfdc','userid') is not None)
        assert(sfdcconfig.get('sfdc','passwd') is not None)
        assert(sfdcconfig.get('sfdc','security_token') is not None)
        self.userid = sfdcconfig.get('sfdc','userid')
        self.passwd = sfdcconfig.get('sfdc','passwd')
        self.security_token = sfdcconfig.get('sfdc','security_token')
        self.sandbox = sfdcconfig.get('sfdc','sandbox')
        if sfdcconfig.get('sfdc','sandbox'):
            self.sf_instance = Salesforce(
                username=self.userid,
                password=self.passwd,
                security_token=self.security_token,
                sandbox=True)
        else:
            self.sf_instance = Salesforce(
                username=self.userid,
                password=self.passwd,
                security_token=self.security_token)


    def execute(self, event, *args, **kwargs):
        method_map={
                'get-opportunity':self.get_opportunity,
                'update-opportunity':self.update_opportunity,
                   }
        result = method_map[event](*args, **kwargs)
        return result

    def get_opportunity(self, custom_id_field, custom_id):
        try:
            result = self.sf_instance.Opportunity.get_by_custom_id(custom_id_field, custom_id)
            return result
        except SFDCRestExceptions as e:
            raise Exception({'messages': e.message,'code':e.code})
            return None



    def update_opportunity(self, record_id, data):
        """
        Arguments:
        * record_id -- the Id of the SObject to update
        * data -- a dict of the data to update the SObject from.
        """

        try:
            updatestatus = self.sf_instance.Opportunity.update(record_id,data)
            if updatestatus == SUCCESS_STATUS_CODE:
                return True
        except SFDCRestExceptions as e:
            raise Exception({'messages': e.message,'code':e.code})
            return false










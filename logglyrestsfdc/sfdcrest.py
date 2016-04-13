__author__ = 'ssinha'
"""
" Copyright:    Loggly, Inc.
" Author:       Sandip Sinha
" Email:        ssinha@loggly.com
" Note:         This is to introduce all SFDC interactions in Loggly using REST APIs for the first time. This will continue'
"               to evolve as more and more programs will need to be interfaced with SFDC.
"""

from simple_salesforce import Salesforce, SalesforceResourceNotFound, SalesforceMoreThanOneRecord
from logglyrestsfdc.helper.exceptions import SFDCRestExceptions
SUCCESS_STATUS_CODE=204
import config
import collections


class sfdcrestClient(object):
    userid = None
    passwd = None
    security_token = None
    sandbox = None
    sf_instance = None
    session_id = None

    def __init__(self, env):
        settings = getattr( config, env )
        configp = collections.namedtuple('configp', 'username passwd security_token')
        rs =  configp( username = settings['username'], passwd = settings['password'], security_token = settings['token'])
        assert(rs.username is not None)
        assert(rs.passwd is not None)
        assert(rs.security_token is not None)
        self.userid = rs.username
        self.passwd = rs.passwd
        self.security_token = rs.security_token
        if env == 'sandbox':
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
                'create-opportunity':self.create_opportunity,
                'delete-opportunity':self.delete_opportunity,
                'get-contact':self.get_contact,
                'update-contact':self.update_contact,
                   }
        result = method_map[event](*args, **kwargs)
        return result

    def get_opportunity(self, custom_id_field, custom_id):
        try:
            result = self.sf_instance.Opportunity.get_by_custom_id(custom_id_field, custom_id)
            return result
        except SFDCRestExceptions as e:
            print ('Resource errored out')
            return None
        except SalesforceResourceNotFound as e:
            print ('Resource errored out')
            return None
        except SalesforceMoreThanOneRecord as e:
            print 'More than 1 contact found'
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
            print ('Resource errored out')
            return false


    def create_opportunity(self, record_id, data):
        """
        Arguments:
        * record_id -- the Id of the SObject to update
        * data -- a dict of the data to update the SObject from.
        """
        if isinstance(data, dict) and 'Subdomain__c' in data:

            try:
                insertstatus = self.sf_instance.Opportunity.create(data)
                if insertstatus.success:
                    return True
            except SFDCRestExceptions as e:
                print ('Resource errored out')
                return false

        else:
            print 'Not enough data to create a SFDC Opportunity'
            return False

    def delete_opportunity(self, Id):
        """
        Arguments:
        * record_id -- the Id of the SObject to delete
        """
        try:
            deletestatus = self.sf_instance.Opportunity.create(data)
            if deletestatus == SUCCESS_STATUS_CODE:
                 return True
        except SFDCRestExceptions as e:
            print ('Resource errored out')
            return False

    def get_contact(self,custom_name, custom_value):
        """
        Arguments:
        custom_name: Name of the field
        custom_value: Value of the field
        """
        try:
            result = self.sf_instance.Contact.get_by_custom_id(custom_name, custom_value)
            return result
        except SFDCRestExceptions as e:
            print ('Resource errored out')
            return None
        except SalesforceResourceNotFound as e:
            print ('Resource Not Found')
            return None
        except SalesforceMoreThanOneRecord as e:
            print 'More than 1 contact found'
            return None


    def update_contact(self,contactId, uodateValues):
        """
        Arguments:
        contactId: Contact ID
        Contact_value: A dict of the fields that need to be updated
        """
        try:
            result = self.sf_instance.Contact.update(contactId, uodateValues)
            return result
        except SFDCRestExceptions as e:
            print ('Resource Not Found')
            return None











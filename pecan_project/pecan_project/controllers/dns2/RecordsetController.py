'''
Date:2021/3/19
Author:Guoyha
'''
import pecan

from webob.exc import status_map
from pecan_project.controllers.dns2.zdns_driver import dns_zone_driver


class RecordsetController(object):
    
    def __init__(self):
        self.msg='msg'
        self.manager = dns_zone_driver.get_instance()

    @pecan.expose('json')
    def index(self):
        return {"Information": "The url is for RRS base RestApi "
                "interface"}

    # http://127.0.0.1:8080/dns2/rrs/list?views_id=123&zones_id=123
    @pecan.expose('json')
    def list(self,**args):
        if args.get('view_id',-1) or args.get('zone_id',-1):
            self.view_id=args.get('view_id')
            self.zone_id=args.get('zone_id')
        else:
            return self.return_msg('error', 'view_id or zone_id is inqure', None)
        
        return str(args)

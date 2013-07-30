# -*- coding: utf-8 -*-
base_url_api_v3 = 'http://localhost:35357/v3'
verify = False
admin_token = 'password'
user01_userid = 'user01'
user01_password = 'password'
default_domain_id = 'default'
default_domain_name = 'default'
shared_domain_name = 'shared'
net_domain_name = 'net'
com_domain_name = 'com'
default_project_id = 'default'
default_project_name = 'default'
x_project_name = 'projectx'
y_project_name = 'projecty'
z_project_name = 'projectz'

auth_payload_domain_name_project_name = {'auth': {'identity': {'methods': ['password'],
                                                               'password': {'user': {'id': 'user01',
                                                                                     'password': 'password'}}},
                                                  'scope': {'project': {'domain': {'name': 'default'},
                                                                        'name': 'default'}}}}

auth_payload_domain_name_project_id = {'auth': {'identity': {'methods': ['password'],
                                                             'password': {'user': {'id': 'user01',
                                                                                   'password': 'password'}}},
                                                'scope': {'project': {'domain': {'name': 'default'},
                                                                      'id': 'default'}}}}

auth_payload_domain_id_project_name = {'auth': {'identity': {'methods': ['password'],
                                                             'password': {'user': {'id': 'user01',
                                                                                   'password': 'password'}}},
                                                  'scope': {'project': {'domain': {'id': 'default'},
                                                                        'name': 'default'}}}}

auth_payload_domain_id_project_id = {'auth': {'identity': {'methods': ['password'],
                                                           'password': {'user': {'id': 'user01',
                                                                                 'password': 'password'}}},
                                              'scope': {'project': {'domain': {'id': 'default'},
                                                                    'id': 'default'}}}}

auth_payload_domain_id = {'auth': {'identity': {'methods': ['password'],
                                                'password': {'user': {'domain': {'id': 'default'},
                                                                      'id': 'user01',
                                                                      'password': 'password'}}}}}

auth_payload_domain_name = {'auth': {'identity': {'methods': ['password'],
                                                  'password': {'user': {'domain': {'name': 'default'},
                                                                        'id': 'user01',
                                                                        'password': 'password'}}}}}

auth_payload = {'auth': {'identity': {'methods': ['password'],
                                      'password': {'user': {'id': 'user01',
                                                            'password': 'password'}}}}}
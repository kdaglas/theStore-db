from tests.test_base import Testing
from run import app
from flask import jsonify, json


class TestAttendant(Testing):

    def test_for_invalid_url(self):
        '''testing for invalid url '''
        admin = self.adminlogin()
        resp = self.app.post("/api/v2/auth/sign",
                             content_type='application/json', 
                             headers=dict(Authorization='Bearer '+admin['token']),
                             data=Testing.registering_attendant )
        self.assertEqual(resp.status_code, 405)
        self.assertIn(b"Please put a valid URL", resp.data)


    def test_for_method_not_allowed(self):
        ''' test for method not allowed '''
        admin = self.adminlogin()
        resp = self.app.post("/api/v2/auth/signup/76446",
                             content_type='application/json', 
                             headers=dict(Authorization='Bearer '+admin['token']),
                             data=Testing.registering_attendant )
        self.assertEqual(resp.status_code, 405)
        self.assertIn(b"Method not allowed", resp.data)


    def test_add_user_with_invalid_field(self):
        '''testing for invalid fields '''
        admin = self.adminlogin()
        resp = self.app.post("/api/v2/auth/signup",
                             content_type='application/json', 
                             headers=dict(Authorization='Bearer '+admin['token']),
                             data=Testing.wrong_afields)
        self.assertEqual(resp.status_code, 400)
        self.assertIn(b"Some fields are missing, please check", resp.data)


    # def test_user_reg_successful(self):
    #     '''testing for successful '''
    #     admin = self.adminlogin()
    #     resp = self.app.post("/api/v2/auth/signup",
    #                          content_type='application/json', 
    #                          headers=dict(Authorization='Bearer '+admin['token']),
    #                          data=Testing.registering_attendant )
    #     self.assertEqual(resp.status_code, 201)
    #     self.assertIn(b"You have successfully added Douglas", resp.data)

    
    def test_add_user_with_empty_name(self):
        '''testing for space '''
        admin = self.adminlogin()
        resp = self.app.post("/api/v2/auth/signup",
                                content_type='application/json', 
                                headers=dict(Authorization='Bearer '+admin['token']),
                                data=Testing.empty_aname)
        self.assertEqual(resp.status_code, 400)
        self.assertIn(b"Username is missing", resp.data)


    def test_add_user_with_empty_contact(self):
        '''testing for sapace '''
        admin = self.adminlogin()
        resp = self.app.post("/api/v2/auth/signup",
                                content_type='application/json', 
                                headers=dict(Authorization='Bearer '+admin['token']),
                                data=Testing.empty_contact)
        self.assertEqual(resp.status_code, 400)
        self.assertIn(b"Contact is missing", resp.data)


    def test_add_user_with_empty_password(self):
        '''testing for sapace '''
        admin = self.adminlogin()
        resp = self.app.post("/api/v2/auth/signup",
                                content_type='application/json', 
                                headers=dict(Authorization='Bearer '+admin['token']),
                                data=Testing.empty_password)
        self.assertEqual(resp.status_code, 400)
        self.assertIn(b"Password is missing", resp.data)


    def test_add_user_with_bad_name(self):
        '''testing for bad name '''
        admin = self.adminlogin()
        resp = self.app.post("/api/v2/auth/signup",
                                content_type='application/json', 
                                headers=dict(Authorization='Bearer '+admin['token']),
                                data=Testing.wrong_anme)
        self.assertEqual(resp.status_code, 400)
        self.assertIn(b"Username should be one or two words of 5 or more characters each", resp.data)


    def test_add_user_with_bad_cntact(self):
        '''testing for bad contact '''
        admin = self.adminlogin()
        resp = self.app.post("/api/v2/auth/signup",
                                content_type='application/json', 
                                headers=dict(Authorization='Bearer '+admin['token']),
                                data=Testing.wrong_contact)
        self.assertEqual(resp.status_code, 400)
        self.assertIn(b"Contact should be in this format '+256-755-598090'", resp.data)


    # def test_add_user_with_bad_password(self):
    #     '''testing for bad password '''
    #     admin = self.adminlogin()
    #     resp = self.app.post("/api/v2/auth/signup",
    #                             content_type='application/json', 
    #                             headers=dict(Authorization='Bearer '+admin['token']),
    #                             data=Testing.wrong_password)
    #     self.assertEqual(resp.status_code, 400)
    #     self.assertIn(b"Password must have 7 characters with atleast a lowercase, uppercase letter and a number", resp.data)


    def test_adding_existing_name(self):
        '''testing for duplicate data '''
        admin= self.adminlogin()
        resp1 = self.app.post("/api/v2/auth/signup",
                                content_type='application/json', 
                                headers=dict(Authorization='Bearer '+admin['token']),
                                data=Testing.registering_attendant)
        resp = self.app.post("/api/v2/auth/signup",
                             content_type='application/json', 
                             headers=dict(Authorization='Bearer '+admin['token']),
                             data=Testing.dupliate_name)                      
        self.assertEqual(resp.status_code, 400)
        self.assertIn(b"Attendant name already exists, use another", resp.data)


    def test_adding_existing_contact(self):
        '''testing for duplicate data '''
        admin= self.adminlogin()
        resp1 = self.app.post("/api/v2/auth/signup",
                                content_type='application/json', 
                                headers=dict(Authorization='Bearer '+admin['token']),
                                data=Testing.registering_attendant)
        resp = self.app.post("/api/v2/auth/signup",
                             content_type='application/json', 
                             headers=dict(Authorization='Bearer '+admin['token']),
                             data=Testing.dupliate_contact)                      
        self.assertEqual(resp.status_code, 400)
        self.assertIn(b"Contact already exists, use another", resp.data)


    def test_fetching_attendants(self):
        '''testing for getting all attendants '''
        admin= self.adminlogin()
        resp1 = self.app.post("/api/v2/auth/signup",
                                content_type='application/json', 
                                headers=dict(Authorization='Bearer '+admin['token']),
                                data=Testing.registering_attendant)
        resp = self.app.get("/api/v2/auth/signup",
                             content_type='application/json', 
                             headers=dict(Authorization='Bearer '+admin['token']),)                      
        self.assertEqual(resp.status_code, 200)
        self.assertIn(b"All attendants have been viewed", resp.data)


    # def test_for_fetching_empty_attendants_table(self):
    #     '''test for fetching all attendants that dont exist'''
    #     admin = self.adminlogin()
    #     resp = self.app.get("/api/v2/auth/signup",
    #                          content_type='application/json', 
    #                          headers=dict(Authorization='Bearer '+admin['token']),)              
    #     self.assertEqual(resp.status_code, 404)
    #     self.assertIn(b"No attendants added yet", resp.data)


    def test_updating_attenadant(self):
        '''test for updating '''
        admin = self.adminlogin()
        resp = self.app.post("/api/v2/auth/signup",
                             content_type='application/json', 
                             headers=dict(Authorization='Bearer '+admin['token']),
                             data=Testing.registering_attendant)
        resp2 = self.app.put("/api/v2/auth/signup/1",
                                 content_type='application/json', 
                                 headers=dict(Authorization='Bearer '+admin['token']),
                                 data=Testing.update_user)
        self.assertEqual(resp2.status_code, 200)
        self.assertIn(b"Attendant is now admin", resp2.data)


    def test_updating_attenadant_with_wrong_role(self):
        '''test for updating '''
        admin = self.adminlogin()
        resp = self.app.post("/api/v2/auth/signup",
                             content_type='application/json', 
                             headers=dict(Authorization='Bearer '+admin['token']),
                             data=Testing.registering_attendant)
        resp2 = self.app.put("/api/v2/auth/signup/1",
                                 content_type='application/json', 
                                 headers=dict(Authorization='Bearer '+admin['token']),
                                 data=Testing.update_wrong_role)
        self.assertEqual(resp2.status_code, 400)
        self.assertIn(b"Role should either be admin or attendant", resp2.data)


    # def test_updating_attenadant_with_wrong_field(self):
    #     '''test for updating '''
    #     admin = self.adminlogin()
    #     resp = self.app.post("/api/v2/auth/signup",
    #                          content_type='application/json', 
    #                          headers=dict(Authorization='Bearer '+admin['token']),
    #                          data=Testing.registering_attendant)
    #     resp2 = self.app.put("/api/v2/auth/signup/1",
    #                              content_type='application/json', 
    #                              headers=dict(Authorization='Bearer '+admin['token']),
    #                              data=Testing.update_role_wrong_fields)
    #     self.assertEqual(resp2.status_code, 400)
    #     self.assertIn(b"Some fields are missing, please check", resp2.data)


    def test_login_successful(self):
        ''' test for successful login '''
        self.register_attendant()
        resp = self.app.post("/api/v2/auth/login",
                                 content_type='application/json',
                                 data=Testing.login_info)
        self.assertEqual(resp.status_code, 200)
        self.assertIn(b"You have been logged in", resp.data)


    # def test_with_invalid_fields_login(self):
    #     ''' test for invalid fields login '''
    #     self.register_attendant()
    #     resp = self.app.post("/api/v2/auth/login",
    #                             content_type='application/json',
    #                             data=Testing.login_info_invalid_fields)
    #     self.assertEqual(resp.status_code, 400)
    #     self.assertIn(b"Some fields are missing, please check", resp.data)


    def test_login_unsuccessful(self):
        ''' test for wrong name '''
        self.register_attendant()
        resp = self.app.post("/api/v2/auth/login",
                                 content_type='application/json',
                                 data=Testing.login_invalid_name)
        self.assertEqual(resp.status_code, 401)
        self.assertIn(b"Invalid username or password", resp.data)            

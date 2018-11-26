from tests.test_base import Testing
from run import app
from flask import jsonify, json


class TestAttendant(Testing):

    '''testing the login route
        so that it is working in
        accordance to the bneeded way'''

    def test_login_wrong_fields(self):
        ''' test login for wrong fields '''
        resp = self.app.post("/api/v2/auth/login",
                             content_type='application/json',
                             data=Testing.wrong_lfields)
        self.assertEqual(resp.status_code, 400)
        self.assertIn(b"Some fields are missing, please check", resp.data) 

    def test_login_unsuccessful(self):
        ''' test login for wrong credentials '''
        resp = self.app.post("/api/v2/auth/login",
                             content_type='application/json',
                             data=Testing.login_invalid_name)
        self.assertEqual(resp.status_code, 401)
        self.assertIn(b"Invalid username or password", resp.data) 

    def test_login_successful(self):
        ''' test for successful login '''
        self.register_attendant()
        resp = self.app.post("/api/v2/auth/login",
                             content_type='application/json',
                             data=Testing.login_info)
        self.assertEqual(resp.status_code, 200)
        self.assertIn(b"You have been logged in", resp.data)



    '''testing the add attendant route
        so that an attendant can be
        added the right way'''

    def test_for_invalid_url(self):
        '''testing for invalid url '''
        admin = self.adminlogin()
        resp = self.app.post("/api/v2/auth/sign",
                             content_type='application/json', 
                             headers=dict(Authorization='Bearer '+admin['token']),
                             data=Testing.registering_attendant )
        self.assertEqual(resp.status_code, 405)
        self.assertIn(b"Please put a valid URL", resp.data)

    def test_for_add_with_method_not_allowed(self):
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

    # def test_add_user_with_user_logged_in(self):
    #     '''testing for user authentication '''
    #     attendant = self.attendantlogin()
    #     resp = self.app.post("/api/v2/auth/signup",
    #                          content_type='application/json', 
    #                          headers=dict(Authorization='Bearer '+attendant['token']),
    #                          data=Testing.registering_attendant)
    #     self.assertEqual(resp.status_code, 401)
    #     self.assertIn(b"Unauthorized to operate this feature", resp.data)

    def test_add_user_with_empty_name(self):
        '''testing for space '''
        admin = self.adminlogin()
        resp = self.app.post("/api/v2/auth/signup",
                             content_type='application/json', 
                             headers=dict(Authorization='Bearer '+admin['token']),
                             data=Testing.empty_aname)
        self.assertEqual(resp.status_code, 400)
        self.assertIn(b"Some values are missing, recheck", resp.data)

    def test_add_user_with_empty_contact(self):
        '''testing for space '''
        admin = self.adminlogin()
        resp = self.app.post("/api/v2/auth/signup",
                             content_type='application/json', 
                             headers=dict(Authorization='Bearer '+admin['token']),
                             data=Testing.empty_contact)
        self.assertEqual(resp.status_code, 400)
        self.assertIn(b"Some values are missing, recheck", resp.data)

    def test_add_user_with_empty_password(self):
        '''testing for sapace '''
        admin = self.adminlogin()
        resp = self.app.post("/api/v2/auth/signup",
                             content_type='application/json', 
                             headers=dict(Authorization='Bearer '+admin['token']),
                             data=Testing.empty_password)
        self.assertEqual(resp.status_code, 400)
        self.assertIn(b"Some values are missing, recheck", resp.data)

    def test_add_user_with_bad_name(self):
        '''testing for bad name '''
        admin = self.adminlogin()
        resp = self.app.post("/api/v2/auth/signup",
                             content_type='application/json', 
                             headers=dict(Authorization='Bearer '+admin['token']),
                             data=Testing.wrong_anme)
        self.assertEqual(resp.status_code, 400)
        self.assertIn(b"Username should be one or two words of 5 or more characters each", resp.data)

    def test_add_user_with_bad_contact(self):
        '''testing for bad contact '''
        admin = self.adminlogin()
        resp = self.app.post("/api/v2/auth/signup",
                             content_type='application/json', 
                             headers=dict(Authorization='Bearer '+admin['token']),
                             data=Testing.wrong_contact)
        self.assertEqual(resp.status_code, 400)
        self.assertIn(b"Contact should be in this format '+256-755-598090'", resp.data)

    def test_add_user_with_bad_password(self):
        '''testing for bad password '''
        admin = self.adminlogin()
        resp = self.app.post("/api/v2/auth/signup",
                             content_type='application/json', 
                             headers=dict(Authorization='Bearer '+admin['token']),
                             data=Testing.wrong_password)
        self.assertEqual(resp.status_code, 400)
        self.assertIn(b"Password must have 7 characters with atleast a lowercase, uppercase letter and a number", resp.data)

    def test_adding_existing_name(self):
        '''testing for duplicate data '''
        admin= self.adminlogin()
        resp = self.app.post("/api/v2/auth/signup",
                             content_type='application/json', 
                             headers=dict(Authorization='Bearer '+admin['token']),
                             data=Testing.dupliate_name)                      
        self.assertEqual(resp.status_code, 400)
        self.assertIn(b"Attendant name already exists, use another", resp.data)

    def test_adding_existing_contact(self):
        '''testing for duplicate data '''
        admin= self.adminlogin()
        resp = self.app.post("/api/v2/auth/signup",
                             content_type='application/json', 
                             headers=dict(Authorization='Bearer '+admin['token']),
                             data=Testing.dupliate_contact)                      
        self.assertEqual(resp.status_code, 400)
        self.assertIn(b"Contact already exists, use another", resp.data)

    def test_user_reg_successful(self):
        '''testing for successful '''
        admin = self.adminlogin()
        resp = self.app.post("/api/v2/auth/signup",
                             content_type='application/json', 
                             headers=dict(Authorization='Bearer '+admin['token']),
                             data=Testing.registering_attendant )
        self.assertEqual(resp.status_code, 201)
        self.assertIn(b"You have successfully added Douglas", resp.data)



    '''tests for the fetching 
        all route so that all
        attendants can be accessed'''

    # def test_fetch_attendant_with_user_logged_in(self):
    #     '''testing for user authentication '''
    #     attendant = self.attendantlogin()
    #     resp = self.app.get("/api/v2/auth/signup",
    #                          content_type='application/json', 
    #                          headers=dict(Authorization='Bearer '+attendant['token']),)
    #     self.assertEqual(resp.status_code, 401)
    #     self.assertIn(b"Unauthorized to operate this feature", resp.data)

    # def test_for_fetching_empty_attendants_table(self):
    #     '''test for fetching all attendants that dont exist'''
    #     admin = self.adminlogin()
    #     resp = self.app.get("/api/v2/auth/signup",
    #                          content_type='application/json', 
    #                          headers=dict(Authorization='Bearer '+admin['token']),)              
    #     self.assertEqual(resp.status_code, 404)
    #     self.assertIn(b"No attendants added yet", resp.data)

    def test_fetching_attendants(self):
        '''testing for getting all attendants '''
        admin= self.adminlogin()
        resp = self.app.get("/api/v2/auth/signup",
                             content_type='application/json', 
                             headers=dict(Authorization='Bearer '+admin['token']),)                      
        self.assertEqual(resp.status_code, 200)
        self.assertIn(b"All attendants have been viewed", resp.data)

    

    '''tests for the fetching 
        all route so that all
        attendants can be accessed'''

    def test_fetch_attendant_with_wrong_input(self):
        '''testing for user authentication '''
        admin = self.adminlogin()
        resp = self.app.get("/api/v2/auth/signup/ai",
                             content_type='application/json', 
                             headers=dict(Authorization='Bearer '+admin['token']),)
        self.assertEqual(resp.status_code, 400)
        self.assertIn(b"Id input should be an integer", resp.data)

    # def test_fetch_attendant_with_user_logged_in(self):
    #     '''testing for user authentication '''
    #     attendant = self.attendantlogin()
    #     resp = self.app.get("/api/v2/auth/signup/1",
    #                          content_type='application/json', 
    #                          headers=dict(Authorization='Bearer '+attendant['token']),)
    #     self.assertEqual(resp.status_code, 401)
    #     self.assertIn(b"Unauthorized to operate this feature", resp.data)

    def test_for_fetching_no_attendant(self):
        '''test for fetching all attendants that dont exist'''
        admin = self.adminlogin()
        resp = self.app.get("/api/v2/auth/signup/100",
                             content_type='application/json', 
                             headers=dict(Authorization='Bearer '+admin['token']),)              
        self.assertEqual(resp.status_code, 404)
        self.assertIn(b"No attendant with that id", resp.data)

    def test_fetching_attendant(self):
        '''test for getting one attendant '''
        admin= self.adminlogin()
        resp = self.app.get("/api/v2/auth/signup/1",
                             content_type='application/json', 
                             headers=dict(Authorization='Bearer '+admin['token']),)                      
        self.assertEqual(resp.status_code, 200)
        self.assertIn(b"Attendant has been viewed", resp.data)



    '''the tests for updating
        route so that user can
        edit another user'''

    def test_update_attendant_with_wrong_fields(self):
        '''test for wrong fields '''
        admin = self.adminlogin()
        resp = self.app.put("/api/v2/auth/signup/1",
                             content_type='application/json', 
                             headers=dict(Authorization='Bearer '+admin['token']),
                             data=Testing.wrong_ufields)
        self.assertEqual(resp.status_code, 400)
        self.assertIn(b"Some fields are missing, please check", resp.data)

    def test_update_attendant_with_wrong_id(self):
        '''test for wrong id '''
        admin = self.adminlogin()
        resp = self.app.put("/api/v2/auth/signup/ai",
                             content_type='application/json', 
                             headers=dict(Authorization='Bearer '+admin['token']),
                             data=Testing.update_user)
        self.assertEqual(resp.status_code, 400)
        self.assertIn(b"Id input should be an integer", resp.data)

    # def test_update_attendant_with_user_logged_in(self):
    #     '''testing for user authentication '''
    #     attendant = self.attendantlogin()
    #     resp = self.app.put("/api/v2/auth/signup/1",
    #                          content_type='application/json', 
    #                          headers=dict(Authorization='Bearer '+attendant['token']),
    #                          data=Testing.update_user)
    #     self.assertEqual(resp.status_code, 401)
    #     self.assertIn(b"Unauthorized to operate this feature", resp.data)

    def test_updating_attenadant_with_wrong_role(self):
        '''test for updating with wrong role '''
        admin = self.adminlogin()
        resp2 = self.app.put("/api/v2/auth/signup/1",
                             content_type='application/json', 
                             headers=dict(Authorization='Bearer '+admin['token']),
                             data=Testing.update_wrong_role)
        self.assertEqual(resp2.status_code, 400)
        self.assertIn(b"Role should either be admin or attendant", resp2.data)

    def test_updating_attenadant_with_wrong_id(self):
        '''test for updating with wrong or no id'''
        admin = self.adminlogin()
        resp2 = self.app.put("/api/v2/auth/signup/100",
                             content_type='application/json', 
                             headers=dict(Authorization='Bearer '+admin['token']),
                             data=Testing.update_user)
        self.assertEqual(resp2.status_code, 404)
        self.assertIn(b"No attendant with that id", resp2.data)

    def test_updating_attenadant(self):
        '''test for updating '''
        admin = self.adminlogin()
        resp2 = self.app.put("/api/v2/auth/signup/1",
                             content_type='application/json', 
                             headers=dict(Authorization='Bearer '+admin['token']),
                             data=Testing.update_user)
        self.assertEqual(resp2.status_code, 200)
        self.assertIn(b"Attendant role has been updated", resp2.data)


    
    '''tests for deleting
        route so that user can
        delete another user'''

    def test_delete_attendant_with_wrong_id(self):
        '''test for wrong id '''
        admin = self.adminlogin()
        resp = self.app.delete("/api/v2/auth/signup/ai",
                                content_type='application/json', 
                                headers=dict(Authorization='Bearer '+admin['token']),)
        self.assertEqual(resp.status_code, 400)
        self.assertIn(b"Id input should be an integer", resp.data)

    # def test_delete_attendant_with_user_logged_in(self):
    #     '''testing for user authentication '''
    #     admin = self.adminlogin()
    #     resp = self.app.delete("/api/v2/auth/signup/1",
    #                             content_type='application/json', 
    #                             headers=dict(Authorization='Bearer '+admin['token']),)
    #     self.assertEqual(resp.status_code, 401)
    #     self.assertIn(b"Unauthorized to operate this feature", resp.data)

    def test_delete_attenadant_with_no_id(self):
        '''test for updating '''
        admin = self.adminlogin()
        resp2 = self.app.delete("/api/v2/auth/signup/100",
                             content_type='application/json', 
                             headers=dict(Authorization='Bearer '+admin['token']),)
        self.assertEqual(resp2.status_code, 404)
        self.assertIn(b"No attendant with that id", resp2.data)

    def test_successful_deletion(self):
        ''' test for delete '''
        admin = self.adminlogin()
        resp = self.app.delete("/api/v2/auth/signup/1",
                                content_type='application/json',
                                headers=dict(Authorization='Bearer '+admin['token']),)
        self.assertEqual(resp.status_code, 200)
        self.assertIn(b"Successfully deleted attendant", resp.data)

from django.test import Client, TestCase
from api.tests.utils import create_test_user, login, make_request, create_test_branch


class UserApiTest(TestCase):
    """Test for User API"""

    def setUp(self):
        self.client = Client()
        self.endpoint = '/api'
        self.user = create_test_user()
        self.header = {
            'HTTP_TOKEN': login(self.client, 'tester', 'tester123')
        }
        self.branch = create_test_branch()

    def retrieve_user(self, user_id):
        query = 'query {user(id: "%s") {username}}' % user_id

        return make_request(self.client, query, self.endpoint, self.header)

    def create_user(self):
        query = '''mutation{
            createUser(input:{
              userData:{
                username:"tester2",
                email:"test2@test.com",
                password:"tester123",
                firstName:"test2",
                lastName:"test2"
              },
              customerServiceData:{
                email: "test@test.com",
                phone: "1234567",
                branchId: %s
              }
            }){
              user{
                id,
                username
              }
            }
          }''' % self.branch.id
        return make_request(self.client, query, '/api', self.header, 'POST')

    def test_creation_of_user(self):
        response = self.create_user()
        expected = {
            'id': response['data']['createUser']['user']['id'],
            'username': 'tester2',
        }
        self.assertEqual(expected, response['data']['createUser']['user'])

    def test_deleting_of_user(self):
        response = self.create_user()
        user = response['data']['createUser']['user']
        query = '''mutation{
          deleteUser(input:{
            id:"%s"
          }){
            user{
              username
            }
          }
        }''' % user.get('id')

        response = make_request(self.client, query, '/api', self.header, 'POST')
        expected = {
            'username': user.get('username')
        }
        self.assertEqual(expected, response['data']['deleteUser']['user'])

        query = '''
            query{
                 user(id:"%s"){
                  username
                }
            }
        ''' % user.get('id')
        response = make_request(self.client, query, '/api', self.header)
        self.assertEqual(None, response['data']['user'])

    def retrieve_user(self):
        query = '''
            query{
                 users{
                  edges{
                    node{
                      username
                    }
                  }
                }
            }
        '''
        return make_request(self.client, query, self.endpoint, self.header)

    def test_retrieve_user(self):
        response = self.retrieve_user()
        expected = {
            'username': 'tester'
        }
        self.assertEqual(len(response['data']['users']['edges']), 1)
        self.assertEqual(expected, response['data']['users']['edges'][0]['node'])

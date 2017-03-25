from base64 import b64encode
from django.contrib.auth.models import User
from accounts.models import Bank, Branch


def make_request(client, query, endpoint='/api', headers={}, method='GET'):
    if method == 'GET':
        return client.get(endpoint, data={'query': query}, **headers).json()

    if method == 'POST':
        return client.post(endpoint, data={'query': query}, **headers).json()


def create_test_user(username="tester", email="test@test.com"):
    user = User(username=username, email=email)
    user.set_password("tester123")
    user.save()
    return user


def create_test_bank():
    return Bank.objects.create(
        name="testbank",
        logo="",
        banner="",
        address="abc",
        city="abc",
        state="abc",
        country="abc"
    )


def create_test_branch():
    return Branch.objects.create(
        name="testbank",
        sort_code=123456,
        email="test@tets.com",
        phone="123456",
        address="abc",
        city="abc",
        state="abc",
        country="abc"
    )


def login(client, user, password):
        credentials = '{}:{}'.format(user, password)
        b64_encoded_credentials = b64encode(credentials.encode('utf-8'))
        return client.post(
            '/api/login',
            **{'HTTP_AUTHORIZATION': 'Basic %s' % b64_encoded_credentials.decode('utf-8')}
        ).json()['token']

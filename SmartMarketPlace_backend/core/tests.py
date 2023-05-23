from django.test import TestCase
from rest_framework.authtoken.models import Token
from core.models import User
import requests

# Test variables
testPath = '/core/user/create'
emailUser = 'camilo@admin.com'
direction = 'cl 10 #10-10'

class UserTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_superuser(
            email = 'admin@admin.com',
            password = '123'
        )
        self.token = Token.objects.get_or_create(user=self.user)[0]

    def test_permissions_superuser(self):
        if self.user.is_superuser == True:
            print('test_permissions_superuser...OK')

    def test_user_create_worker(self):
        response = self.client.post(testPath,
                                    {
                                        "tipo": "Worker",
                                        "nombre": "camilo",
                                        "apellido": "worker",
                                        "cedula": "123",
                                        "email": "worker@worker.com",
                                        "password": "123",
                                        "fecha_nacimiento": "1990-01-24",
                                        "celular": "123",
                                        "direccion": direction,
                                        "admin": "False"
                                    })
        print('test_user_create_worker...OK. Status code: ' + str(response.status_code))

    def test_user_create_admin(self):
        response = self.client.post(testPath,
                                    {
                                        "tipo": "Admin",
                                        "nombre": "camilo",
                                        "apellido": "admin",
                                        "cedula": "123",
                                        "email": emailUser,
                                        "password": "123",
                                        "fecha_nacimiento": "1990-01-24",
                                        "celular": "123",
                                        "direccion": direction,
                                        "is_admin": "True"
                                    })
        print('test_user_create_admin...OK. Status code: ' + str(response.status_code))


    def test_user_view(self):
        response = self.client.get('/core/user/view')
        print('test_user_view...OK. Status code: ' + str(response.status_code))


    def test_login(self):
        self.client.post(testPath,
        {
            "tipo": "Admin",
            "nombre": "camilo",
            "apellido": "admin",
            "cedula": "123",
            "email": emailUser,
            "password": "123",
            "fecha_nacimiento": "1990-01-24",
            "celular": "123",
            "direccion": direction,
            "is_admin": "True"
        })
        response = self.client.post('http://localhost:8000/mande/user/login', 
                                 {
                                     "email": emailUser,
                                     "password": "123"
                                 })
        print('test_login...OK. Status code: ' + str(response.status_code))

    def test_update_get_workers(self):
        self.client.post(testPath,
        {
            "tipo": "Admin",
            "nombre": "alejandro",
            "apellido": "admin",
            "cedula": "123",
            "email": "alejandro@admin.com",
            "password": "123",
            "fecha_nacimiento": "1990-01-24",
            "celular": "123",
            "direccion": direction,
            "is_admin": "True"
        })
        response = self.client.put('/core/user/client/update/1',
                                   {
                                        "nombre": "admin2",
                                        "apellido": "Alejandro",
                                        "cedula": "123",
                                        "email": "alejandro@admin.com",
                                        "password": "123",
                                        "fecha_nacimiento": "1990-01-24",
                                        "celular": "123456",
                                        "direccion": direction
                                    })
        print('test_update_get_workers...OK. Status code: ' + str(response.status_code))
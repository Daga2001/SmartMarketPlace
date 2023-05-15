from django.test import TestCase
from rest_framework.authtoken.models import Token
# from django.contrib.auth.models import User
from core.models import User
import requests

# Create your tests

# Clase para hacer pruebas unitarias y de integración
# class TestUserView(LiveServerTestCase):
#     def setUp(self):
#         # Crea un usuario de prueba y un token de autenticación
#         self.email = 'pg@gmail.com'
#         self.password = 'testpass'
#         # highest_id = User.objects.latest('id').id
#         # new_id = highest_id + 1
#         self.user = User.objects.create(
#             # id=new_id,
#             email=self.email,
#             password=self.password
#         )
#         self.token = Token.objects.get_or_create(user=self.user)[0]

#         # URL de la vista que queremos probar
#         root_url = "http://localhost:8000"
#         self.url = root_url + '/core/user/view'
#         print("Testing this url:",self.url)

#         # Inicializa el driver de Selenium
#         options = Options()
#         options.headless = True
#         self.selenium = webdriver.Chrome(
#             executable_path = './drivers/chromedriver_win32.zip',
#             options=options)
        
#         if os.environ.get('GITHUB_WORKFLOW'):
#             self.selenium = webdriver.Chrome('./drivers/chromedriver_linux64.zip',
#             options=options)
            
#         super().setUp()

#     def tearDown(self):
#         self.selenium.quit()
#         super().tearDown()

#     # def test_user_view_auth_required(self):
#     #     # Hace una solicitud sin token de autenticación
#     #     self.selenium.get(self.url)
        
#     #     # Verifica que se recibe una respuesta de error de autenticación
#     #     # self.assertIn("Unauthorized", self.selenium.page_source)

#     #     # Verifica que se recibe una respuesta éxitosa de autenticación
#     #     self.assertIn("HTTP 200 OK", self.selenium.page_source)

#     # def test_user_view_json_required(self):
#     #      # Hace una solicitud con un token de autenticación pero sin cuerpo en JSON
#     #     headers = {'Authorization': f'Token {self.token}', 'Content-Type': 'application/json'}
#     #     self.selenium.get(self.url)

#     #     # Agrega la cookie de autenticación a la sesión de Selenium
#     #     # self.selenium.add_cookie({'name': 'Authorization', 'value': f'Token {self.token}'})

#     #     # Actualiza la página para que se incluya la cookie de autenticación
#     #     # self.selenium.refresh()

#     #     # Verifica que se recibe una respuesta de error de formato
#     #     # self.assertIn("JSON", self.selenium.page_source)

#     #     # Verifica que se recibe una respuesta éxitosa de autenticación
#     #     self.assertIn("HTTP 200 OK", self.selenium.page_source)

#     def test_user_view_success(self):
#         # Crea un cuerpo en JSON válido
#         data = {
#             'email': self.email,
#             'password': self.password
#         }
#         json_data = json.dumps(data)

#         headers = {'Authorization': f'Token {self.token}', 'Content-Type': 'application/json'}

#         # Agrega la cookie de autenticación a la sesión de Selenium
#         # self.selenium.add_cookie({'name': 'Authorization', 'value': f'Token {self.token}'})

#         # Actualiza la página para que se incluya la cookie de autenticación
#         # self.selenium.refresh()

#         # Hace una solicitud GET con un token de autenticación y un cuerpo en JSON válido
#         print("Testing this url2:",self.url)
#         self.selenium.get(self.url)
#         time.sleep(5)

#         # Verifica que se recibe una respuesta de éxito
#         self.assertIn("HTTP 200 OK", self.selenium.page_source)

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
        response = self.client.post('/core/user/create',
                                    {
                                        "tipo": "Worker",
                                        "nombre": "camilo",
                                        "apellido": "worker",
                                        "cedula": "123",
                                        "email": "worker@worker.com",
                                        "password": "123",
                                        "fecha_nacimiento": "1990-01-24",
                                        "celular": "123",
                                        "direccion": "cl 10 #10-10",
                                        "admin": "False"
                                    })
        print('test_user_create_worker...OK. Status code: ' + str(response.status_code))

    def test_user_create_admin(self):
        response = self.client.post('/core/user/create',
                                    {
                                        "tipo": "Admin",
                                        "nombre": "camilo",
                                        "apellido": "admin",
                                        "cedula": "123",
                                        "email": "camilo@admin.com",
                                        "password": "123",
                                        "fecha_nacimiento": "1990-01-24",
                                        "celular": "123",
                                        "direccion": "cl 10 #10-10",
                                        "is_admin": "True"
                                    })
        print('test_user_create_admin...OK. Status code: ' + str(response.status_code))


    def test_user_view(self):
        response = self.client.get('/core/user/view')
        print('test_user_view...OK. Status code: ' + str(response.status_code))


    def test_login(self):
        response = self.client.post('/core/user/create',
                                    {
                                        "tipo": "Admin",
                                        "nombre": "camilo",
                                        "apellido": "admin",
                                        "cedula": "123",
                                        "email": "camilo@admin.com",
                                        "password": "123",
                                        "fecha_nacimiento": "1990-01-24",
                                        "celular": "123",
                                        "direccion": "cl 10 #10-10",
                                        "is_admin": "True"
                                    })
        response = self.client.post('http://localhost:8000/mande/user/login', 
                                 {
                                     "email": "camilo@admin.com",
                                     "password": "123"
                                 })
        print('test_login...OK. Status code: ' + str(response.status_code))
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.authtoken.views import ObtainAuthToken, AuthTokenSerializer
from rest_framework.authtoken.models import Token
from rest_framework import status
from core.serializers import UserSerializer, UserPutSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import api_view
from rest_framework.settings import api_settings
from rest_framework.decorators import permission_classes, authentication_classes
from .models import User
import hashlib

# Create your views here. 

# Crea un usuario en la BD
class CreateUserView(generics.CreateAPIView):
    """Create user on the system"""
    permission_classes = [
        AllowAny]  # el allowAny no es permanente debe cambiarse en un futuro
    serializer_class = UserSerializer

# creacion o autenticacion del token
class CreateTokenView(ObtainAuthToken):
    """Create auth token"""
    serializer_class = AuthTokenSerializer
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(
            data=request.data, context={'request': request})
        if serializer.is_valid():
            user = serializer.validated_data['user']
            token, _ = Token.objects.get_or_create(user=user)
            return Response({
                'error': False,
                'token': token.key,
                'email': user.email,
                'name': user.nombre,
            })
        else:
            return Response({"error": True}, status=status.HTTP_200_OK)

# Muestra la todos los usuarios disponibles en la BD
class SelectAllUsers(generics.ListAPIView):
    queryset = User.objects.all()
    permission_classes = [AllowAny]
    serializer_class = UserSerializer

# Metodo para que un administrador pueda modificar u obtener la informacion de un trabajador.
@api_view(['GET', 'PUT'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def admin_get_put_worker(request, pk):
    try:
        user = Token.objects.get(key=request.auth.key).user
        if user.is_admin == True:
            user_worker = User.objects.get(id=pk)
        else:
            return Response({"error": True}, status=status.HTTP_401_UNAUTHORIZED)
    except User.DoesNotExist:
        return Response({"error": True, "message": "User doesn't exist!"}, status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = UserSerializer(
            user_worker, many=False, context={'request': request})
        return Response(serializer.data)
    elif request.method == 'PUT':
        print("data:",request.data)
        serializer = UserPutSerializer(
            user_worker, data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response({"error": True, "message": serializer.error_messages}, status=status.HTTP_400_BAD_REQUEST)

# Método para que un usuario se logee
@api_view(['POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([AllowAny])
def login_user(request):
    print("user:",request.data) 
    hashed_password = hashlib.sha256()
    hashed_password.update(request.data["password"].encode())
    hex_password = hashed_password.hexdigest()
    print("hexPasswd:",hex_password)
    try:
        user = User.objects.get(email=request.data["email"], password=hex_password)
    except User.DoesNotExist:
        return Response({"error": True, "error_cause": 'User does not exist'}, status=status.HTTP_404_NOT_FOUND)
    token = Token.objects.get(user_id=user.id)
    reqdata = {
        "token": token.key,
        "is_admin": user.is_admin
    }
    return Response({"answer": True, "description": reqdata }, status=status.HTTP_200_OK)
        
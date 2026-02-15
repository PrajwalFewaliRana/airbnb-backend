from .serializers import UserDetailSerializer
from rest_framework.response import Response
from django.http import JsonResponse
from rest_framework.decorators import api_view,authentication_classes,permission_classes
from property.serializers import ReservationsListSerializer
from rest_framework.permissions import IsAuthenticated



from .models import User

@api_view(['GET'])
@authentication_classes([])
@permission_classes([])

def landlord_detail(request,pk):
    user = User.objects.get(pk=pk)
    serializer = UserDetailSerializer(user,many=False)
    
    return JsonResponse(serializer.data,safe=False)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def reservations_list(request):
    reservations = request.user.reservations.all()
    serializer= ReservationsListSerializer(reservations,many=True)
    return JsonResponse(serializer.data,safe=False)

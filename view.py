from django.shortcuts import render

# Create your views here.
from rest_framework.response import Response
from rest_framework import status
from .serializers import PlanSerializer
from .models import Plan

class PlanViews(APIView):
    def post(self, request):
        serializer = 
PlanSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({"status": "error", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
        
class PansViewSet(viewsets.ModelViewSet):
    queryset = Plans.objects.all().order_by('plan_name')
    serializer_class = PlanSerializer

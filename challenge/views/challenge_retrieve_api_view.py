from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework import generics, filters

from django_filters.rest_framework import DjangoFilterBackend

from challenge.serializers import ChallengeSerializer
from challenge.models import Challenge, ChallengeCategory

class ChallengeRetrieveAPIView(generics.ListAPIView):
    serializer_class = ChallengeSerializer
    queryset = Challenge.objects.all()
    filter_backends = [filters.SearchFilter]
    search_fields = ['start_at', 'end_at']

    def get(self,request,*args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())

        category = request.query_params.get("category", None)
        category_id = get_object_or_404(ChallengeCategory, title=category)

        queryset = queryset.filter(category=category_id)

        serializer = self.get_serializer(queryset, many=True)

        return Response(serializer.data)

from rest_framework.generics import ListAPIView, get_object_or_404
from rest_framework.response import Response

from challenge.models import Challenge, ChallengeCategory
from challenge.serializers import ChallengeSerializer


class RelatedListAPIView(ListAPIView):
    serializer_class = ChallengeSerializer
    filterset_fields = []
    search_fields = []
    ordering_fields = []

    def list(self, request, challenge_id, *args, **kwargs):
        """
        연관 챌린지 리스트 API
        : challenge_id의 category와 동일한 challenge 목록 반환
        """
        category_ids = [
            *ChallengeCategory.objects.filter(challenge_id=challenge_id).values_list("category_id", flat=True)
        ]
        challenge_ids = [
            *ChallengeCategory.objects.exclude(challenge_id=challenge_id)
            .filter(category_id__in=category_ids)
            .values_list("challenge_id", flat=True)
        ]
        queryset = Challenge.objects.is_progressing().filter(pk__in=challenge_ids)

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

# 클래스 기반의 Rest CRUD 처리
from bbs.models import Bbs, Events
from bbs.serializers import BbsSerializer, UserSerializer, GroupSerializer, EventsSerializer
from rest_framework import generics, viewsets
from django.contrib.auth.models import User, Group


# generics 에 목록과 생성 API 가 정의되어 있다
class BbsList(generics.ListCreateAPIView):
    queryset = Bbs.objects.using('default').all()
    serializer_class = BbsSerializer


# generics 에 상세, 수정, 삭제 API 가 정의되어 있다
class BbsDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Bbs.objects.using('default').all()
    serializer_class = BbsSerializer


# 사용자 목록을 화면에 뿌려주는 ViewSet
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.using('default').all()
    serializer_class = UserSerializer


# 그룹목록을 화면에 뿌려주는 ViewSet
class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.using('default').all()
    serializer_class = GroupSerializer


class EventsList(generics.ListAPIView):
    queryset = Events.objects.using('sungbak').all()
    serializer_class = EventsSerializer


class EventsDetail(generics.RetrieveAPIView):
    queryset = Events.objects.using('sungbak').all()
    serializer_class = EventsSerializer


"""
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from bbs.models import Bbs
from bbs.serializers import BbsSerializer


# 요청 url 인 bbs/ 에 대해서 urls.py 에 정의된 view.bbs_list 가 호출된다.
@api_view(['GET', 'POST'])
def bbs_list(request, format=None):
    if request.method == 'GET':
        bbs = Bbs.objects.all()  # SELECT * FROM Bbs
        serializer = BbsSerializer(bbs, many=True)  # many 값이 True 이면 다수의 데이터 instance 를 직렬화할수 있다
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = BbsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# 요청 url 인 bbs/번호 에 대해서 urls.py 에 정의된 view.bbs_detail 이 호출된다
@api_view(['GET', 'PUT', 'DELETE'])
def bbs_detail(request, pk, format=None):
    try:
        bbs = Bbs.objects.get(pk=pk)
    except Bbs.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = BbsSerializer(bbs)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = BbsSerializer(bbs, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        bbs.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
"""
from django.shortcuts import render
from core.models import MemeModel
from core.serializer import MemeSerializer, CreateMemeSerializer
from django.http import Http404
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
# Create your views here.
@api_view (['GET','PATCH','POST'])
def memeViews(request,id=None):
     if request.method == 'GET':
          if id is not None:
               print(id)
               memes = MemeModel.objects.filter(id = id)
               if memes:
                    serializer = MemeSerializer(memes,many=True)
                    return Response(serializer.data)
               else:
                    return Response({'details':"The id doesn't exist"},status=status.HTTP_404_NOT_FOUND)
          else:
               memes = MemeModel.objects.all().order_by('-id')[:100]
               serializer = MemeSerializer(memes,many=True)
               return Response(serializer.data)
     if request.method == 'PATCH':
          if id is not None:
               print(id)
               try:
                    memes = MemeModel.objects.get(id = id)
               except:
                    print("Entered Except!")
                    return Response({'detail':"The id doesn't exist"},status=status.HTTP_400_BAD_REQUEST)
               if memes:
                    state = 0
                    print("Entere if")
                    if 'url' in request.query_params:
                         print('Url')
                         memes.url = request.query_params['url']
                         memes.save()
                         state = 1
                    if 'caption' in request.query_params:
                         print('Caption')
                         memes.caption = request.query_params['caption']
                         memes.save()
                         state = 1
                    if state == 1:
                         return Response(status=status.HTTP_202_ACCEPTED)
                    else:
                         return Response(status=status.HTTP_204_NO_CONTENT)
               
          else:
               return Response(status= status.HTTP_400_BAD_REQUEST)
     if request.method == 'POST':
          if 'name' in request.query_params and 'url' in request.query_params and 'caption' in request.query_params and request.query_params['url']!='None'and request.query_params['caption']!='None' and request.query_params['name']!='None' :
               exist = MemeModel.objects.filter(name=request.query_params['name'],url=request.query_params['url'],caption=request.query_params['caption'])
               if exist:
                    return Response(status=status.HTTP_409_CONFLICT)
               meme = MemeModel.objects.create(name=request.query_params['name'],url=request.query_params['url'],caption=request.query_params['caption'])
               serializer = CreateMemeSerializer(meme)
               return Response(serializer.data)
          else:
               return Response(status=status.HTTP_400_BAD_REQUEST)




     




from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from .models import Snippet
from .serializers import SnippetSerializer


@csrf_exempt
def snippet_list(request):
    """
    List code snippets (GET) or make new one (POST)
    """
    if request.method == 'GET':
        snippets = Snippet.objects.all()
        serializer = SnippetSerializer( snippets, many=True )
        return JsonResponse( serializer.data, safe=False )

    elif request.method == 'POST':
        data = JSONParser().parse( request )
        serializer = SnippetSerializer( data=data )
        if serializer.is_valid():
            # 201: Resource Created
            serializer.save()
            return JsonResponse( serializer.data, status=201 )

        # 400: Bad Request
        return JsonResponse( serializer.errors, status=400 )


@csrf_exempt
def snippet_detail(request, pk):
    """
    Retrieve, update or delete code snippet
    """
    try:
        snippet = Snippet.objects.get( pk=pk )
    except Snippet.DoesNotExist:
        return HttpResponse( status=404 )

    if request.method == 'GET':
        serializer = SnippetSerializer( snippet )
        return JsonResponse( serializer.data )

    elif request.method == 'PUT':
        data = JSONParser().parse( request )
        serializer = SnippetSerializer( snippet, data=data )
        if serializer.is_valid():
            serializer.save()
            return JsonResponse( serializer.data )

        # 400: Bad Request
        return JsonResponse( serializer.errors, status=400 )

    elif request.method == 'DELETE':
        # 204: No Content
        snippet.delete()
        return HttpResponse( status=204 )

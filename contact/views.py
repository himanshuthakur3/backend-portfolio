from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import ContactSerializer


@api_view(["GET", "POST"])
def contact_api(request):

    if request.method == "GET":
        return Response({"message": "API Working Successfully"})

    serializer = ContactSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response({
            "success": True,
            "message": "Message sent successfully"
        })

    return Response(serializer.errors, status=400)
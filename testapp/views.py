from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer
from rest_framework import status
from .models import Credentials , Assignment, Subject, Notes
from . import functions
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view , permission_classes , authentication_classes , renderer_classes
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
import json

# Create your views here.
@csrf_exempt
@api_view(['POST'])
@authentication_classes((TokenAuthentication,))
@permission_classes((IsAuthenticated,))
def handle_upload_assignment(request,sub_id,assign_name):
    print("handle_upload_assignment called")
    count = Assignment.objects.count()
    assign_id = "a_"+sub_id+"_"+str(count+1)
    
    file1 = request.FILES["file"]
    if file1 is None:
        return HttpResponse(status=status.HTTP_400_BAD_REQUEST)
    file1_path = "/tmp/"+assign_id
    with open(file1_path,"wb+") as destination:
        for chunk in file1.chunks():
            destination.write(chunk)
    
    
    uploaded_file_id = functions.upload_file_to_drive(file1_path,assign_id)
    s = Subject.objects.get(subject_id=sub_id)
    if s is None:
        return HttpResponse(status=status.HTTP_400_BAD_REQUEST)
    a = Assignment(name=assign_name, assignment_id=assign_id, drive_file_id=uploaded_file_id , subject=s)
    a.save()
    return HttpResponse(status=status.HTTP_200_OK)
    
@api_view(['GET'])
@renderer_classes((JSONRenderer,))
def get_assigns(request,sub_id):
    return Response(functions.get_assignments_of_subject(sub_id))
    
@csrf_exempt
@api_view(['POST'])
@authentication_classes((TokenAuthentication,))
@permission_classes((IsAuthenticated,))
def handle_upload_notes(request,sub_id,note_name):
    print("handle_upload_note called")
    count = Notes.objects.count()
    n_id = "n_"+sub_id+"_"+str(count+1)
    
    file1 = request.FILES["file"]
    if file1 is None:
        return HttpResponse(status=status.HTTP_400_BAD_REQUEST)
    file1_path = "/tmp/"+n_id
    with open(file1_path,"wb+") as destination:
        for chunk in file1.chunks():
            destination.write(chunk)
    
    
    uploaded_file_id = functions.upload_file_to_drive(file1_path,n_id)
    s = Subject.objects.get(subject_id=sub_id)
    if s is None:
        return HttpResponse(status=status.HTTP_400_BAD_REQUEST)
    n = Notes(name=note_name,note_id=n_id, drive_file_id=uploaded_file_id , subject=s)
    n.save()
    return HttpResponse(status=status.HTTP_200_OK)

@api_view(['GET'])
@renderer_classes((JSONRenderer,))
def get_subs_of_sem(request,sem_id):
    #return HttpResponse(functions.get_subjects_of_sem(sem_id),content_type="application/json")
    return Response(functions.get_subjects_of_sem(sem_id))

@api_view(['GET'])
@renderer_classes((JSONRenderer,))
def get_notes(request,sub_id):
    return Response(functions.get_notes_of_subject(sub_id))

    
    
    
    
    
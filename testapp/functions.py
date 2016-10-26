from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
from oauth2client.service_account import ServiceAccountCredentials
from httplib2 import Http
from .models import Credentials, Assignment, Subject, Notes
from django.core import serializers
from . import myserializers




def get_authenticated_gauth():
    gauth = GoogleAuth()
    # Get creds from database and save to file
    creds = Credentials.objects.get(pk=1)
    creds_file = open('/tmp/mycreds.txt','w')
    creds_file.write(creds.data)
    creds_file.close()
    gauth.LoadCredentialsFile("/tmp/mycreds.txt")
    #if gauth.credentials is None:
        # Authenticate if they're not there
        #gauth.LocalWebserverAuth()
    if gauth.access_token_expired:
        # Refresh them if expired
        gauth.Refresh()
    else:
        # Initialize the saved creds
        gauth.Authorize()
    # Save the current credentials to a file
    gauth.SaveCredentialsFile("/tmp/mycreds.txt")
    # Save creds from file to database
    creds_file1 = open("/tmp/mycreds.txt","r")
    new_creds = creds_file1.read()
    creds_file1.close()
    creds.data = new_creds
    creds.save()
    return gauth
    
def upload_file_to_drive(filePath,fileName):
    gauth = get_authenticated_gauth()
    drive = GoogleDrive(gauth)
    file1 = drive.CreateFile({"title":fileName, "parents": [{"kind": "drive#fileLink", "id": "0B41Zw_PUW6Q2dUxaZnhtbWpFazg"}]})
    file1.SetContentFile(filePath)
    file1.Upload()
    return file1['id']
    
def get_assignments_of_subject(sub_id):
    query = Assignment.objects.filter(assignment_id__regex=r'^a_'+sub_id)
    #data = serializers.serialize('json',Assignment.objects.filter(assignment_id__regex=r'^a_'+sub_id))
    data = myserializers.AssignmentSerializer(query,many=True)
    return data.data
    
def get_subjects_of_sem(sem_id):
    queryset = Subject.objects.filter(subject_id__regex=r'^'+sem_id)
    #data = serializers.serialize('json',Subject.objects.filter(subject_id__regex=r'^'+sem_id))
    data = myserializers.SubjectSerializer(queryset,many=True)
    return data.data

def get_subjects_lite_of_sem(sem_id):
    queryset = Subject.objects.filter(subject_id__regex=r'^'+sem_id)
    #data = serializers.serialize('json',Subject.objects.filter(subject_id__regex=r'^'+sem_id))
    data = myserializers.SubjectSerializerLite(queryset,many=True)
    return data.data

def get_notes_of_subject(sub_id):
    query = Notes.objects.filter(note_id__regex=r'^n_'+sub_id)
    #data = serializers.serialize('json',Notes.objects.filter(note_id__regex=r'^n_'+sub_id))
    data = myserializers.NotesSerializer(query,many=True)
    return data.data
    
def get_drive_url(file_id):
    return "http://drive.google.com/file/d/"+file_id
    
    
    
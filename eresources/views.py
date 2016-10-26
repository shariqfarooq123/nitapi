from django.shortcuts import render
from testapp import functions

# Create your views here.
def show_subjects(request):
    if request.method == 'POST':
        course_code = request.POST.get('course') 
        course ="Btech" if course_code=="b" else "Mtech"
        branch = request.POST.get('branch')
        sem = request.POST.get('sem')
        sem_id = course_code+"_"+branch+"_"+sem
        
        title=course+"/"+branch+"/" +sem
        
    else:
        sem_id = "b_ECE_5"
        title = "Btech/ECE/5"
    
    sub_list = functions.get_subjects_lite_of_sem(sem_id)
    context = {
        "obj_list":sub_list,
        "title":title,
        
    }
    return render(request,"list.html",context)

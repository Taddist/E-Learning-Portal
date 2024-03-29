from django.shortcuts import render
from django.contrib.auth import authenticate
from django.core.exceptions import PermissionDenied
from students.models import User 
from courses.models import Course
from courses.views import calculate_score
# Create your views here.

def get_all_scores_from_user(user):
	scores=[]
	for course in Course.objects.all():
		course_scores=[]
		for section in course.section_set.order_by('number'):
			course_scores.append((section,calculate_score(user,section),))
		scores.append((course,course_scores),)
	return scores

def student_detail(request):
	if not request.user.is_authenticated:
		raise PermissionDenied
	student=request.user
	return render(request,'students/student_detail.html',{ 'student':student,'scores':get_all_scores_from_user(student)})

	
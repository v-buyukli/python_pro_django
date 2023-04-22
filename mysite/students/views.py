from django.http import HttpResponse
from django.template import loader

from .forms import CountForm
from .models import Student
from .services import students_generator


def index(request):
    template = loader.get_template("students/index.html")
    context = {"form": CountForm()}
    return HttpResponse(template.render(context, request))


def generate_student(request):
    first_name, last_name, age = students_generator.generate_student()
    student = Student.objects.create(first_name=first_name, last_name=last_name, age=age)

    template = loader.get_template("students/generate-student.html")
    context = {"student": student}
    return HttpResponse(template.render(context, request))


def generate_students(request):
    count = int(request.GET.get("count", 10))
    students = students_generator.generate_students(count)
    Student.objects.bulk_create(students)

    template = loader.get_template("students/generate-students.html")
    context = {"students": students}
    return HttpResponse(template.render(context, request))

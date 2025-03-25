from rest_framework import serializers
from .models import Student

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['name', 'student_email', 'locker_number']

class StudentAllSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = [
            'name',
            'student_email',
            'personal_email',
            'locker_number',
            'locker_combination',
            'good_student'
        ]





# install djangorestframework
# in proj settings.py -> add "rest_framework" to INSTALLED_APPS list
# update pip freeze > requirements.txt
# created serializers.py file 
# import serializers from rest_framework and the Student-model from .models (file)
# created Serializer Models 
# Meta defines the model and fields we want to serialize
# makemigrations+migrate and create fixtures/json file(fake data for test)
# in the shell :
# import both the model and the serializer model
# create model-instance-variable = Model.objects.get(attribute/field/id)
# create serialized_variable = SerializedModel(model-instance-variable) the variable we created in the line above 
# (serialized_variable.data) shows the data from the model-instance-variable in a dictionary format
# we can now use dictionary methods to grab data (serialized_variable.data['attribute-name'])        
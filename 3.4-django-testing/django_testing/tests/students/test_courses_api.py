import pytest
from rest_framework.test import APIClient

from students.models import Course, Student


# @pytest.fixture()
# def Clinet(url):
#     client = APIClient()
#     response = client.get(url)
#     return response
@pytest.mark.django_db
def test_example():
    # Arrange
    client = APIClient()
    Student.objects.create(name='Test')
    Course.objects.create(name='Math')

    # Act
    response = client.get('http://127.0.0.1:8000/api/v1/courses/')
    data = response.json()
    # Assert
    assert response.status_code == 200
    assert len(data) == 1

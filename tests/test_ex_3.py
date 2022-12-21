# # function  Run once per test
# # class	  Run once per class of tests
# # module	  Run once per module
# # session	  Run once per session


# import pytest

# from django.contrib.auth.models import User


# @pytest.mark.django_db
# def test_user_create():
#    User.objects.create_user('test', 'test@test.com', 'test')
#    count = User.objects.all().count()
#    print(count)
#    assert User.objects.count() == 1


# @pytest.mark.django_db
# def test_user_create1():
#    count = User.objects.all().count()
#    print(count)
#    assert count == 0


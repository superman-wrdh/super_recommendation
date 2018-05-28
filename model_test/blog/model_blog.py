from model_test.model_test_case import set_up
from uuid import uuid4
from datetime import datetime

if __name__ == '__main__':
    set_up()
    from web_api.models import UserRegCode

    reg = UserRegCode(id=uuid4(), user_id=uuid4(), reg_code=uuid4(), created_time=datetime.now())
    reg.save()
    objects_all = UserRegCode.objects.all()
    print(len(objects_all))

from django.db import models
from django.contrib.auth.models import AbstractUser

ORDINARY_USER,ADMIN,MANAGER=("ordinary_user","admin",'manager')

NEW,CODE_VERIFY,DONE,PHOTO_DONE =("new","code_verify",'done','photo_done')

VIA_EMAIL ,VIA_PHONE=("via_email","via_phone")


class User(AbstractUser):
    USER_ROLE=(
        
    )
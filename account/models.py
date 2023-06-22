from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from ckeditor.fields import RichTextField

# Create your models here.


class MyAccountManager(BaseUserManager):
    # create_user deals with creating the user of costumer type
    def create_user(self, email, name, contact_number, viewpass=None, password=None, ):
        if not email:
            raise ValueError("enter email")
        if not name:
            raise ValueError("enter first name")

        user = self.model(
            email=self.normalize_email(email),
            name=name,
            contact_number=contact_number,
            viewpass=viewpass,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    # def create_vendor(self, shop_number, shop_name, shop_add, plan, gst, vendor, subscripton_amount):

    #     user = self.model(
    #         shop_number=shop_number,
    #         shop_name=shop_name,
    #         shop_add=shop_add,
    #         plan=plan,
    #         gst=gst,
    #         vendor=vendor,
    #         subscripton_amount=subscripton_amount,
    #     )
    #     user.save(using=self._db)
    #     return user

    def create_superuser(self, email, name, contact_number, password):
        user = self.create_user(
            email=self.normalize_email(email),
            name=name,
            contact_number=contact_number,
            # viewpass=viewpass,
            password=password,
        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class Account(AbstractBaseUser):
    email = models.EmailField(verbose_name="email", max_length=100, unique=True)
    viewpass = models.CharField(max_length=30, null=True, blank=True)
    name = models.CharField(max_length=100)
    contact_number = models.CharField(max_length=15, null=True, blank=True)
    credits=models.IntegerField(default=0)
    is_superuser = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    is_startup = models.BooleanField(default=False)
    is_mentor = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name', 'contact_number']

    objects = MyAccountManager()

    def __str__(self):
        return self.email

    def has_module_perms(self, app_label):
        return True

    def has_perm(self, perm, obj=None):
        return self.is_admin

def get_uplaod_file_name(userpic, filename,):
    return u'shop/%s/%s%s' % (str(userpic.vendor_id)+"/template","",filename)
def get_uplaod_file_name_blog(userpic, filename,):
    return u'blog/%s/%s%s' % (str(userpic.blogger_id)+"/template","",filename)

class Startup(models.Model):
    founder = models.OneToOneField(Account, on_delete=models.CASCADE, primary_key=True, )
    email = models.EmailField(verbose_name="email", max_length=100)
    phone = models.CharField(max_length=15, null=True, blank=True)
    STAGE = (
        ('seed', 'Seed'),
        ('revenue', 'Revenue'),
    )
    stage = models.CharField(max_length=20, choices=STAGE,default='seed')
    about = RichTextField(null=True, blank=True,)
    startup_name = models.CharField(max_length=150, unique=True)
    address = models.CharField(max_length=100,blank=True, null=True)
    country = models.CharField(max_length=30,blank=True, null=True)
    state = models.CharField(max_length=20,blank=True, null=True)
    gst = models.CharField(max_length=30 ,null=True, blank=True)
    meetings=models.JSONField(blank=True, null=True)
    is_blocked = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    # objects= MyAccountManager()
    def __str__(self):
        return self.startup_name


def get_uplaod_file_name(userpic, filename,):
    return u'mentor/%s/%s%s' % (str(userpic.mentor_id)+"/profile","",filename)
class Mentor(models.Model):
    mentor = models.OneToOneField(Account, on_delete=models.CASCADE, primary_key=True, )
    email = models.EmailField(verbose_name="email", max_length=100)
    phone = models.CharField(max_length=15, null=True, blank=True)
    about = RichTextField(null=True, blank=True,)
    name= models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    designation = models.CharField(max_length=100)
    interests= models.JSONField(blank=True, null=True , default={"skills": [""]})
    image = models.ImageField(upload_to=get_uplaod_file_name, default="")
    linkedin= models.CharField(max_length=100)
    bio=models.TextField(blank=True, null=True)
    charges_in=models.IntegerField()
    charges_out=models.IntegerField()
    meetings=models.JSONField(blank=True, null=True,default=[])
    application=models.JSONField(blank=True, null=True,default=[])


    is_blocked = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    # objects= MyAccountManager()
    def __str__(self):
        return self.name


class Waitlist(models.Model):
    email = models.EmailField(verbose_name="email", max_length=100)
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15, null=True, blank=True)
    startup_name = models.CharField(max_length=150)

    def __str__(self):
        return self.email
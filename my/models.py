# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models, connection


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Ip(models.Model):
    ip = models.CharField(max_length=40, primary_key=True)
    mac = models.CharField(max_length=30)
    com = models.CharField(max_length=200)

    class Meta:
        managed = False
        db_table = 'ip'


class Mac(models.Model):
    mac = models.CharField(max_length=30, primary_key=True)
    switch = models.CharField(max_length=40)
    port = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'mac'


class NetManager(models.Manager):
    def get_203_all(self):
        cursor = connection.cursor()
        cursor.execute("""select A.ip,A.mac,B.switch,B.port,A.com 
                                                   from ip as A , mac as B 
                                                   where A.mac = B.mac  and A.ip like '203%'
                                                   order by A.ip
                                                   """)
        rows = cursor.fetchall()
        return [r for i in range(1,255) for r in rows if r[0] == ("203.68.236." + str(i))]

    def get_203_ip(self, ip):
        cursor = connection.cursor()
        cursor.execute("""select A.ip,A.mac,B.switch,B.port,A.com 
                                                   from ip as A , mac as B 
                                                   where A.mac = B.mac  and A.ip like '203%'
                                                   order by A.ip
                                                   """)
        return [r  for r in cursor.fetchall() if r[0] == ip ]

    def get_203_range(self, ip1,ip2):
        cursor = connection.cursor()
        cursor.execute("""select A.ip,A.mac,B.switch,B.port,A.com 
                                                   from ip as A , mac as B 
                                                   where A.mac = B.mac  and A.ip like '203%'
                                                   order by A.ip
                                                   """)
        rows = cursor.fetchall()
        return [r for i in range(ip1, ip2 + 1) for r in rows if r[0] == ("203.68.236." + str(i))]

    def get_10_all(self):
        cursor = connection.cursor()
        cursor.execute("""select A.ip,A.mac,B.switch,B.port,A.com 
                                                   from ip as A , mac as B 
                                                   where A.mac = B.mac  and A.ip like '10%'
                                                   order by A.ip
                                                   """)
        rows = cursor.fetchall()
        return [r  for r in rows]

class My(models.Model):
    netManager = NetManager()
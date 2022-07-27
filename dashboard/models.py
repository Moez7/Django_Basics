# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class BaseReseauCommerciaux(models.Model):
    entite = models.ForeignKey('Groupe', models.DO_NOTHING, db_column='ENTITE', blank=True, null=True)  # Field name made lowercase.
    entite2 = models.CharField(db_column='ENTITE2', primary_key=True, max_length=50, db_collation='French_CI_AS')  # Field name made lowercase.
    agence_client_libelle = models.CharField(db_column='AGENCE_CLIENT_LIBELLE', max_length=50, db_collation='French_CI_AS', blank=True, null=True)  # Field name made lowercase.
    agence_client_zone = models.IntegerField(db_column='AGENCE_CLIENT_ZONE', blank=True, null=True)  # Field name made lowercase.
    client_zone_libelle = models.CharField(db_column='CLIENT_ZONE_LIBELLE', max_length=50, db_collation='French_CI_AS', blank=True, null=True)  # Field name made lowercase.
    client_zone_region = models.IntegerField(db_column='CLIENT_ZONE_REGION', blank=True, null=True)  # Field name made lowercase.
    client_region_libelle = models.CharField(db_column='CLIENT_REGION_LIBELLE', max_length=8000, db_collation='French_CI_AS', blank=True, null=True)  # Field name made lowercase.
    lib = models.CharField(db_column='LIB', max_length=50, db_collation='French_CI_AS', blank=True, null=True)  # Field name made lowercase.
    fonction = models.CharField(db_column='Fonction', max_length=50, db_collation='French_CI_AS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Base_Reseau_Commerciaux'



class Groupe(models.Model):
    entite = models.CharField(db_column='ENTITE', primary_key=True, max_length=50, db_collation='French_CI_AS')  # Field name made lowercase.
    groupe = models.CharField(db_column='GROUPE', max_length=50, db_collation='French_CI_AS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Groupe'


class Indicateurs(models.Model):
    id_menu = models.FloatField(db_column='ID_MENU', blank=True, null=True)  # Field name made lowercase.
    id_ss_menu = models.FloatField(db_column='ID_SS_MENU', blank=True, null=True)  # Field name made lowercase.
    ordre = models.FloatField(db_column='ORDRE', blank=True, null=True)  # Field name made lowercase.
    ref = models.FloatField(db_column='REF', primary_key=True)  # Field name made lowercase.
    libelle_indicateur = models.CharField(db_column='Libelle_Indicateur', max_length=50, db_collation='French_CI_AS', blank=True, null=True)  # Field name made lowercase.
    poids_indicateur = models.FloatField(db_column='Poids_Indicateur', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Indicateurs'




class RealisationPilotage(models.Model):
    id_menu = models.FloatField(db_column='ID_MENU', blank=True, null=True)  # Field name made lowercase.
    id_ss_menu = models.FloatField(db_column='ID_SS_MENU', blank=True, null=True)  # Field name made lowercase.
    ordre = models.FloatField(db_column='ORDRE', blank=True, null=True)  # Field name made lowercase.
    date_situation = models.FloatField(db_column='DATE_SITUATION', blank=True, null=True)  # Field name made lowercase.
    entite = models.ForeignKey(BaseReseauCommerciaux, models.DO_NOTHING, db_column='ENTITE', blank=True, null=True)  # Field name made lowercase.
    segment = models.CharField(db_column='SEGMENT', max_length=50, db_collation='French_CI_AS', blank=True, null=True)  # Field name made lowercase.
    ref = models.ForeignKey(Indicateurs, models.DO_NOTHING, db_column='REF', blank=True, null=True)  # Field name made lowercase.
    agence_realisation = models.CharField(db_column='AGENCE_REALISATION', max_length=50, db_collation='French_CI_AS', blank=True, null=True)  # Field name made lowercase.
    n_1 = models.CharField(db_column='N_1', max_length=50, db_collation='French_CI_AS', blank=True, null=True)  # Field name made lowercase.
    n = models.CharField(db_column='N', max_length=50, db_collation='French_CI_AS', blank=True, null=True)  # Field name made lowercase.
    objectif_s1 = models.CharField(db_column='OBJECTIF_S1', max_length=50, db_collation='French_CI_AS', blank=True, null=True)  # Field name made lowercase.
    rar = models.FloatField(db_column='RAR', blank=True, null=True)  # Field name made lowercase.
    tro = models.FloatField(db_column='TRO', blank=True, null=True)  # Field name made lowercase.
    trpp = models.FloatField(db_column='TRPP', blank=True, null=True)  # Field name made lowercase.
    objectif = models.CharField(db_column='OBJECTIF', max_length=50, db_collation='French_CI_AS', blank=True, null=True)  # Field name made lowercase.
    resultat = models.FloatField(db_column='RESULTAT', blank=True, null=True)  # Field name made lowercase.
    score = models.CharField(db_column='SCORE', max_length=50, db_collation='French_CI_AS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Realisation_Pilotage'





class Score(models.Model):
    segment = models.CharField(db_column='SEGMENT', max_length=255, db_collation='French_CI_AS', blank=True, null=True)  # Field name made lowercase.
    indicateur = models.CharField(db_column='INDICATEUR', max_length=255, db_collation='French_CI_AS', blank=True, null=True)  # Field name made lowercase.
    score = models.FloatField(db_column='SCORE', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Score'


class StockClient(models.Model):
    client_id = models.IntegerField(db_column='CLIENT_ID', blank=True, null=True)  # Field name made lowercase.
    agence_client_ctos = models.CharField(db_column='AGENCE_CLIENT_CTOS', max_length=50, db_collation='French_CI_AS', blank=True, null=True)  # Field name made lowercase.
    zone = models.CharField(db_column='ZONE', max_length=50, db_collation='French_CI_AS', blank=True, null=True)  # Field name made lowercase.
    region = models.CharField(db_column='REGION', max_length=50, db_collation='French_CI_AS', blank=True, null=True)  # Field name made lowercase.
    client_nom = models.CharField(db_column='CLIENT_NOM', max_length=50, db_collation='French_CI_AS', blank=True, null=True)  # Field name made lowercase.
    client_marche = models.CharField(db_column='CLIENT_MARCHE', max_length=50, db_collation='French_CI_AS', blank=True, null=True)  # Field name made lowercase.
    segment = models.CharField(db_column='SEGMENT', max_length=50, db_collation='French_CI_AS', blank=True, null=True)  # Field name made lowercase.
    sous_segment = models.CharField(db_column='SOUS_SEGMENT', max_length=8000, db_collation='French_CI_AS', blank=True, null=True)  # Field name made lowercase.
    client_secteur_activite = models.IntegerField(db_column='CLIENT_SECTEUR_ACTIVITE', blank=True, null=True)  # Field name made lowercase.
    client_email_1 = models.CharField(db_column='CLIENT_EMAIL_1', max_length=50, db_collation='French_CI_AS', blank=True, null=True)  # Field name made lowercase.
    client_email_2 = models.CharField(db_column='CLIENT_EMAIL_2', max_length=50, db_collation='French_CI_AS', blank=True, null=True)  # Field name made lowercase.
    client_email_3 = models.CharField(db_column='CLIENT_EMAIL_3', max_length=50, db_collation='French_CI_AS', blank=True, null=True)  # Field name made lowercase.
    client_telephone_1 = models.CharField(db_column='CLIENT_TELEPHONE_1', max_length=50, db_collation='French_CI_AS', blank=True, null=True)  # Field name made lowercase.
    client_telephone_2 = models.CharField(db_column='CLIENT_TELEPHONE_2', max_length=50, db_collation='French_CI_AS', blank=True, null=True)  # Field name made lowercase.
    client_telephone_3 = models.CharField(db_column='CLIENT_TELEPHONE_3', max_length=50, db_collation='French_CI_AS', blank=True, null=True)  # Field name made lowercase.
    client_telephone_4 = models.CharField(db_column='CLIENT_TELEPHONE_4', max_length=50, db_collation='French_CI_AS', blank=True, null=True)  # Field name made lowercase.
    client_profession = models.CharField(db_column='CLIENT_PROFESSION', max_length=50, db_collation='French_CI_AS', blank=True, null=True)  # Field name made lowercase.
    client_age = models.IntegerField(db_column='CLIENT_AGE', blank=True, null=True)  # Field name made lowercase.
    client_vrd = models.IntegerField(db_column='CLIENT_VRD', blank=True, null=True)  # Field name made lowercase.
    client_mmm = models.IntegerField(db_column='CLIENT_MMM', blank=True, null=True)  # Field name made lowercase.
    client_encours_engagement = models.IntegerField(db_column='CLIENT_ENCOURS_ENGAGEMENT', blank=True, null=True)  # Field name made lowercase.
    client_portefeuille = models.CharField(db_column='CLIENT_PORTEFEUILLE', max_length=50, db_collation='French_CI_AS', blank=True, null=True)  # Field name made lowercase.
    client_portefeuille_type = models.CharField(db_column='CLIENT_PORTEFEUILLE_TYPE', max_length=50, db_collation='French_CI_AS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Stock_Client'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150, db_collation='French_CI_AS')

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255, db_collation='French_CI_AS')
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100, db_collation='French_CI_AS')

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128, db_collation='French_CI_AS')
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150, db_collation='French_CI_AS')
    first_name = models.CharField(max_length=150, db_collation='French_CI_AS')
    last_name = models.CharField(max_length=150, db_collation='French_CI_AS')
    email = models.CharField(max_length=254, db_collation='French_CI_AS')
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class BlogPost(models.Model):
    id = models.BigAutoField(primary_key=True)
    title = models.CharField(max_length=100, db_collation='French_CI_AS')
    content = models.TextField(db_collation='French_CI_AS')
    date_posted = models.DateTimeField()
    author = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'blog_post'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(db_collation='French_CI_AS', blank=True, null=True)
    object_repr = models.CharField(max_length=200, db_collation='French_CI_AS')
    action_flag = models.SmallIntegerField()
    change_message = models.TextField(db_collation='French_CI_AS')
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100, db_collation='French_CI_AS')
    model = models.CharField(max_length=100, db_collation='French_CI_AS')

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255, db_collation='French_CI_AS')
    name = models.CharField(max_length=255, db_collation='French_CI_AS')
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40, db_collation='French_CI_AS')
    session_data = models.TextField(db_collation='French_CI_AS')
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class PredictPredresults(models.Model):
    id = models.BigAutoField(primary_key=True)
    sepal_length = models.FloatField()
    sepal_width = models.FloatField()
    petal_length = models.FloatField()
    petal_width = models.FloatField()
    classification = models.CharField(max_length=30, db_collation='French_CI_AS')

    class Meta:
        managed = False
        db_table = 'predict_predresults'


class Sysdiagrams(models.Model):
    name = models.CharField(max_length=128, db_collation='French_CI_AS')
    principal_id = models.IntegerField()
    diagram_id = models.AutoField(primary_key=True)
    version = models.IntegerField(blank=True, null=True)
    definition = models.BinaryField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sysdiagrams'
        unique_together = (('principal_id', 'name'),)


class UsersProfile(models.Model):
    id = models.BigAutoField(primary_key=True)
    image = models.CharField(max_length=100, db_collation='French_CI_AS')
    user = models.OneToOneField(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'users_profile'

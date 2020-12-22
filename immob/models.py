from django.db import models

from django.contrib.auth.models import AbstractUser, PermissionsMixin, BaseUserManager
from django.conf import settings

class UserManager(BaseUserManager):

    use_in_migrations = True
    
    def _create_user(self, username, email, phone, password, **extra_fields):

        values = [username, email, phone]
        field_value_map = dict(zip(self.model.REQUIRED_FIELDS, values))
        for field_name, value in field_value_map.items():
            if not value:
                raise ValueError("Le champ {} doit etre rempli".format(field_name))
        
        email = self.normalize_email(email)
        user = self.model(
            username=username,
            email=email,
            phone=phone,
            **extra_fields
        )

        user.set_password(password)
        user.save(using=self._db)
        return user


    def create_user(self, username, email, phone, password, **extra_fields):

        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_active') is not True:
            raise ValueError("Une lié au droit d'accès c'est produite")

        return self._create_user(username, email, phone, password, **extra_fields)

    def create_superuser(self, username, email, phone, password=None, **extra_fields):

        extra_fields.setdefault('is_staff', True),
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError("Le champ is staff ne pas être faux pour l'admin")
        if extra_fields.get('is_superuser') is not True:
            raise ValueError("Le champ is superuser ne pas être faux pour l'admin")
        if extra_fields.get('is_active') is not True:
            raise ValueError("Le champ is active ne pas être faux pour l'admin")

        return self._create_user(username, email, phone, password, **extra_fields)
class User(AbstractUser, PermissionsMixin):

    username = models.CharField('Nom utilisateur', max_length=50, unique=True)
    first_name = models.CharField('Nom', max_length=50, null=True)
    first_name = models.CharField('Prénom', max_length=50, null=True)
    email =  models.EmailField(max_length=254, unique=True)
    phone = models.CharField('Contact', max_length=30, unique=True)
    news = models.BooleanField("Je souhaite m'abonner à la newslater")
    ag_admin = models.BooleanField("Administrateur agence", default=False)
    is_superuser = models.BooleanField(default=False)
    
    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'phone']

    def __str__(self):

        return self.username

    def save(self, *args, **kwargs):

        self.passord = self.set_password(self.password)
        super(User, self).save(*args, **kwargs)



class Agence(models.Model):

    nom = models.CharField("Nom agence", max_length=128)
    status = models.BooleanField("Aggréer ou non", default=False)
    Commune = models.ForeignKey("Ville", verbose_name="Ville ou commune", on_delete=models.CASCADE)
    localite = models.CharField("Adresse postale", max_length=254)
    numero_agr = models.CharField("Numéro d'aggregation", max_length=50)
    regi_commerce = models.CharField("Regis de commerce", max_length=128)
    num_cpte = models.CharField("Numero de compte contribiable", max_length=50)
    dg = models.OneToOneField("User", verbose_name="Propriétaire", on_delete=models.CASCADE)


class Ville(models.Model):
    
    ville = models.CharField(max_length=128)

    def __str__(self):
        return self.ville

    
class Types(models.Model):

    libele = models.CharField(max_length=128)

    def __str__(self):
        return self.libele


class Offre(models.Model):
    
    titre = models.CharField(max_length=128)

    

    def __str__(self):
        return self.titre

class Demande(models.Model):
    
    libele = models.CharField(max_length=128)

    def __str__(self):
        return self.libele


class Immobilier(models.Model):
    
    type_immob = models.ForeignKey("Types", verbose_name="Type de bien", on_delete=models.CASCADE)
    nombre = models.IntegerField("Nombre de pièces")
    surface = models.IntegerField("Surface en m²")
    commune = models.ForeignKey("Ville", verbose_name="Ville ou commune", on_delete=models.CASCADE)
    prix = models.IntegerField("Prix de loyer souhaité")
    adresse = models.CharField("Adresse postale", max_length=254)
    image = models.ImageField(upload_to=settings.MEDIA_ROOT)
    image_1 = models.ImageField(upload_to=settings.MEDIA_ROOT)
    image_2 = models.ImageField(upload_to=settings.MEDIA_ROOT, blank=True, null=True)
    desc = models.TextField("Description du bien")
    status = models.ForeignKey("Offre", verbose_name="Faite un choix", on_delete=models.CASCADE)
    user = models.ForeignKey("User", verbose_name="Propriétaire", on_delete=models.CASCADE)


   
    def __str__(self):
        return self.type_immob


class Besoins(models.Model):

    type_bien = models.ForeignKey("Types", verbose_name="Type de bien", on_delete=models.CASCADE)
    nombre = models.IntegerField("Nombre de pièces")
    surface = models.IntegerField("Surface minimale en m²")
    prix = models.IntegerField("Prix minimum")
    prix_2 = models.IntegerField("Prix maximum")
    demande = models.ForeignKey("Demande", verbose_name="Type de besoin", on_delete=models.CASCADE)
    commune = models.ForeignKey("Ville", verbose_name="Ville ou commune", on_delete=models.CASCADE)
    adresse = models.CharField("Adresse postale", max_length=254)
    user = models.ForeignKey("User", verbose_name="Demandeur", on_delete=models.CASCADE)

    def __str__(self):
        return self.type_besoin

   


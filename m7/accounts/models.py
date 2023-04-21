import uuid
from decimal import Decimal
from django.db import models
from django.db.models import Sum
from django.utils import timezone
from django_lifecycle import hook, LifecycleModelMixin
from django.contrib.auth.models import AbstractBaseUser, UserManager, PermissionsMixin

from django.utils.translation import gettext_lazy as _

from m7.contracts.models import Contract
from m7.dividends.models import Dividend


class User(LifecycleModelMixin, AbstractBaseUser, PermissionsMixin):
    id = models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True)

    username = models.CharField(
        _('username'),
        max_length=150,
        unique=True,
        help_text=(
            '150 caracteres ou menos. Letras, números e @/./+/-/_ apenas.'),
        error_messages={
            'unique': _("A user with that username already exists."),
        }
    )
    first_name = models.CharField(_('first name'), max_length=30, blank=True)

    last_name = models.CharField(_('last name'), max_length=150, blank=True)

    email = models.EmailField(_('email address'), unique=True)
    date_joined = models.DateTimeField(_('date joined'), default=timezone.now)

    is_staff = models.BooleanField(
        _('staff status'),
        default=False,
        help_text=_(
            'Designates whether the user can log into this admin site.'),
    )
    is_active = models.BooleanField(
        _('active'),
        default=True,
        help_text=_(
            'Designates whether this user should be treated as active. '
            'Unselect this instead of deleting accounts.'
        ),
    )

    objects = UserManager()
    
    EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', ]

    class Meta:
        verbose_name = 'Usuário'
        verbose_name_plural = 'Usuários'
        permissions = [
            # ("can_edit_salon", "Pode editar as configurações do estabelecimento"),
        ]

    def __str__(self):
        return f'{self.first_name} {self.last_name}' if self.first_name else self.email

    def my_contracts(self):
        return Contract.objects.filter(
            user=self
        )
    
    def my_dividends(self):
        return Dividend.objects.filter(
            contract__in=self.my_contracts()
        )

    def get_total_count_contracts(self):
        return self.my_contracts().count()

    def get_total_contributions(self):
        return self.my_contracts().total_contribution() or 0
    
    def get_total_contributions_activies_contract(self):
        return self.my_contracts().activies().total_contribution() or 0
    
    def get_avarage_percent_activies_contract(self):
        return self.my_contracts().activies().avarage_percent() or 0
    
    def get_total_dividends_received(self):
        return self.my_dividends().total_received() or 0
    
    def get_percent_invest(self):
        total_contributions = self.get_total_contributions()
        if total_contributions > 0:
            return int(
                (Decimal(self.get_total_dividends_received()) / Decimal(self.get_total_contributions()))*100
            )
        
        return 0


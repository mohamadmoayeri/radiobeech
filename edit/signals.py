from django_cleanup.signals import cleanup_pre_delete

from django.db.models.signals import pre_delete,pre_save

from django.dispatch import receiver

from sorl.thumbnail import delete

from home.models import story

from profiles.models import personal_information

from django.core.cache import cache


def sorl_delete(**kwargs):
    delete(kwargs['file'])
    
cleanup_pre_delete.connect(sorl_delete)


@receiver(pre_delete,sender=story)
def del_story(sender,**kwargs):
    cache.clear()


@receiver(pre_delete,sender=personal_information)
def del_person(sender,**kwargs):
    cache.clear()


@receiver(pre_save,sender=story)
def save_story(sender,**kwargs):
    cache.clear()

@receiver(pre_save,sender=personal_information)
def save_person(sender,**kwargs):
    cache.clear()


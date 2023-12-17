from django.db import models


class CosmoPerson(models.Model):
    name = models.CharField(max_length=255, verbose_name='Name')
    born = models.CharField(max_length=255, verbose_name='Born')
    died = models.CharField(max_length=255, verbose_name='Died')
    cause_of_death = models.CharField(max_length=255, verbose_name='Cause of death')
    nationality = models.CharField(max_length=255, verbose_name='Nationality')
    time_in_space = models.CharField(max_length=255, verbose_name='Time in space')
    missions = models.CharField(max_length=255, verbose_name='Missions')
    years_of_service = models.CharField(max_length=255, verbose_name='Years of service')
    image = models.ImageField(upload_to="media/", null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ("-created_at",)
        verbose_name = "Kosmonavt"
        verbose_name_plural = "Kosmonavtlar"


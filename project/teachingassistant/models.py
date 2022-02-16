"""Models relating to Teaching Assistants."""
from django.db import models


class TA(models.Model):
    """TA Object. Primary key is predefined as an integer value by Django."""

    class Meta:
        """Metadata regarding TA's."""

        verbose_name = 'TA'
        verbose_name_plural = 'TA\'s'

    def __str__(self):
        """Human readable class name, for admin site."""
        human_readable_name = ""
        if self.year == 'GR':
            # flag the TA as a 'G'TA
            # NOTE: we can change the admin site to display an arrow or
            #       something if the TA is a GTA (or if they're contracted)
            human_readable_name += 'G'
        human_readable_name += 'TA ' + self.first_name + ' ' + self.last_name
        return human_readable_name

    # define choice variable
    YEAR = (
        ('FR', 'Freshman'),
        ('SO', 'Sophomore'),
        ('JR', 'Junior'),
        ('SR', 'Senior'),
        ('GR', 'Graduate')
        )

    # define fields
    first_name = models.CharField('TA\'s first name',
                                  max_length=50, default='missing')
    last_name = models.CharField('TA\'s last name',
                                 max_length=50, default='missing')
    student_id = models.CharField('TA\'s student ID', max_length=50,
                                  unique=True, blank=True)

    contracted = models.BooleanField('Contracted', blank=True, null=True)

    # experience needs to be configured to account for whatever
    # we want to display experience/relevant skills as
    experience = models.CharField('TA\'s experience', max_length=100,
                                  blank=True)

    year = models.CharField('TA\'s current year', max_length=2,
                            choices=YEAR, blank=True)


class Availability(models.Model):
    """Object representing a single TA's availability."""

    class Meta:
        """Metadata regarding Availability objects."""

        verbose_name = 'Availability'
        verbose_name_plural = 'Availability\'s'

    def __str__(self):
        """Human readable object name."""
        return f'{self.ta}\'s Availability'

    monday_start = models.TimeField(auto_now=False, auto_now_add=False,
                                    blank=True, null=True)
    monday_end = models.TimeField(auto_now=False, auto_now_add=False,
                                  blank=True, null=True)
    tuesday_start = models.TimeField(auto_now=False, auto_now_add=False,
                                     blank=True, null=True)
    tuesday_end = models.TimeField(auto_now=False, auto_now_add=False,
                                   blank=True, null=True)
    wednesday_start = models.TimeField(auto_now=False, auto_now_add=False,
                                       blank=True, null=True)
    wednesday_end = models.TimeField(auto_now=False, auto_now_add=False,
                                     blank=True, null=True)
    thursday_start = models.TimeField(auto_now=False, auto_now_add=False,
                                      blank=True, null=True)
    thursday_end = models.TimeField(auto_now=False, auto_now_add=False,
                                    blank=True, null=True)
    friday_start = models.TimeField(auto_now=False, auto_now_add=False,
                                    blank=True, null=True)
    friday_end = models.TimeField(auto_now=False, auto_now_add=False,
                                  blank=True, null=True)
    saturday_start = models.TimeField(auto_now=False, auto_now_add=False,
                                      blank=True, null=True)
    saturday_end = models.TimeField(auto_now=False, auto_now_add=False,
                                    blank=True, null=True)
    sunday_start = models.TimeField(auto_now=False, auto_now_add=False,
                                    blank=True, null=True)
    sunday_end = models.TimeField(auto_now=False, auto_now_add=False,
                                  blank=True, null=True)

    # key to TA
    ta = models.OneToOneField(TA, on_delete=models.CASCADE)


class Holds(models.Model):
    """Possible holds to be applied to TA accounts."""

    class Meta:
        """Metadata regarding Holds objects."""

        verbose_name = 'Holds'
        verbose_name_plural = 'Holds'

    def __str__(self):
        """Human readable object name."""
        return f'{self.ta}\'s Holds'

    # if the TA has not completed the initialization of their profile
    # NOTE: defaults to true such that a new TA will be required
    #       to update their profile before being scheduled
    incomplete_profile = models.BooleanField('Incomplete profile',
                                             default=True)

    # if the TA needs to update their availability
    update_availability = models.BooleanField('Update availability!',
                                              default=False)

    # if the TA needs to update their experience
    update_experience = models.BooleanField('Update experience!',
                                            default=False)

    # if the TA has no holds
    no_holds = models.BooleanField('No holds', default=False)

    # key to TA
    ta = models.OneToOneField(TA, on_delete=models.CASCADE)

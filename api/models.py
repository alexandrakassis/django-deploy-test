from django.db import models

# Create your models here.
class Cycle(models.Model):
    experiment_id = models.IntegerField(default=0)
    cycle_id = models.AutoField(primary_key=True)
    batch_id = models.IntegerField(default=0)
    step_number = models.IntegerField(default=0)
    temperature = models.DecimalField(max_digits=5, decimal_places=1, default=0.0)
    humidity = models.DecimalField(max_digits=5, decimal_places=1, default=0.0)
    aa_checked = models.BooleanField(default=False)
    cycle_start_time = models.DateTimeField(null=True, blank=True)
    cycle_end_time = models.DateTimeField(null=True, blank=True)
    time_per_cycle = models.DurationField(null=True, blank=True)
    recipe = models.CharField(max_length=100, null=True, default="")
    mask = models.CharField(max_length=100, null=True, default="")
    amino_id = models.CharField(max_length=100, null=True, default="")
    amino = models.CharField(max_length=20, null=True, default="")
    notes = models.CharField(max_length=300, null=True, default="")
    
    def __str__(self):
        return f"Cycle ID {self.cycle_id} in Experiment {self.experiment_id}"
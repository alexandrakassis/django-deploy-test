#translate cycle data into a json response

from rest_framework import serializers
from .models import Cycle

class CycleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cycle
        fields = ('cycle_id', 
                  'experiment_id', 
                  'batch_id', 
                  'step_number',
                  'temperature', 
                  'humidity', 
                  'cycle_start_time', 
                  'cycle_end_time',
                  'aa_checked',
                  'notes'
                  )
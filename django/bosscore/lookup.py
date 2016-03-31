
from .serializers import BossLookupSerializer
from .models import BossLookup


class LookUpKey:
    """
    Bosskey manager

    """
    @staticmethod
    def add_lookup(lookup_key, boss_key, collection_name, experiment_name=None,
                   channel_layer_name=None, max_time_sample=None):
        """
        Add the lookup key that correspond to a data model object
        Args:
            lookup_key: Lookup key for the object that was created
            boss_key: Bosskey for the objec that we created
            collection_name: Collection name . Matches the collection in the bosskey
            experiment_name: Experiment name . Matches the experiment in the bosskey
            channel_layer_name: Channel or Layer name . Matches the channel or layer in the bosskey
            max_time_sample: Time sample (optional argument)

        Returns: None

        """
        # Create the boss lookup key

        lookup_data = {'lookup_key': lookup_key, 'boss_key': boss_key,
                       'collection_name': collection_name,
                       'experiment_name': experiment_name,
                       'channel_layer_name': channel_layer_name
                       }
        serializer = BossLookupSerializer(data=lookup_data)
        if serializer.is_valid():
            serializer.save()

            if collection_name and experiment_name and channel_layer_name and max_time_sample:
                # Add lookup keys for all timesamples for the channel and layer
                for time in range(max_time_sample+1):
                    lookup_data['lookup_key'] = lookup_key + '&' + str(time)
                    lookup_data['boss_key'] = boss_key + '&' + str(time)

                    serializer = BossLookupSerializer(data=lookup_data)
                    if serializer.is_valid():
                        serializer.save()

    @staticmethod
    def get_lookup_key(bkey):
        """
        Get the lookup keys for a request
        Args:
            bkey: Bosskey that corresponds to a request

        Returns:

        """
        lookup_obj = BossLookup.objects.get(boss_key=bkey)
        return lookup_obj
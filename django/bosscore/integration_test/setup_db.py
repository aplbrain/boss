from ..models import *


class setupTestDB:
    @staticmethod
    def insert_test_data():
        col = Collection.objects.create(name='col1')
        lkup_key = str(col.pk)
        bs_key = col.name
        BossLookup.objects.create(lookup_key=lkup_key, boss_key=bs_key, collection_name=col.name)

        cf = CoordinateFrame.objects.create(name='cf1', description='cf1',
                                            x_start=0, x_stop=1000,
                                            y_start=0, y_stop=1000,
                                            z_start=0, z_stop=1000,
                                            x_voxel_size=4, y_voxel_size=4, z_voxel_size=4,
                                            time_step=1
                                            )
        exp = Experiment.objects.create(name='exp1', collection=col, coord_frame=cf, max_time_sample=10)
        lkup_key = str(col.pk) + '&' + str(exp.pk)
        bs_key = col.name + '&' + str(exp.name)
        BossLookup.objects.create(lookup_key=lkup_key, boss_key=bs_key, collection_name=col.name,
                                  experiment_name=exp.name)

        channel = ChannelLayer.objects.create(name='channel1', experiment=exp, is_channel=True, default_time_step=1)
        lkup_key = str(col.pk) + '&' + str(exp.pk) + '&' + str(channel.pk)
        bs_key = col.name + '&' + exp.name + '&' + channel.name
        BossLookup.objects.create(lookup_key=lkup_key, boss_key=bs_key,
                                  collection_name=col.name,
                                  experiment_name=exp.name,
                                  channel_layer_name=channel.name
                                  )
        layer = ChannelLayer.objects.create(name='layer1', experiment=exp, is_channel=False, default_time_step=1)
        lkup_key = str(col.pk) + '&' + str(exp.pk) + '&' + str(layer.pk)
        bs_key = col.name + '&' + exp.name + '&' + layer.name
        BossLookup.objects.create(lookup_key=lkup_key, boss_key=bs_key,
                                  collection_name=col.name,
                                  experiment_name=exp.name,
                                  channel_layer_name=layer.name
                                  )

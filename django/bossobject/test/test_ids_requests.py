# Copyright 2016 The Johns Hopkins University Applied Physics Laboratory
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from rest_framework.test import APITestCase
from django.conf import settings
from rest_framework.test import force_authenticate
from rest_framework.test import APIRequestFactory

from bosscore.request import BossRequest
from bosscore.error import BossError
from bosscore.test.setup_db import SetupTestDB
from bossobject.views import Reserve

version = settings.BOSS_VERSION


class ReserveIdRequestTests(APITestCase):
    """
    Class to test boss requests for the reserve id service
    """

    def setUp(self):
        """
            Initialize the database
            :return:
        """
        self.rf = APIRequestFactory()

        dbsetup = SetupTestDB()
        self.user = dbsetup.create_user()
        dbsetup.set_user(self.user)
        self.client.force_login(self.user)
        dbsetup.insert_spatialdb_test_data()

    def test_request_ids_service(self):
        """
        Test initialization of cutout requests for the datamodel
        :return:
        """
        url = '/' + version + '/ids/col1/exp1/layer1/0/0:6/0:10/0:2/'
        col = 'col1'
        exp = 'exp1'
        channel = 'layer1'
        boss_key = 'col1&exp1&layer1'
        resolution = 0


        # Create the request
        request = self.rf.get(url)
        force_authenticate(request, user=self.user)
        drfrequest = Reserve().initialize_request(request)
        drfrequest.version = version

        # Create the request dict
        request_args = {
            "service": "ids",
            "version": version,
            "collection_name": col,
            "experiment_name": exp,
            "channel_name": channel,
            "resolution": resolution,
            "x_args": "0:6",
            "y_args": "0:10",
            "z_args": "0:2",
            "time_args": None

        }
        ret = BossRequest(drfrequest, request_args)
        self.assertEqual(ret.get_collection(), col)
        self.assertEqual(ret.get_experiment(), exp)
        self.assertEqual(ret.get_channel(), channel)
        self.assertEqual(ret.get_boss_key(), boss_key)

    def test_request_ids_service_invalid_channel_type(self):
        """
        Test initialization of cutout requests for the datamodel
        :return:
        """
        """
        Test initialization of cutout requests for the datamodel
        :return:
        """
        url = '/' + version + '/ids/col1/exp1/channel1/0/0:6/0:10/0:2/'
        col = 'col1'
        exp = 'exp1'
        channel = 'channel1'
        boss_key = 'col1&exp1&channel1'
        resolution = 0

        # Create the request
        request = self.rf.get(url)
        force_authenticate(request, user=self.user)
        drfrequest = Reserve().initialize_request(request)
        drfrequest.version = version

        # Create the request dict
        request_args = {
            "service": "ids",
            "version": version,
            "collection_name": col,
            "experiment_name": exp,
            "channel_name": channel,
            "resolution": resolution,
            "x_args": "0:6",
            "y_args": "0:10",
            "z_args": "0:2",
            "time_args": None

        }

        with self.assertRaises(BossError):
            ret = BossRequest(drfrequest, request_args)



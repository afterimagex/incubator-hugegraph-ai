# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.


from abc import ABC
from pyhugegraph.utils.huge_router import HGraphRouter
from pyhugegraph.utils.huge_requests import HGraphSession


# todo: rename -> HGraphMetaData or delete
class ParameterHolder:
    def __init__(self):
        self._dic = {}

    def set(self, key, value):
        self._dic[key] = value

    def get_value(self, key):
        if key not in self._dic:
            return None
        return self._dic[key]

    def get_dic(self):
        return self._dic

    def get_keys(self):
        return self._dic.keys()


class HGraphContext(ABC):
    def __init__(self, sess: HGraphSession) -> None:
        self._sess = sess
        self._cache = {}  # todo: move parameter_holder to cache

    def close(self):
        self._sess.close()


# todo: rename -> HGraphModule | HGraphRouterable | HGraphModel
class HugeParamsBase(HGraphContext, HGraphRouter):
    def __init__(self, sess: HGraphSession) -> None:
        super().__init__(sess)
        self._parameter_holder = None

    def add_parameter(self, key, value):
        self._parameter_holder.set(key, value)

    def get_parameter_holder(self):
        return self._parameter_holder

    def create_parameter_holder(self):
        self._parameter_holder = ParameterHolder()

    def clean_parameter_holder(self):
        self._parameter_holder = None

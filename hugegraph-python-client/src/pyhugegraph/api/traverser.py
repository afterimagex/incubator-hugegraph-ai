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
import json

from pyhugegraph.api.common import HugeParamsBase
from pyhugegraph.utils.exceptions import NotFoundError
from pyhugegraph.utils.util import check_if_success


class TraverserManager(HugeParamsBase):

    def k_out(self, source_id, max_depth):
        uri = f'traversers/kout?source="{source_id}"&max_depth={max_depth}'
        response = self._sess.get(uri)
        if check_if_success(response, NotFoundError(response.content)):
            return response.json()
        return {}

    def k_neighbor(self, source_id, max_depth):
        uri = f'traversers/kneighbor?source="{source_id}"&max_depth={max_depth}'
        response = self._sess.get(uri)
        if check_if_success(response, NotFoundError(response.content)):
            return response.json()
        return {}

    def same_neighbors(self, vertex_id, other_id):
        uri = f'traversers/sameneighbors?vertex="{vertex_id}"&other="{other_id}"'
        response = self._sess.get(uri)
        if check_if_success(response, NotFoundError(response.content)):
            return response.json()
        return {}

    def jaccard_similarity(self, vertex_id, other_id):
        uri = f'traversers/jaccardsimilarity?vertex="{vertex_id}"&other="{other_id}"'
        response = self._sess.get(uri)
        if check_if_success(response, NotFoundError(response.content)):
            return response.json()
        return {}

    def shortest_path(self, source_id, target_id, max_depth):
        uri = (
            "traversers/shortestpath?"
            f'source="{source_id}"&target="{target_id}"&max_depth={max_depth}'
        )
        response = self._sess.get(uri)
        if check_if_success(response, NotFoundError(response.content)):
            return response.json()
        return {}

    def all_shortest_paths(self, source_id, target_id, max_depth):
        uri = (
            "traversers/allshortestpaths?"
            f'source="{source_id}"&target="{target_id}"&max_depth={max_depth}'
        )
        response = self._sess.get(uri)
        if check_if_success(response, NotFoundError(response.content)):
            return response.json()
        return {}

    def weighted_shortest_path(self, source_id, target_id, weight, max_depth):
        uri = (
            "traversers/weightedshortestpath?"
            f'source="{source_id}"&target="{target_id}"&weight={weight}&max_depth={max_depth}'
        )
        response = self._sess.get(uri)
        if check_if_success(response, NotFoundError(response.content)):
            return response.json()
        return {}

    def single_source_shortest_path(self, source_id, max_depth):
        uri = f'traversers/singlesourceshortestpath?source="{source_id}"&max_depth={max_depth}'
        response = self._sess.get(uri)
        if check_if_success(response, NotFoundError(response.content)):
            return response.json()
        return {}

    def multi_node_shortest_path(
        self,
        vertices,
        direction="BOTH",
        properties=None,
        max_depth=10,
        capacity=100000000,
        with_vertex=True,
    ):
        if properties is None:
            properties = {}
        uri = "traversers/multinodeshortestpath"
        data = {
            "vertices": {"ids": vertices},
            "step": {"direction": direction, "properties": properties},
            "max_depth": max_depth,
            "capacity": capacity,
            "with_vertex": with_vertex,
        }
        response = self._sess.post(
            uri,
            data=json.dumps(data),
        )
        if check_if_success(response, NotFoundError(response.content)):
            return response.json()
        return {}

    def paths(self, source_id, target_id, max_depth):
        uri = f'traversers/paths?source="{source_id}"&target="{target_id}"&max_depth={max_depth}'
        response = self._sess.get(uri)
        if check_if_success(response, NotFoundError(response.content)):
            return response.json()
        return {}

    def customized_paths(
        self, sources, steps, sort_by="INCR", with_vertex=True, capacity=-1, limit=-1
    ):
        uri = f"traversers/customizedpaths"

        data = {
            "sources": sources,
            "steps": steps,
            "sort_by": sort_by,
            "with_vertex": with_vertex,
            "capacity": capacity,
            "limit": limit,
        }
        response = self._sess.post(
            uri,
            data=json.dumps(data),
        )
        if check_if_success(response, NotFoundError(response.content)):
            return response.json()
        return {}

    def template_paths(
        self, sources, targets, steps, capacity=10000, limit=10, with_vertex=True
    ):
        uri = f"traversers/templatepaths"
        data = {
            "sources": sources,
            "targets": targets,
            "steps": steps,
            "capacity": capacity,
            "limit": limit,
            "with_vertex": with_vertex,
        }
        response = self._sess.post(
            uri,
            data=json.dumps(data),
        )
        if check_if_success(response, NotFoundError(response.content)):
            return response.json()
        return {}

    def crosspoints(self, source_id, target_id, max_depth):
        uri = (
            f"traversers/crosspoints?"
            f'source="{source_id}"&target="{target_id}"&max_depth={max_depth}'
        )
        response = self._sess.get(uri)
        if check_if_success(response, NotFoundError(response.content)):
            return response.json()
        return {}

    def customized_crosspoints(
        self,
        sources,
        path_patterns,
        with_path=True,
        with_vertex=True,
        capacity=-1,
        limit=-1,
    ):
        uri = f"traversers/customizedcrosspoints"
        data = {
            "sources": sources,
            "path_patterns": path_patterns,
            "with_path": with_path,
            "with_vertex": with_vertex,
            "capacity": capacity,
            "limit": limit,
        }
        response = self._sess.post(
            uri,
            data=json.dumps(data),
        )
        if check_if_success(response, NotFoundError(response.content)):
            return response.json()
        return {}

    def rings(self, source_id, max_depth):
        uri = f'traversers/rings?source="{source_id}"&max_depth={max_depth}'
        response = self._sess.get(uri)
        if check_if_success(response, NotFoundError(response.content)):
            return response.json()
        return {}

    def rays(self, source_id, max_depth):
        uri = f'traversers/rays?source="{source_id}"&max_depth={max_depth}'
        response = self._sess.get(uri)
        if check_if_success(response, NotFoundError(response.content)):
            return response.json()
        return {}

    def fusiform_similarity(
        self,
        sources,
        label,
        direction,
        min_neighbors,
        alpha,
        min_similars,
        top,
        group_property,
        min_groups=2,
        max_degree=10000,
        capacity=-1,
        limit=-1,
        with_intermediary=False,
        with_vertex=True,
    ):
        uri = "traversers/fusiformsimilarity"
        data = {
            "sources": sources,
            "label": label,
            "direction": direction,
            "min_neighbors": min_neighbors,
            "alpha": alpha,
            "min_similars": min_similars,
            "top": top,
            "group_property": group_property,
            "min_groups": min_groups,
            "max_degree": max_degree,
            "capacity": capacity,
            "limit": limit,
            "with_intermediary": with_intermediary,
            "with_vertex": with_vertex,
        }
        response = self._sess.post(
            uri,
            data=json.dumps(data),
        )
        if check_if_success(response, NotFoundError(response.content)):
            return response.json()
        return {}

    def vertices(self, ids):
        uri = "traversers/vertices"
        params = {"ids": '"' + ids + '"'}
        response = self._sess.get(
            uri,
            params=params,
        )
        if check_if_success(response, NotFoundError(response.content)):
            return response.json()
        return {}

    def edges(self, ids):
        uri = "traversers/edges"
        params = {"ids": ids}
        response = self._sess.get(
            uri,
            params=params,
        )
        if check_if_success(response, NotFoundError(response.content)):
            return response.json()
        return {}

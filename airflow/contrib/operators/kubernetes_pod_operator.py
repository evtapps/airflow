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
"""Executes task in a Kubernetes POD"""
import warnings

from airflow.providers.cncf.kubernetes.operators.kubernetes_pod import KubernetesPodOperator as K8sPodOp


class KubernetesPodOperator(K8sPodOp):
    """
    This class is deprecated.
    Please use `airflow.providers.cncd.kubernetes.operators.kubernetes_pod.KubernetesPodOperator
    """

    def __init__(self, *args, **kwargs):
        warnings.warn(
            """This class is deprecated
            Please use
            `airflow.providers.cncd.kubernetes.operators.kubernetes_pod.KubernetesPodOperator.`.""",
            DeprecationWarning, stacklevel=2
        )
        super(KubernetesPodOperator, self).__init__(*args, **kwargs)

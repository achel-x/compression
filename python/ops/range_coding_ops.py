# -*- coding: utf-8 -*-
# Copyright 2018 Google LLC. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ==============================================================================
"""Range coding operations."""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

# Dependency imports

from tensorflow.python.framework import load_library
from tensorflow.python.platform import resource_loader


__all__ = list()
_ops = dict()
_range_coding_ops = load_library.load_op_library(
    resource_loader.get_path_to_datafile("../../_range_coding_ops.so"))
for name in dir(_range_coding_ops):
  if name.startswith("_"):
    continue
  if name in ("LIB_HANDLE", "OP_LIST", "deprecated_endpoints", "tf_export"):
    continue
  __all__.append(name)
  _ops[name] = getattr(_range_coding_ops, name)
globals().update(_ops)
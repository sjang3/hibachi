# Copyright 2019 Balaji Veeramani. All Rights Reserved.
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

class Selector:

    def __call__(X, y):
        raise NotImplementedError


class LasVegas(Selector):

    def __call__(X, y):
        raise NotImplementedError


class LasVegasIncremental(Selector):

    def __call__(X, y):
        raise NotImplementedError


class QBB(Selector):

    def __call__(X, y):
        raise NotImplementedError


class RELIEF(Selector):

    def __call__(X, y):
        raise NotImplementedError


class SFG(Selector):

    def __call__(X, y):
        raise NotImplementedError


class SFBG(Selector):

    def __call__(X, y):
        raise NotImplementedError


class SFFG(Selector):

    def __call__(X, y):
        raise NotImplementedError


class Genetic(Selector):

    def __call__(X, y):
        raise NotImplementedError


class Greedy(Selector):

    def __call__(X, y):
        raise NotImplementedError


class SuperGreedy(Selector):

    def __call__(X, y):
        raise NotImplementedError
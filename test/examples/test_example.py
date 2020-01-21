# Copyright 2019 PyI40AAS Contributors
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may not use this file except in compliance with
# the License. You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the License for the
# specific language governing permissions and limitations under the License.
"""
Tests for the example aas

Functions to test if an object is the same to the example aas from example_aas.py
"""
from aas.examples.data import example_aas
from test._helper.testCase_for_example_aas import *
import unittest


class ExampleAASTest(unittest.TestCase):

    def test_example_asset_identification_submodel(self):
        submodel = example_aas.create_example_asset_identification_submodel()
        assert_example_asset_identification_submodel(self, submodel)

    def test_example_bill_of_material_submodel(self):
        submodel = example_aas.create_example_bill_of_material_submodel()
        assert_example_bill_of_material_submodel(self, submodel)

    def test_example_asset(self):
        asset = example_aas.create_example_asset()
        assert_example_asset(self, asset)

    def test_example_concept_description(self):
        concept_description = example_aas.create_example_concept_description()
        assert_example_concept_description(self, concept_description)

    def test_example_concept_dictionary(self):
        concept_dictionary = example_aas.create_example_concept_dictionary()
        assert_example_concept_dictionary(self, concept_dictionary)

    def test_example_asset_administration_shell(self):
        concept_dictionary = example_aas.create_example_concept_dictionary()
        shell = example_aas.create_example_asset_administration_shell(concept_dictionary)
        assert_example_asset_administration_shell(self, shell)

    def test_example_submodel(self):
        submodel = example_aas.create_example_submodel()
        assert_example_submodel(self, submodel)

    def test_full_example(self):
        obj_store = example_aas.create_full_example()
        assert_full_example(self, obj_store)

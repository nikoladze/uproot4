# BSD 3-Clause License; see https://github.com/scikit-hep/uproot4/blob/master/LICENSE

from __future__ import absolute_import

import pytest
import skhep_testdata

import uproot4


def test_issue510b():
    with pytest.raises(NotImplementedError):
        with uproot4.open(skhep_testdata.data_path("uproot-issue510b.root"))[
            "EDepSimEvents"
        ] as t:
            t["Event"]["Trajectories.Points"].array(library="np")


def test_issue403():
    with pytest.raises(NotImplementedError):
        with uproot4.open(skhep_testdata.data_path("uproot-issue403.root"))[
            "Model"
        ] as t:
            t["Model.collimatorInfo"].array(library="np")


def test_issue475():
    with pytest.raises(NotImplementedError):
        with uproot4.open(skhep_testdata.data_path("uproot-issue475.root"))[
            "Event/Elec/ElecEvent"
        ] as t:
            t["fElecChannels"].array(library="np")

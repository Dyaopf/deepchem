"""
Gathers all splitters in one place for convenient imports
"""
from __future__ import print_function
from __future__ import division
from __future__ import unicode_literals

# TODO(rbharath): Get rid of * import
from deepchem.splits.splitters import *
from deepchem.splits.splitters import ScaffoldSplitter
from deepchem.splits.splitters import SpecifiedSplitter
from deepchem.splits.splitters import IndexSplitter
from deepchem.splits.splitters import IndiceSplitter
from deepchem.splits.task_splitter import merge_fold_datasets
from deepchem.splits.task_splitter import TaskSplitter

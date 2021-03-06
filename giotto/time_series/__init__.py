"""The module :mod:`giotto.time_series` implements transformers to
preprocess time series or embed them in a higher dimensional space for
persistent homology.
"""

from .embedding import SlidingWindow, TakensEmbedding
from .features import PermutationEntropy
from .preprocessing import Resampler, Stationarizer
from .multivariate import PearsonCorrelation
from .target import Labeller

__all__ = [
    'Resampler',
    'Stationarizer',
    'PermutationEntropy',
    'TakensEmbedding',
    'SlidingWindow',
    'Labeller',
    'PearsonCorrelation'
]

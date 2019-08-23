"""Constants."""

import os
from enum import Enum, auto


DEFAULT_WORKING_DIR = '/tmp/autodist'
DEFAULT_SERIALIZATION_DIR = os.path.join(DEFAULT_WORKING_DIR, 'strategies')
DEFAULT_PORT_RANGE = iter(range(15000, 16000))


class Env(Enum):
    """AutoDist Environment Variables."""

    AUTODIST_WORKER = auto()
    AUTODIST_STRATEGY_ID = auto()


MAX_INT64 = int(2 ** 63 - 1)
COLOCATION_PREFIX = 'loc:@'
BINARY_ENCODED_COLOCATION_PREFIX = b"loc:@"
UPDATE_OP_VAR_POS = 0
SPARSE_AVERAGE_BY_COUNTER = 1
SPARSE_NO_AVERAGE = 3


class InitOps(Enum):
    """
    List of all AutoDist-defined ops for "initialization".

    Note that the initialization here does not refer to the variable initialization in TensorFlow,
    but the "initialization" before distributed computing for AutoDist.
    """

    MIRROR_VARIABLE_INIT_OP = 'mirror_variable_init_op'

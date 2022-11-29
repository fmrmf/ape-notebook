import pytest

from ape_notebook.kernel import ApeKernel


@pytest.fixture
def kernel():
    return ApeKernel()

# TESTS — delete this block when done ────────────────────────────────────────
# Tests are required to publish this package. The publish pipeline runs your
# tests as a quality gate — a package will not be published if tests fail or
# do not meet the minimum requirements.
#
# Requirements checked before publishing:
#   - At least one test per node
#   - All tests must pass
#   - Output fields must be meaningfully asserted — not just type-checked
#
# The generated test below is a starting point. Replace the TODO comment with
# real assertions that verify your node returns correct data for known inputs.
# Think: given a specific input, what should the output fields contain?
#
# Run your tests locally at any time:
#   axiom test
from gen.messages_pb2 import MultiplyInput, MathOutput
from nodes.multiply import multiply


class _NoOpLogger:
    """Minimal AxiomLogger implementation for unit tests."""
    def debug(self, msg: str, **attrs) -> None: pass
    def info(self, msg: str, **attrs) -> None: pass
    def warn(self, msg: str, **attrs) -> None: pass
    def error(self, msg: str, **attrs) -> None: pass


class _NoOpSecrets:
    """Minimal AxiomSecrets implementation for unit tests.
    Override get() to return specific values for secrets your node requires.
    """
    def get(self, name: str, default: str = "") -> str:
        return default


def test_multiply():
    log = _NoOpLogger()
    secrets = _NoOpSecrets()
    input_msg = MultiplyInput(a=5.0, b=3.0)
    result = multiply(log, secrets, input_msg)
    assert isinstance(result, MathOutput)
    assert result.result == 15.0
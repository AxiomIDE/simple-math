from gen.messages_pb2 import AddInput, MathOutput
from gen.axiom_logger import AxiomLogger, AxiomSecrets


def add(log: AxiomLogger, secrets: AxiomSecrets, input: AddInput) -> MathOutput:
    """Adds two numbers together and returns the sum."""
    try:
        log.info(f"Adding {input.a} + {input.b}")
        result = input.a + input.b
        log.info(f"Result: {result}")
        return MathOutput(result=result)
    except Exception as e:
        log.error(f"Error adding numbers: {e}")
        return MathOutput(result=0.0)
from gen.messages_pb2 import MultiplyInput, MathOutput
from gen.axiom_logger import AxiomLogger, AxiomSecrets


def multiply(log: AxiomLogger, secrets: AxiomSecrets, input: MultiplyInput) -> MathOutput:
    """Multiplies two numbers together and returns the product."""
    try:
        log.info(f"Multiplying {input.a} and {input.b}")
        result = input.a * input.b
        log.info(f"Result: {result}")
        return MathOutput(result=result)
    except Exception as e:
        log.error(f"Error during multiplication: {str(e)}")
        raise
from gen.messages_pb2 import SubtractInput, MathOutput
from gen.axiom_logger import AxiomLogger, AxiomSecrets


def subtract(log: AxiomLogger, secrets: AxiomSecrets, input: SubtractInput) -> MathOutput:
    """Subtracts the second number from the first and returns the difference."""
    try:
        log.info(f"Subtracting {input.b} from {input.a}")
        result = input.a - input.b
        log.info(f"Subtraction result: {result}")
        return MathOutput(result=result)
    except Exception as e:
        log.error(f"Error during subtraction: {str(e)}")
        raise
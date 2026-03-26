from gen.messages_pb2 import DivideInput, MathOutput
from gen.axiom_logger import AxiomLogger, AxiomSecrets


def divide(log: AxiomLogger, secrets: AxiomSecrets, input: DivideInput) -> MathOutput:
    """Divides the first number by the second and returns the quotient."""
    try:
        log.info(f"Dividing {input.a} by {input.b}")
        
        if input.b == 0:
            log.error("Division by zero attempted")
            raise ValueError("Cannot divide by zero")
        
        result = input.a / input.b
        log.info(f"Division result: {result}")
        
        return MathOutput(result=result)
    
    except Exception as e:
        log.error(f"Error during division: {str(e)}")
        raise
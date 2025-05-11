from src.core.inquiry_engine import build_inquiry_engine
from src.core.reasoning_tracker import ReasoningTracker
from src.core.erotetic_equilibrium_evaluator import compute_eee_score

def preguntar_con_deliberacion(subpregunta: str):
    engine = build_inquiry_engine()
    tracker = ReasoningTracker()
    tracker.add_step("Pregunta enviada", subpregunta)
    result = engine({"question": subpregunta, "chat_history": []})
    respuesta = result["answer"]
    tracker.add_step("Respuesta recibida", respuesta)
    return respuesta, tracker.steps, compute_eee_score(tracker.steps)

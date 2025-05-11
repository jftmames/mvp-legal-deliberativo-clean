from src.engine.subquestion_generator import generar_subpreguntas
from src.engine.consultor_deliberativo import preguntar_con_deliberacion

def ejecutar_deliberacion(pregunta: str, n_subpreguntas: int = 3):
    subqs = generar_subpreguntas(pregunta, n_subpreguntas)
    resultados = []
    for sub in subqs:
        resp, hist, eee = preguntar_con_deliberacion(sub)
        resultados.append({"subpregunta": sub, "respuesta": resp, "trace": hist, "eee": eee})
    return {"respuesta_central": resultados[0]["respuesta"] if resultados else "", "resultados": resultados}

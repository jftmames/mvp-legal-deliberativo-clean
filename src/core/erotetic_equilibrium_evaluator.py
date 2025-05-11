def compute_eee_score(steps):
    depth = len(steps)
    if depth == 0:
        return {"depth": 0, "plurality": 0, "traceability": 0.0}
    plurality = len({s["detail"] for s in steps})
    traceability = sum(1 for s in steps if s["detail"]) / depth
    return {"depth": depth, "plurality": plurality, "traceability": traceability}

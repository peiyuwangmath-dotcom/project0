from .demo_responses import DEMO_RESPONSES


def call_model(query: str, model_index: int) -> str:
    """单个模型的调用入口，目前直接取固定值。
    """
    return DEMO_RESPONSES[model_index]


def evaluate_query(query: str) -> list[dict[str, str]]:
    """组织各模型的回答"""
    results = []
    for model_index in range(len(DEMO_RESPONSES)):
        answer = call_model(query, model_index)
        results.append({
            "model_id": f"demo-{model_index + 1:02d}",
            "model_name": f"模型占位 {model_index + 1:02d}",
            "answer": answer,
        })
    return results

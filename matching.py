from rapidfuzz import fuzz
from intents import INTENTS
from config import CONFIDENCE_THRESHOLD
from normalizer import normalize


def match_intent(user_input: str) -> tuple[str | None, int]:
    """
    Match user input against known intents and return:
    (best_answer, confidence_score)
    """
    normalized_input = _normalize_text(user_input)
    best_match = _find_best_intent_match(normalized_input, INTENTS)

    return _build_response(best_match, CONFIDENCE_THRESHOLD)


def _normalize_text(text: str) -> str:
    """Normalize input text using shared normalizer."""
    return normalize(text)


def _find_best_intent_match(
    normalized_input: str,
    intents: dict
) -> dict:
    """
    Iterate through all intents and find the best match.
    Returns a dict with score and answer.
    """
    best_match_score = 0
    best_match_answer = None

    for intent_name, intent_data in intents.items():
        match = _evaluate_intent_patterns(normalized_input, intent_data)

        if match["score"] > best_match_score:
            best_match_score = match["score"]
            best_match_answer = match["answer"]

    return {
        "score": best_match_score,
        "answer": best_match_answer,
    }


def _evaluate_intent_patterns(
    normalized_input: str,
    intent_data: dict
) -> dict:
    """
    Evaluate all patterns for a single intent and return the best match.
    """
    best_score_for_intent = 0
    intent_answer = intent_data["answer"]

    for pattern in intent_data["patterns"]:
        normalized_pattern = _normalize_text(pattern)
        score = _calculate_similarity(normalized_input, normalized_pattern)

        if score > best_score_for_intent:
            best_score_for_intent = score

    return {
        "score": best_score_for_intent,
        "answer": intent_answer,
    }


def _calculate_similarity(input_text: str, pattern_text: str) -> int:
    """Calculate similarity score between two strings."""
    return fuzz.partial_ratio(input_text, pattern_text)


def _build_response(best_match: dict, threshold: int) -> tuple[str | None, int]:
    """
    Return final response based on confidence threshold.
    """
    if best_match["score"] >= threshold:
        return best_match["answer"], best_match["score"]

    return None, best_match["score"]
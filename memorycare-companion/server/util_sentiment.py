# Lightweight, dependency-free sentiment heuristic for demo.
NEG_WORDS = set("""sad lonely tired upset angry afraid anxious confused hopeless pain hurt worried bored frustrated guilty useless overwhelmed""".split())
POS_WORDS = set("""happy calm loved grateful excited proud relaxed hopeful cheerful strong brave joyful energetic confident comfort""".split())

def polarity(text: str) -> str:
    text = (text or "").lower()
    n_neg = sum(w in NEG_WORDS for w in text.split())
    n_pos = sum(w in POS_WORDS for w in text.split())
    if n_neg > n_pos + 1:
        return "negative"
    if n_pos > n_neg + 1:
        return "positive"
    return "neutral"

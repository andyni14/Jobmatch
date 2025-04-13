def compute_match(resume, jd):
    resume_words = set(resume.lower().split())
    jd_words = set(jd.lower().split())
    matched = resume_words & jd_words
    score = round(len(matched) / len(jd_words) * 100, 2) if jd_words else 0
    return score, list(matched)

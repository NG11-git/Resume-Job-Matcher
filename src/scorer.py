from sklearn.metrics.pairwise import cosine_similarity

import numpy as np

def compute_similarity(resume_emb, jd_emb):
    return cosine_similarity(
        [resume_emb],
        [jd_emb]
    )[0][0]
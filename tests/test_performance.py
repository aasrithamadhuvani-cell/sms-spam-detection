import time
from sklearn.pipeline import make_pipeline
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB

def test_text_pipeline_smoke_latency():
    texts=["free prize claim now","see you at college","win cash reward","meeting at five"]
    labels=[1,0,1,0]
    model=make_pipeline(TfidfVectorizer(),MultinomialNB())
    model.fit(texts,labels)
    start=time.perf_counter()
    pred=model.predict(["free cash reward"])
    elapsed=time.perf_counter()-start
    assert pred[0] in [0,1]
    assert elapsed < 5

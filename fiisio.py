# -*- coding: utf-8 -*-
from library import normal
from library import segmentation
from library import tagger
from library import sentiment 
from library import bm25
from library import frequence
from library import merger
from library import model
from library import segger
from library import textrank
from library import tnt
from library import trie
                
class Fiisio(object):

    def __init__(self, doc):
        self.doc = doc
        self.bm25 = bm25.BM25(doc)

    @property
    def words(self):
        return segger.seg(self.doc)

    @property
    def sentences(self):
        return normal.get_sentences(self.doc)

    @property
    def sentiment(self):
        return sentiment.classify(self.doc)

    @property
    def tags(self):
        words = self.words
        tags = tagger.tag(words)
        return zip(words, tags)

    @property
    def tf(self):
        return self.bm25.f

    @property
    def idf(self):
        return self.bm25.idf

    def sim(self, doc):
        return self.bm25.simall(doc) 

    def keywords(self, limit=5, merge=False):
        doc = []
        sents = self.sentences
        for sent in sents:
            words = seg.seg(sent)
            words = normal.filter_stop(words)
            doc.append(words)
        rank = textrank.KeywordTextRank(doc)
        rank.solve()
        ret = []
        for w in rank.top_index(limit):
            ret.append(w)
        if merge:
            wm = words_merge.SimpleMerge(self.doc, ret)
            return wm.merge()
        return ret
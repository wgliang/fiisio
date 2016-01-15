# -*- coding: utf-8 -*-

# ------------------------------------------------------------
# 标签学习库

# import tagger

# tagger.train("resource/wparts.txt")

# tagger.save("resource/tag.marshal")

# ------------------------------------------------------------

# ------------------------------------------------------------
# 分词学习库

# import seg_init

# seg_init.train("resource/data.txt")

# seg_init.save("resource/seg.marshal")

# ------------------------------------------------------------

# ----------------------------------------------------------
# 情感分析测试

import sentiment

# sentiment.train("resource/data.txt")
# sentiment.save("resource/seg.marshal")

s = sentiment.classify(u" 奇酷太棒了。")
print s

# ------------------------------------------------------------
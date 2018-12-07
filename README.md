# 中文信息处理实验

哈工大中文信息处理课的课程大作业

## Lab 1 : 中文自动分词

实现了正向最大匹配、逆向最大匹配和双向最大匹配三种匹配算法，使用的测试数据来源于[这里](http://sighan.cs.uchicago.edu/bakeoff2005/)。

* build_dict.py

基于已分词的文本构建词典，来源于[这里](https://github.com/HIT-SCIR/scir-training-day/tree/master/2-python-practice/3-max-matching-word-segmentation)。

使用方法：`python build_dict.py <segmented file> <output file>`

* max_match.py

使用最大匹配算法根据给定的词典进行分词，包括了正向最大匹配、逆向最大匹配和双向最大匹配。

使用方法：`python max_match.py [-forward | -backward | -bi_direction] <file to segment> <dictionary file> <output file>`

* eval.py

对照给定的标准分词结果检查分词的准确率。

使用方法：`python eval.py <output file> <gold file>`
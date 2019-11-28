- [Bioinformatic homework](#bioinformatic-homework)
  - [1. Explain BAM FLAG value： 143](#1-explain-bam-flag-value-143)
  - [2. Explain BAM FLAG value： 99](#2-explain-bam-flag-value-99)
  - [3. Explain BAM FLAG value：516](#3-explain-bam-flag-value516)
  - [4. Explain BAM FLAG value： 2064](#4-explain-bam-flag-value-2064)
  - [5. Explain BAM FLAG value： 147](#5-explain-bam-flag-value-147)
  - [6. Explain BAM CIGAR：14M2D31M](#6-explain-bam-cigar14m2d31m)
  - [7. Explain BAM CIGAR：3S6M1D5M](#7-explain-bam-cigar3s6m1d5m)
  - [8. Explain BAM CIGAR: 6M14N5M](#8-explain-bam-cigar-6m14n5m)
  - [9. Explain BAM CIGAR: 7M5D8M2I14M (小写：7m5d8m2i14m）](#9-explain-bam-cigar-7m5d8m2i14m-%e5%b0%8f%e5%86%997m5d8m2i14m)
  - [10. how long is the read with alignment CIGAR of 7M5D8M2I14M?](#10-how-long-is-the-read-with-alignment-cigar-of-7m5d8m2i14m)
# Bioinformatic homework
## 1. Explain BAM FLAG value： 143
Answer:
- template having multiple segments in sequencing
- each segment properly aligned according to the aligner
- segment unmapped
- next segment in the template unmapped
- the last segment in the template

## 2. Explain BAM FLAG value： 99
Answer:
- template having multiple segments in sequencing
- each segment properly aligned according to the aligner
- SEQ of the next segment in the template being reversed
- the first segment in the template
  
## 3. Explain BAM FLAG value：516
Answer:
- segment unmapped
- not passing quality controls

## 4. Explain BAM FLAG value： 2064
Answer:
- SEQ being reverse complemented
- supplementary alignment

## 5. Explain BAM FLAG value： 147
Answer:
- template having multiple segments in sequencing
- each segment properly aligned according to the aligner
- SEQ being reverse complemented
- the last segment in the template

## 6. Explain BAM CIGAR：14M2D31M
14个match，2个缺失（查询序列没有但参考序列有），31个match(match可能是正确匹配的，也可能是错配)

## 7. Explain BAM CIGAR：3S6M1D5M
开始的3个字符不考率，6个match，1个缺失，5个match

## 8. Explain BAM CIGAR: 6M14N5M
6个match，14个插入（查询序列有但是参考序列没有），5个match的

## 9. Explain BAM CIGAR: 7M5D8M2I14M  (小写：7m5d8m2i14m）
7个match，5个缺失，8个match，2个插入，14个match

## 10. how long is the read with alignment CIGAR of 7M5D8M2I14M?
7+8+2+14=31bp
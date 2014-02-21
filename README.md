Video
=====

Video ranker

First part of the code attaches tag to every video based on the text. tags are output in myfile after the code is run.

The second part of the code is used to do cosine ranking using all possible features. Based on the features , the top 3 videos are ranked. The format of the output is [video_rank1, video_rank2, video_rank3, this video id]. The iteration of the list is from 0 to 473 to account for all the 474 videos. 

# Document Similarity Algorithms Experiment

Document similarity comparison using 5 popular algorithms: Jaccard, TF-IDF, Doc2vec, USE, and BERT.

33,914 New York Times articles are used for the experiment. It aims to show which algorithm yields the best result out of the box in 2020.

# Purpose

1. By running multiple algorithms with some of which are most up-to-date and trendy in NLP community, it will show which algorithms give the best results and by how much onto the same set of data.
2. By using full-length popular media publications as our data input, we will simulate the real world similarity/recommendation use case.
3. By following URLs, you can actually see and compare the quality document similarity yourself.
4. By using only the pretrained models available publicly, you can easily set it up and start implementing document similarity on your own with very little prior knowledge while expecting the similar result output.

# Data Setup

33,914 New York Times articles from 2018 to June 2020 were selected. The data was mostly collected from their RSS feed.

5 articles were chosen as the basis. They represent different categories.

1. [How My Worst Date Ever Became My Best](https://www.nytimes.com/2020/02/14/style/modern-love-worst-date-of-my-life-became-best.html) (lifestyle)
2. [A Deep-Sea Magma Monster Gets a Body Scan](https://www.nytimes.com/2019/12/03/science/axial-volcano-mapping.html) (science)
3. [Renault and Nissan Try a New Way After Years When Carlos Ghosn Ruled](https://www.nytimes.com/2019/11/29/business/renault-nissan-mitsubishi-alliance.html) (business)
4. [Dominic Thiem Beats Rafael Nadal in Australian Open Quarterfinal](https://www.nytimes.com/2020/01/29/sports/tennis/thiem-nadal-australian-open.html) (sports)
5. [2020 Democrats Seek Voters in an Unusual Spot: Fox News](https://www.nytimes.com/2019/04/17/us/politics/fox-news-democrats-2020.html) (politics)

# Comparison Criteria

Overlapping tags, sections, subsections, writing format, and subjective judgement are considered. For a more detailed description, please follow this blog post.

# Algorithm That Win Overall

TF-IDF. It resulted in the best matches in 2.5 out of 5 comparisons.

The detailed breakdowns of how each algorithm predicted can be found in the algorithm folders.

# Winner Algorithm By Each Article

## How My Worst Date Ever Became My Best

Winner: BERT

|Title|Tag Overlap|Section Overlap|Subsection Overlap|Style Overlap|Theme|Subjective|
|---|---|---|---|---|---|---|
| [Why Are All the Exes Texting?](https://www.nytimes.com/2020/05/29/style/modern-love-coronavirus-why-are-all-the-exes-texting.html) | 1 | Y | Y | Y | Dating | Related |
| [When Love Seems Too Easy to Trust](https://www.nytimes.com/2018/04/13/style/when-love-seems-too-easy-to-trust.html) | 1 | Y | Y | Y | Dating | Related |
| [He Saved His Last Lesson for Me](https://www.nytimes.com/2020/03/06/style/modern-love-long-distance-dating-korea.html) | 1 | Y | Y | Y | Dating | Related |

## A Deep-Sea Magma Monster Gets a Body Scan

Winner: TF-IDF

|Title|Tag Overlap|Section Overlap|Subsection Overlap|Style Overlap|Theme|Subjective|
|---|---|---|---|---|---|---|
| [A 3D Encounter With a Violent Volcano’s Underbelly](https://www.nytimes.com/2019/12/18/science/volcano-3d-reunion-island.html) | 4 | Y | N | Y | 3D Mapped Volcano | Highly Related |
| [Pressure, and Mystery, on the Rise](https://www.nytimes.com/2015/01/06/science/predicting-what-a-volcano-may-or-may-not-do-is-as-tricky-as-it-is-crucial-as-iceland-well-knows.html) | 1 | Y | Y | Y | Iceland's Volcano | Related |
| [It’s Not Just Hawaii: The U.S. Has 169 Volcanoes That Could Erupt](https://www.nytimes.com/2018/05/14/us/us-active-volcanoes-hawaii.html) | 2 | N | N | Y | Volcanos | Related |


## Renault and Nissan Try a New Way After Years When Carlos Ghosn Ruled

Winner: TF-IDF

|Title|Tag Overlap|Section Overlap|Subsection Overlap|Style Overlap|Theme|Subjective|
|---|---|---|---|---|---|---|
| [Nissan CEO Says 'No Merit' in Merger With Renault-Nikkei](https://www.nytimes.com/reuters/2018/04/25/business/25reuters-renault-nissan-m-a.html) | 3 | N | N | Y | Nissan and Renault | Related |
| [Carlos Ghosn and the Roots of Nissan’s Decline](https://www.nytimes.com/2020/01/15/automobiles/nissan-carlos-ghosn-strategy.html) | 3 | N | N | N | Carlos Ghosn | Related |
| [Renault Chooses Volkswagen Executive as New C.E.O.](https://www.nytimes.com/2020/01/28/business/renault-ceo-luca-de-meo.html) | 5 | Y | Y | Y | Renault CEO | Very Related |

## Dominic Thiem Beats Rafael Nadal in Australian Open Quarterfinal

Winner: Jaccard, TF-IDF, and USE

(Jaccard)

|Title|Tag Overlap|Section Overlap|Subsection Overlap|Style Overlap|Theme|Subjective|
|---|---|---|---|---|---|---|
| [Djokovic vs. Federer, a Rivalry for the Ages, Is One-Sided This Time](https://www.nytimes.com/2020/01/30/sports/tennis/djokovic-federer-australian-open.html) | 3 | Y | Y | Y | Australian Open | Related |
| [Novak Djokovic Wins the Australian Open](https://www.nytimes.com/2020/02/02/sports/tennis/australian-open-djokovic-thiem.html) | 4 | Y | Y | Y | Dominic vs Novak in Australian Open | Very Related |
| [With Rome Title, Nadal Back on Track Entering French Open](https://www.nytimes.com/aponline/2018/05/20/sports/tennis/ap-ten-italian-open.html) | 1 | N | N | Y | French Open | Unrelated |

## 2020 Democrats Seek Voters in an Unusual Spot: Fox News

Winner: USE

|Title|Tag Overlap|Section Overlap|Subsection Overlap|Style Overlap|Theme|Subjective|
|---|---|---|---|---|---|---|
| [Bernie Sanders Had a Problem With MSNBC. Then Came Super Tuesday.](https://www.nytimes.com/2020/03/05/business/media/msnbc-bernie-sanders-media.html) | 7 | N | N | Y | Sanders and MSNBC | Very Related |
| [Democrats, Don’t Abandon Fox News](https://www.nytimes.com/2019/03/08/opinion/fox-news-democrats-debate.html) | 7 | N | N | N | Democrats and Fox News | Very Related |
| [Candidates Running Against, and With, Cable News](https://www.nytimes.com/2010/10/24/us/politics/24cable.html) | 4 | Y | Y | Y | Fox, MSNBC and politics  | Related |

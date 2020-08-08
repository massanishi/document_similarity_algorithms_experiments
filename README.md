Document similarity comparison using 5 popular algorithms: Jaccard, TF-IDF, Doc2vec, USE, and BERT.

33,914 New York Times articles are used for the experiment.

# Purpose

1. By running multiple algorithms with some of which are most up-to-date and trendy in NLP community, it will show which algorithms give the best results and by how much onto the same set of data.
2. By using full-length popular media publications as our data input, we will simulate the real world similarity/recommendation use case.
3. By following URLs, you can actually see and compare the quality document similarity yourself.
4. By using only the pretrained models available publicly, you can easily set it up and start implementing document similarity on your own with very little prior knowledge while expecting the similar result output.

# Data Setup

33,914 New York Times articles from 2018 to June 2020 were selected. The data was mostly collected from their RSS feed. Article lengths are fairly similar with an average of .

From them, 5 articles were chosen as the basis. They represent different categories.

1. How My Worst Date Ever Became My Best (lifestyle)
2. A Deep-Sea Magma Monster Gets a Body Scan (science)
3. Renault and Nissan Try a New Way After Years When Carlos Ghosn Ruled (business)
4. Dominic Thiem Beats Rafael Nadal in Australian Open Quarterfinal (sports)
5. 2020 Democrats Seek Voters in an Unusual Spot: Fox News (politics)

# Comparison Criteria

Articles' tags, sections, subsections, writing format, and subjective judgement is considered.

# Winner Algorithm

TF-IDF

# Winner Algorithm for Each Article Comparison

## How My Worst Date Ever Became My Best

Winner: USE and BERT

(USE)

|Title|Tag Overlap|Section Overlap|Subsection Overlap|Style Overlap|Theme|Subjective|
|---|---|---|---|---|---|---|
| My Quarantine Boyfriend Lost Everything (but Found Me) | 1 | Y | Y | Y | Dating | Related |
| Flying Close to Temptation | 0 | Y | Y | Y | LGBTQ | Related |
| Why Are All the Exes Texting? | 1 | Y | Y | Y | Dating | Related |

## A Deep-Sea Magma Monster Gets a Body Scan

Winner: TF-IDF

|Title|Tag Overlap|Section Overlap|Subsection Overlap|Style Overlap|Theme|Subjective|
|---|---|---|---|---|---|---|
| A 3D Encounter With a Violent Volcano’s Underbelly | 4 | Y | N | Y | 3D Mapped Volcano | Highly Related |
| Pressure, and Mystery, on the Rise | 1 | Y | Y | Y | Iceland's Volcano | Related |
| It’s Not Just Hawaii: The U.S. Has 169 Volcanoes That Could Erupt | 2 | N | N | Y | Volcanos | Related |


## Renault and Nissan Try a New Way After Years When Carlos Ghosn Ruled

Winner: TF-IDF

|Title|Tag Overlap|Section Overlap|Subsection Overlap|Style Overlap|Theme|Subjective|
|---|---|---|---|---|---|---|
| Nissan CEO Says 'No Merit' in Merger With Renault-Nikkei | 3 | N | N | Y | Nissan and Renault | Related |
| Carlos Ghosn and the Roots of Nissan’s Decline | 3 | N | N | N | Cardlos Ghosn | Related |
| Renault Chooses Volkswagen Executive as New C.E.O. | 5 | Y | Y | Y | Renault CEO | Very Related |

## Dominic Thiem Beats Rafael Nadal in Australian Open Quarterfinal

Winner: Jaccard, TF-IDF, and USE

(Jaccard)

|Title|Tag Overlap|Section Overlap|Subsection Overlap|Style Overlap|Theme|Subjective|
|---|---|---|---|---|---|---|
| Djokovic vs. Federer, a Rivalry for the Ages, Is One-Sided This Time | 3 | Y | Y | Y | Australian Open | Related |
| Novak Djokovic Wins the Australian Open | 4 | Y | Y | Y | Dominic vs Novak in Australian Open | Very Related |
| With Rome Title, Nadal Back on Track Entering French Open | 1 | N | N | Y | French Open | Unrelated |

## 2020 Democrats Seek Voters in an Unusual Spot: Fox News

Winner: USE

|Title|Tag Overlap|Section Overlap|Subsection Overlap|Style Overlap|Theme|Subjective|
|---|---|---|---|---|---|---|
| Bernie Sanders Had a Problem With MSNBC. Then Came Super Tuesday. | 7 | N | N | Y | Sanders and MSNBC | Very Related |
| Democrats, Don’t Abandon Fox News | 7 | N | N | N | Democrats and Fox News | Very Related |
| Candidates Running Against, and With, Cable News | 4 | Y | Y | Y | Fox, MSNBC and politics  | Related |

# Note

Detailed breakdown of each article is found in the algorithm folder.

For a more detailed description, please follow this blog post.
Please see [Final Project Report.pdf](https://github.com/Jeffreyhung/UPitts_InformationVisualization/blob/master/Final%20Project%20Report.pdf)  for report with figure


Part 1 – Data Description

<span id="anchor"></span>Dataset 1

1.  Name: Thyroid Disease Dataset – Hypothyroid Data
2.  Source: UCI Machine Learning Repository
    [*https://archive.ics.uci.edu/ml/datasets/Thyroid+Disease*](https://archive.ics.uci.edu/ml/datasets/Thyroid+Disease)
3.  Number of Instance: 3163
4.  Description: Thyroid Disease Dataset that focused on hypothyroid disease that includes some information of the person and several different thyroid related measure result.
5.  Missing Value: 0
6.  Number of Attribute: 25
7.  Attribute Information:

<!-- -->

1.  -   1.  Disease:Hypothyroid / Negative
        2.  Age:Continuous
        3.  Sex:Male, Female, unknow
        4.  On thyroxine: T/F
        5.  Query on thyroxine:T/F
        6.  On antithyroid medication: T/F
        7.  Thyroid surgery: T/F
        8.  Query hypothyroid:T/F
        9.  Query hyperthyroid:T/F
        10. Pregnant T/F
        11. Sick: T/F
        12. Tumor: T/F
        13. Lithium: T/F
        14. Goiter: T/F
        15. TSH measured:T/F
        16. TSH: Continuous
        17. T3 measured:T/F
        18. T3: Continuous
        19. TT4 measured:T/F
        20. TT4: Continuous
        21. T4U measured:T/F
        22. T4U: Continuous
        23. FTI measured:T/F
        24. FTI: Continuous
        25. TBG measured:T/F
        26. TBG: Continuous

<!-- -->

1.  Dataset Preview

Dataset 2

1.  Name: Fertility Dataset– Fertility Diagnosis
2.  Source: UCI Machine Learning Repository
    [*https://archive.ics.uci.edu/ml/datasets/Fertility*](https://archive.ics.uci.edu/ml/datasets/Fertility)
3.  Number of Instance: 100

1.  Description: 100 volunteers provide a semen sample analyzed according to the WHO 2010 criteria. Sperm concentration are related to socio-demographic data, environmental factors, health status, and life habits
2.  Missing Value: 0
3.  Number of Attribute: 10
4.  Attribute Information:

<!-- -->

1.  Season in which the analysis was performed.
    Winter: -1, Spring: -0.33, Summer: 0.33, Fall: 1
2.  Age at the time of analysis.
    Between 18-36 years old: 1, others: 0
3.  Childish diseases (i.e. chicken pox, measles, mumps, polio): No: 0, Yes: 1
4.  Accident or serious trauma: No: 0, Yes: 1
5.  Surgical intervention: No: 0, Yes: 1
6.  High fevers in the last year
    Never: 1, More than three months ago: 0, Less than three months ago: -1
7.  Frequency of alcohol consumption: 1) several times a day, 2) every day, 3) several times a week, 4) once a week, 5) hardly ever or never (0, 1)
8.  Smoking habit: Never: -1, Occasional: 0, Daily: 1
9.  Number of hours spent sitting per day: Continuous, 0~1
10. Output: Diagnosis: Normal: N, Altered: O

<!-- -->

1.  Dataset Preview

Part 2 – Visualizations

Dataset 1

Figure 1-1: Percentage of people that is diagnosed as normal and Hypothyroid.

Figure 1-2: Percentage of different sex of all the ones having hypothyroid.

Figure 1-3: Bar chart showing the age distribution. 0 means normal and 1 means hypothyroid. X-axis are the age in years.

Figure 1-4: Bar chart showing the percentage of different condition and percentage of normal and hypothyroid.

Figure 1-5: Bar chart showing the percentage of having each measure.

Dataset 2

Figure 2-1: Percentage of people that is diagnosed as normal and altered.

Figure 2-2: Bar chart showing the distribution of age, 0 means normal and 1 means abnormal. X-axis present the age in years

Figure 2-3: Bar chart showing the distribution of sitting hours, 0 means
normal and 1 means abnormal. X-axis present sitting hours

Figure 2-4: Pie charts showing the percentage of the season the sperm is collected

Figure 2-5: Bar chart showing the percentage of different condition and percentage of normal and altered.

Figure 2-6: The scatter plot presents the relation between fever, alcohol and the condition of the semen.

Part 3 – Observations

Dataset 1

Figure 1-1

Percentage of people that is diagnosed as normal and Hypothyroid. Blue means normal and red means hypothyroid. We can see that most people do not have hypothyroid, and the percentage of people having is about 5 percent.

Figure 1-2

Percentage of sex of all the ones having hypothyroid. Blue means men and red means women. From this figure, we can see that more than 3/4 of people having hypothyroid are female, because of that, we can assume that there might be some reason leading to female having higher rate than male to have hypothyroid.

Figure 1-3

Bar chart showing the age distribution. 0 means normal and 1 means hypo-thyroid. X-axis are the age in years. From a broader view, the distribution of the normal people is similar to the Gaussian distribution, which have less data is both high and low end and have more data in the middle. On the other hand, the distribution of hypothyroid is more distributed, there are no significant special points that have more counts than other.

Figure 1-4

Bar chart showing the percentage of different condition and percentage of normal and hypothyroid. The x-axis shows different conditions, which are: On Thyroxine, Query on Thyroxine, On Anti-Thyroid, Query Hypothyroid, Query Hyperthyroid, Pregnant, Sick, Tumor, Lithium and Goiter. The y-axis presents the percentage of people under each condition. The blue charts represent normal data and the red chart represent Hypothyroid data.

From this figure, we can briefly tell the relation between the percentage of normal and abnormal under each condition. By observing this figure, I found out that there isn’t a condition that has great effect on having hypothyroid or not due to the reason of the difference between the percentage of them are not too significant. The only two factors that may be considered are “On Thyroxine” and “Query Hyperthyroid”. For the factor “On Thyroxine”, the percentage of normal is almost twice as the percentage of abnormal, therefore, we can guess that people that are on thyroxine are more likely to not have hypothyroid. For the factor “Query Hyperthyroid”, the percentage of having hyperthyroid is about 1.5 times of the percentage of normal, we can make a guess that people who have hyperthyroid are more likely to query hyperthyroid than people who don’t have hyperthyroid.

Figure 1-5

Bar chart showing the percentage of having each measure. In this bar chart I found out that the percentage of normal and abnormal in each test measure are really close. For my assumption, this might mean that these measures are required for knowing if a person have hypothyroid or not, which is necessary measure in this dataset. As for the TBG measure, which is extremely less compare to other measures, I guess it may be a measure that is not common is thyroid related test, causing that both normal and abnormal have a low percentage of this measure.

Dataset 2

Figure 2-1

Percentage of people that is diagnosed as normal and altered.

Blue means normal and red means altered.

From this figure, we can tell that only 12% of people are have abnormal sperm, most of the people are having normal sperm.

Figure 2-2

Bar chart showing the distribution of age, 0 means normal and 1 means abnormal. X -axis present the age in years. In this I found out that in this dataset, there are more younger people than older people. Surprisingly, the number of men at age 28 is the highest and none of them have altered sperm. However, from an overall view, there seems to be no pattern of normal or altered sperm when comparing them with age.** **

Figure 2-3

Bar chart showing the distribution of sitting hours, 0 means normal and 1 means abnormal. X-axis present sitting hours. From the chart, we can see most people are having sitting hours around three to nine hours a day. Similar to the figure 1-3, the distribution of abnormal is pretty distributed, there are no significant special points that have more counts than other. It is also hard to find a pattern of normal or altered sperm when comparing them with sitting hours.

Figure 2-4

Pie chart showing the percentage of the season the sperm is collected. From the figure, we can say that Spring, Fall and Winter each present almost one third of the total data and Summer almost have not data. I guess that this might related to how these sperm are collected, for example, the sperm collection progress may start in fall and continued for a year, and most people who are willing to participate attends the progress early.

Figure 2-5

Bar chart showing the percentage of different condition and percentage of normal and altered. The x-axis shows different conditions, which are: Disease, Trauma and Surgical. The y-axis presents the percentage of people under each condition of each group. The blue charts represent normal data and the red chart represent altered data.

From this figure, we can see the relation between each factor and the percentage of having normal or abnormal sperm. By observing this bar chart, I assume that these factors don’t have great effect in the normality of a men’s sperm, the reason of that is because under each condition, the percentage of normal and abnormal are similar. Take disease as example, both normal and abnormal have high percentage of having disease, therefore we assume that disease don’t have effect in the normality of a men’s sperm.

Figure 2-6

The scatter plot presents the relation between fever, alcohol and the condition of the semen. The x-axis present if the person has fever recently. 0 means not having fever in the last year, 1 means having fever more than three months age and 2 means having fever less than three months ago. The y-axis presents the frequency of having alcohol, 0 means hardly ever or never have alcohol, the larger the number is the more frequent the person have alcohol, the largest number 4 means having alcohol several times a day. Color blue represent the normal one and red represent altered one. The larger the scatter plot is indicated higher number of people.

By observing this scatter plot, we can found out that people who have fever more than three months ago are having the highest rate of have abnormal sperm, but we cannot see any relation between the frequency of having alcohol, we can only see that people, including normal and abnormal, tends not to drink alcohol, the number of people decreased as the frequency of drinking alcohol raised. As for the percentage of people having fever, we can see that most people have fever more than three months age, and only have a few people have fever in the past three months. I guess that the main reason of not able to find any significant relation on this dataset is mainly because the number of dataset is too small, which is only a hundred data in this dataset, if we are able to gain more data and have it visualized, be might be able to find some more significant relations among each factors.

Part 4 – Appendix

For this project, I complete all the program in Python, the following part is the code that I used to produce these visualized charts.

Dataset 1

In first step of this part, I first process the raw data and organize it into an easier format for further visualization

After this, the data attribute will become like this:

Next, we will start to visualize the data

Dataset 2

In first step of this part, I first process the raw data and organize it into an easier format for further visualization

After this, the data attribute will become like this:

Next, we will start to visualize the data

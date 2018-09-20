## Introduction

  I did my summer internship in EPRA (Engineering, Procurement, Research, and Analysis). My internship started on 13 August and ended on 14 September. EPRA; provides engineering services in electric power generation, transmission, distribution and trading sectors. Their works mostly depending on research and development. The first day, the company gave me information about their projects. Since I have experienced in object-oriented programming languages like R and Python, we decided to work on TUBITAK project which uses data analytics and machine learning tools for finding illegal activities in electricity and water consumption.  My work divided into three parts:
* Using data mining techniques to utilize KCETAS and KASKI data. 
* Since bill dates are not uniform, normalizing the data
* Clustering the resulting data
* Optimize the algorithm as much as possible so even the data go into the system increases the speed of the algorithm should increase less or constant.

## Main Area of Business
* EPRA; provides engineering services in electric power generation, transmission, distribution and trading sectors. 
* EPRA uses the state of the art software simulation tools developed by the world leaders in the power systems consulting and computer analysis.
* EPRA is the exclusive official representative of the leading international electrical engineering and consulting firm DIgSILENT GmbH​ in Turkey. ​
* EPRA developing [projects](https://www.epra.com.tr/projects) which funding TUBITAK, KOSGEB and Distribution Companies like KCETAS, Başkent Electric or Toroslar Electric. 

## A Brief History Of company
EPRA, who has been active in electricity sector since 2011, provides planning, analysis, technical support, consultancy and training services in the fields of electricity generation transmission, distribution and trade. EPRA, who has a wide range of analysis abilities from very short term electro-magnetic transient analysis to long term market simulations, provides high level engineering services to multiple foreign and domestic customers. 

## Organization Structure of company

## Summer Practice Report
####  Abbreviations
* KCETAS, Kayseri Electric Distribution Company (Kayseri ve Civarı Elektrik Türk A.Ş)
* KASKI, Kayseri Water and Sewerage Management (Kayseri Su ve Kanalizasyon İdaresi)

### Plan 
|     Time      |                                            To do                                            |
|:-------------:|:-------------------------------------------------------------------------------------------:|
|   First week  | Reading past documentation  about last code, understanding  dataset, working on data-mining |
|  Second week  |                       Finding common adresses and mapping their values                      |
|   Third week  |                   Normalizing the time series starting documenting the code                 |
|  Final week   |                            Correlation analysis and  Data Analytics                         |

### First week
After choosing my project, the company gave me the last version of the code they worked on. The code was written in Python (ver3.x). There are 2 bulky datasets which in Excel xlsx format. The datasets contain three  neighborhoods in Kayseri namely,
* Kılıçaslan
* Demokrasi
* İldem Cumhuriyet

  However, there were some serious problems with the datasets. The first one is since all addresses typed by humans, there is mismatch between datasets. Since we used addresses as an index for correlating water and electricity consumption, the same addresses should be matched. Since data is too large, formatting should be done by code, not human-hand. (Both datasets has over 300.000 row.)
Before digging into the code, there are data types and formats which I used and transformed a lot during the internship. Therefore I write Python library that transforms these types and formats. 

<div><img src ="https://github.com/nailtosun/data_formatter/blob/master/venn_diagram.png" class="center"/></div>

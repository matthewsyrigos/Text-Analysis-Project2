# Text-Analysis-Project
 
**1. Project Overview** 

For this assignment, I used wikipedia's API in order to extract information about colleges. I wanted to make the project more realistic and tailored to my needs, which is why I allowed the user to enter the college they want to research. I then analysed the data in different ways. I initially presented the different sections to the users and let them choose which category they wanted to explore. Then using the Markov method and text generator, as well as a function I created, I summarized the text for the user to get an idea about their chosen section.Then, I created two formating functions that would turn the text into easy-to-read bullet points. This was something I, as a dyslexic person, would really use to help me comprehend text better. This project helped me expirement, learn, and create something cool using APIs. I have found it very fun and usefull.

**2. Implementation** 

My code starts by connecting to the wikipedia API and prompting a response from the user that is going to determine which wikipedia page the program is going to explore. After entering the page it analyses the categories and ask for the user to select which one to analyse. The text is then analysed. This process is repeated as many times are the user desires.

While analysing the text, I made the design decision of using multple smaller functions to solve small parts of the problem. This can be apparent by all different functions that call other functions to summarise, create bulletpoints, etc. To analyse the text I used different methods, such as the Morkov, text generator, formating with bullet points, and summarizing. I also analysed different data structures, including lists, dictionaries, and tuples to sort, format and get my desired outputs. In this effort I used the help of chat gtp and google to learn and remember code. Three insances where chat gtp was particularly helpful was in understanding how Morkov works, learning how to turn text in a bullet point format, and remembering how to print information from an API with an index.

(Couldn't add the screenshot here so they are separate files in this repository)

**3. Results** 

My program is able to succesfuly read the user's requests and present the data of their choosen college and sections in a comprehenadble way. Users can choose a college and decide on one or more sections from the one's offered at wikipedia.com for this college, and get information about the relative subject. The information is presented as follows: There is a short summary of the data giving the readers a basic idea of what they are about to read. Then the rest of the information is orginised in bullet points, with enough space in between to not overwhelm people who have trouble reading (such as myself).

It was very interesting to see how this program presents the data and offers an on-point summary most of the times. For example where I was looking at the Atheltics of Boston College, the summary said "Boston College teams are non-ACC/NCAA". This could potentially be something users might be conserned about and it can be answered in the first line of the program. It was also very interesting to see how formating can be utilised in a smart way such as breaking the bulletpoint every time the sentence is over and adusting spacing.

**4. Reflection** 

From my point of view, in this project I succeded analysing the data in the way that I initially wanted. If I had to improve it, I would add more text analysis functions to provide more information to the users. I believe my testing plan was successful since it guided me to my errors and helped me complete the project.

This project, although time consuming and quite challenging at times, was very useful and rewarding to do. I managed to complete all the analysis I had in mind and more successfully and learn alot about how to handle API in an interactive program. I faced quite some barriers and had to pivot a few times. An example is I wanted to look up the sections by name which didn't seem to work in this API so I had to pivot to indices. In general, I learned new functions and applications of APIs and text processing. ChatGPT had a very positive impact in my learning, as well as helping me stay on track and undestand my mistakes in a few instances where I was completely stuck. I wish I had familiarised myself with how well chatGPT explains new coding concept, since I found it to be very helpful. This is something I will definately use going forward.
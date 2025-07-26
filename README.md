# bias_navigation 
Bias Aware Navigation

Step 1: Get trending topics

Step 2: Get URLs

Step 3: Call Readability APIs on the URLs to get the clean text

Step 4: Extract keywords from given document using rake algorithm

a) Get the words from the document by parsing using space and punctuations as delimiters

b) get the candidate keywords by removing stopwords etc

c) calculate the scores for the candidate keywords

d) get the top 3 scores to get the keywords

Step 5: Calculate the bias score

Step 6: Make the UI for Chrome

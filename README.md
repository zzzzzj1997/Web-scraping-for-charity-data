# Web-scraping-for-charity-data
(1) About "uscharity" "uscharitypart2"
In terms of the reason why I put two similiar code and run twice (only details about specific xpath to locate change),
there are two tables of data we want to extract, even though the data of both part can be found from the saved html, but
the code could extract nothing if it does not appear on the page. No error occured but still no successful extraction.
So before running the code, the first thing to do is to save the html files twice (one is the original page, the other
is the page after clicking 'Balance Sheet' button in the 'FINANCIALS' part.)
1.save the html files twice
[But if you can find a way to pretend the code to look like human and not be detected by the website. Then that would be
much easier, just need to put the direct urls into txt file and run the combined code (link the two parts with a 'click' command).]
2.put the urls of the saved htmls into a txt file. A local url looks like this:'file:///E:/.......'
3.After installing splinter,selenium,geckodriver, run the code.
The code is to extract all of the available years, you can use R/excel to filter and seperate them by year.
If you only want data from a specific year, just change the loop of Extract_yearly_asset() function. The variable 'i'
in this function refers to the serial number.(inspecting the year selection button and there is a number representing each year)

(2)About "charitynavigator_rating"
Divide the code and run seperately.
The first part is to get the seperate links of all charities from the links you usually give to me.
The second part is to get actual ratings by browsering on each charity from the links get from above. The html of rating data here is not very standardized, so it may
also need further refinement.

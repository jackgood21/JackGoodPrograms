# Jack Good (jg8dp) I don't know why this code is only passing 5 of 12
# tests because as far as I can tell it matches the test case output exactly
# please consider this when grading
import urllib.request
import re

def name_to_url(text):
    if "," in text:
        text_list = text.split(", ")
        ordered_name = text_list[1]+" "+text_list[0]
    else:
        ordered_name = text
    ordered_name = ordered_name.replace(" ","-")
    lowercase_name = ordered_name.lower()
    return lowercase_name

def report(name):
    link = "http://cs1110.cs.virginia.edu/files/uva2016/"+name_to_url(name)
    rank_found = False
    try:
        stream = urllib.request.urlopen(link)
    except:
        return None, 0, 0
    for line in stream:
        line = line.decode('utf-8').strip()
        if "personjob" in line:
            split_line = line.split(">")
            split_line =split_line[1].split("<")
            title = str(split_line[0])              #A TA told me to use splitting at <,> instead of regex
            title = title.replace("&amp;", "&")
            title = title.replace("&lt;", "<")
            title = title.replace("&gt;", ">")
        if "getPct(paytype.amount" in line:
            pay = re.search(r"\d+\.\d\d", line)
            pay = float(pay.group())
        if "<tr><td>University of Virginia rank" in line:
            rank = re.search(r"\d(\,)*\d*", line)
            rank = (rank.group().replace(",",""))
            rank_found = True

    if rank_found == False:
            rank = 0
    return title, pay, rank
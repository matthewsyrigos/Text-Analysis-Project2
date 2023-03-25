
from mediawiki import MediaWiki
import pprint

wikipedia = MediaWiki()
college_name = input("Please enter the full-name of the college:")
college = wikipedia.page(college_name)

#Looking up for the college's data
def college_lookup():
    """
    This function is used to print the sections with their indices of the college's wikipedia page
    """
    print("We found information on:",college.title)
    print("The page contains the following sections:")
    #Help by chat gpt to print the indexes before each section:
    for index, section in enumerate(college.sections):
        print(f"{index}: {section}")
    #pprint.pprint(college.sections)
    #print(college.content)

#Morkov Text Analysis
    """This function analiyses text using the Morkov technique"""
def generate_frequency_table(text, order):
    words = text.split()
    frequency_table = {}

    for i in range(len(words) - order):
        key = tuple(words[i:i+order])
        next_word = words[i+order]
        if key in frequency_table:
            frequency_table[key].append(next_word)
        else:
            frequency_table[key] = [next_word]

    return frequency_table

def generate_markov_text(frequency_table, seed, length):
    """This function generates text using markov """
    current_key = seed
    result = list(current_key)
    import random
    for _ in range(length):
        if current_key in frequency_table:
            next_word = random.choice(frequency_table[current_key])
            result.append(next_word)
            current_key = tuple(result[-len(current_key):])
        else:
            break

    return ' '.join(result)

#Analysing the section
def section_analysis(section_index):
    """
    This function receives a section of a wikipedia page
    the user is interested in and creates bullet points 
    to simplify the reading and comprehensions process.
    """
    if 0 <= section_index < len(college.sections):
        section_title = college.sections[section_index]
        section_content = college.section(section_title)
    else:
        return "Section index out of range"
    
    lines = section_content.split("\n")
    #bullets = []

    #Used help from chat gpt on how to create a bullet list and format the text
    
    #Unused Code from previous Attempt:
    # for line in lines:
    #     if line.strip():
    #         words = line.strip().split()
    #         formatted_line = ""
    #         current_line = []
    #         word_count = 0
    #         for word in words:
    #             if word_count + len(word) <= 50:
    #                 current_line.append(word)
    #                 word_count += len(word) + 1  
    #             else:
    #                 formatted_line += "→ " + " ".join(current_line) + "\n"
    #                 current_line = [word]
    #                 word_count = len(word) + 1
    #         if current_line:
    #             formatted_line += "→ " + " ".join(current_line) + "\n"
    #         bullets.append(formatted_line)

    bullet_list = format_bullet_list(section_content)

    summary = summarize_section(section_content)
    summary_bullet_list = format_bullet_list(summary)
    #sentiment = sentiment_analysis(bullet_list)

    print("Here is a summary of the content:", summary_bullet_list)
    
    return bullet_list

#Creating a summary
def summarize_section(section_content):
    """This function receives the selection from 
    the selection_analysis function and produces a summary"""
    order = 2
    length = 50

    words = section_content.split()
    if len(words) > 2:
        seed = tuple(words[:order])
    else:
        return section_content

    frequency_table = generate_frequency_table(section_content, order)
    summary = generate_markov_text(frequency_table, seed, length)
    return summary

#Bullet point format
def format_bullet_list(text):
    """With the help of chat gpt, I created this function
    to help me format the text into bullet points."""
    import re
    sentences = re.split('(?<!\w\.\w.)(?<![A-Z][a-z]\.)(?<=\.|\?)\s', text)
    bullets = []

    for sentence in sentences:
        if sentence.strip():
            bullets.append("→ " + sentence.strip())

    bullet_list = "\n\n".join(bullets)
    return bullet_list

#Didn't end up using the sentiment analysis function because my mac was giving me issues while downloading the software
#I also realised sentiment analysis doesn't make too much sense in the case I have decided to develop
# def sentiment_analysis(sentence):
#     """
#     this functions performs a sentiment analysis of a given sentence
#     """
#     from nltk.sentiment.vader import SentimentIntensityAnalyzer 
#     score = SentimentIntensityAnalyzer().polarity_scores(sentence)
#     print(score)

def calling_section_analysis():
    """This function promts inputs from the user and calls the 
    section analysis function. It also prints the results."""
    answer = 'yes'
    while answer == 'yes':
        indexsec = int(input("Pick a section you want to analyse. Enter its index:"))
        print(section_analysis(indexsec))
        answer = input('Do you want to analyse another section (yes/no):')

#if main:
def main():
    college_lookup()
    calling_section_analysis()
    
if __name__ == '__main__':
    main()
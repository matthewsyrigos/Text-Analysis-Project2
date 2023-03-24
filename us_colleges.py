
from mediawiki import MediaWiki
import pprint

wikipedia = MediaWiki()
college_name = input("Please enter the full-name of the college:")
college = wikipedia.page(college_name)

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

    sentiment = sentiment_analysis(bullet_list)

    return bullet_list, sentiment


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

def sentiment_analysis(sentence):
    """
    this functions performs a sentiment analysis of a given sentence
    """
    from nltk.sentiment.vader import SentimentIntensityAnalyzer 
    score = SentimentIntensityAnalyzer().polarity_scores(sentence)
    print(score)

def calling_section_analysis():
    """This function promts inputs from the user and calls the 
    section analysis function. It also prints the results."""
    answer = 'yes'
    while answer == 'yes':
        indexsec = int(input("Pick a section you want to analyse. Enter its index:"))
        print(section_analysis(indexsec))
        answer = input('Do you want to analyse another section (yes/no):')

def main():
    college_lookup()
    calling_section_analysis()
    
if __name__ == '__main__':
    main()
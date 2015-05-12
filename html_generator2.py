def generate_concept_HTML(lesson, concept_title):
    html_text_1 = '''
    <div class="lesson">
       <div class="concept-title">
           ''' + concept_title
    html_text_2 = '''
       </div>
       <div class="concept-description">
           ''' + concept_description
    html_text_3 = '''
       </div>
    </div>'''

    full_html_text = html_text_1 + html_text_2 + html_text_3
    return full_html_text

def lesson(concept):
    start_location = concept.find('LESSON:')
    end_location = concept.find('TITLE:')
    lesson = concept[start_location+7 : end_location-1]
    return lesson

def get_title(concept):
    start_location = concept.find('TILE:')
    title = concept[start_location+8 :]
    return title

def get_description(list_of_concepts)
for concepts in list_of_concepts:
    concepts_HTML = make_HTML(concept)
    return HTML

def make_HTML(concept):
    concept_lesson = concept[0]
    concept_title = concept[1]
    return generate_concept_HTML(concept_lesson, concept_title)


text = '''LESSON=Stage 1 - Lesson 1: The Basics of the Web:
TITLE:How the Web Works,
LESSON: Stage 1 - Lesson 2: Creating a Structured Document with HTML
TITLE: Tags and Elements,  Developer Tools (in the Browser),
LESSON: How do functions help programmers avoid repetition?
TITLE:Why computers are Stupid,
LESSON:Stage 1 - Lesson 3: Adding CSS Style to HTML Structure
TITLE: Avoiding Repetition
LESSON: Stage 2 - Lesson 1:  Introduction to "Serious" Programming
TITLE: Programming and Computers, Getting Started with Python, Programming Languages
'''

list_of_concepts = ['The Web is a system of interlinked, hypertext documents accessed through the Internet.']
['It enables the retreival and display of text and media to your computer.']
['The web is based on different technologies that make it possible for users tolocate and share information through the Internet.']
['These include Web browsers, hypertext Markup (HTTP).']
['To access webpages, you must use a Web browser usually referred to as a browser.']
['Web browsers provide the software interface that enables you to use your mouse to click hyperlinked resources on the World Wide Web']
['The Web is a system of interlinked, hypertext documents accessed through the Internet. It enables the retreival and display of text and media to your computer.']
['The web is based on different technologies that make it possible for users to locate and share information through the Internet.']
['These include Web browsers, hypertext Markup Language (HTML) and Hypertext transfer Protocol HTTP).']
['To access webpages, you must use a Web browser usually referred to as a browser.']
['Web browsers provide the software interface that enables you to use your mouse to click hyperlinked resources on the World Wide Web']
['A text editor is a program that helps you type text similar to document editors, such as Microsoft word or Corel WordPerfect, but without all the extra formatting functions that document editors editor like Notepad, TextEdit, etc.']
['As long as your file names end in .html your browser will know to read them as HTML.']
['But these text editors are meant for writing documents for other people to read.']
['They are notdesigned for writing computer code.']
['Trying to use one of these text editors will be almost impossible.']
['A computer is a universal machine; we can program it to do essentially any computation.']
['So anything that we can imagine, anything that we can figure out how to write a program for we can make the computer do; and what the program needs to be is a very precise sequence of steps.']
['The computer by itself does not know how to do anything, it has a few simple instructions that it can execute; and to make a program do something useful we need to put those instructions together in a way that does what we want.']
['There are many reasons why a designed language like Python is better for writing programs than a natural language like English.']
['One problem with natural languages is that they are ambiguous.']
['Hence, not everyone will interpret the same phrase the same way.']
['To program computers, it is important that we know exactly what our programs mean, and that the computer will run them with the meaning we intended.']
['Another problem with natural language is that they are very verbose.']
['To say something with the level of precision needed for a computer to be able to follow it mechanically would require an awful lot of writing.']
['We want our programs to be short so it is less work to write them, and so that it is easier to read and understand them.']
['If we want we can double quotes instead.']
['If we use double quotes then the double with a double quote it has to end with a double quote.']
['And that is actually a handy property because that means we can have the other kind of with a double quote, it contains a single quote inside it but because we started with a double quote that single quote doesn’t end the string, that single quote is just like another character in the string.']
['The string continues until the closing double quote.']
['We’ll give the first occurrence where the target string appears in the search string but starting from whatever position we pass in as a number.'
['If we pass in 0 it would start from the beginning that would mean the same thing as the original find, if we pass in the position later down the line, it would start from there and would still output the same value we found before – if we start right after that then it wouldn’t find the occurrence because this occurrence starts after that position, it would go to the next target.']
['When working with example code, you do have to exercise with some care or you could inherit bugs from the sample code.']
['Sometimes the example work didn’t work to begin with so in that case your code ould have never of worked.']


print get_description (list_of_concepts)

print generate_all_html(text)

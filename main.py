def read_file_content(story):
    # [assignment] Add your code here 
    with open('C:./Reading-Text-Files\story.txt') as f:
     contents = f.read()
    print(contents)
 
def count_words():
        text = read_file_content("./story.txt")
    # [assignment] Add your code here
        text.count()
print ()

  



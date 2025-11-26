print("This is a Madlibs Generator. You are free to choose a story of your genre to play this.")

print("\nGenres available:")
print("1. Adventure")
print("2. Mystery")
print("3. Romance")
print("4. Horror")
print("5. Comedy")
print("6. Action")
    
while True:
    choice=input("Please enter your choice (1-6): ")
    if choice.isdigit():
        choice=int(choice)
        if 1<= choice <=6:
            break
        else:
            print("Please enter a number between 1 and 6.")
    else:
        print("Invalid input! Try again!")
        
f=open(f"C:\\Users\\karan\\OneDrive\\Desktop\\Python Projects\\Story\\Story{choice}.txt.txt",'r')
story=f.read()
f.close()

genre=['Adventure','Mystery','Romance','Horror',"Comedy","Action"]    
print('You have selected the genre: ',genre[choice-1])
     
words=set()
start_of_word=-1
target_start='<'
target_end='>'

for i, char in enumerate(story):
     if char==target_start:
         start_of_word=i
     if char==target_end and start_of_word!=-1:
         word=story[start_of_word:i+1]
         words.add(word)
         start_of_word=-1
         
answers={}
print()
for word in words:
     value=input("Enter a word for "+word+ ": ")
     answers[word]=value
     
for word in words:
     story=story.replace(word,answers[word])
     
print("Your story with your inputted words:\n")
print(story)


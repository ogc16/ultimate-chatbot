#pip install specific version of embedchain package-opensource framework
#e.g pip install embedchain==0.0.10 on the shell
from embedchain import App
import os

chat_bot = App()
#create a folder named "docs"
# list files
filelist = os.listdir("docs")

for file in filelist:#scanning the folder
  keys=db.keys()
  if file not in keys:#allows us to add new files to the database by caching
   print("Loading file: ", file")
   chat_bot.add("pdf_file", f"docs/{file}")
   db[file]=None

  else:
    print("File already loaded: ", file)


while True:
  #allow the user to ask questions
  query = input("Ask a question: ")
  answer = chat_bot.query(query)
  #return answer
  print(answer)



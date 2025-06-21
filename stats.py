def get_book_text(path_to_file):
   with open(path_to_file) as f:
      file_contents = f.read()

   
   return file_contents


def text_n_words(text):
   text2 = text.split()
   amount_words = len(text2)
   return text2, amount_words



def sort_on(item):
   return item["num"]


def count_letters(text):
   text2 = text.lower()
   
   dictt = []
   characters = []
   k = 0
   
   for i in text2:
      if i.isalpha():
         if i not in characters:
            characters.append(i)
            dictt.append({"char":i, "num":1})
            
         else:
            for j in dictt:
               if j["char"] == i:
                  j["num"] += 1


         dictt.sort(reverse = True, key = sort_on)

   for el in dictt:
      print(f'{el["char"]}: {el["num"]}')
      

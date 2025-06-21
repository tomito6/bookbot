from stats import get_book_text, text_n_words, count_letters
import sys

def main():
   args = sys.argv
   if len(args) <2:
      print("Usage: python3 main.py <path_to_book>")
      sys.exit(1)
   else:
      path_to_file = args[1]
      text = get_book_text(path_to_file)
      text2, amount_words = text_n_words(text)


      print("============ BOOKBOT ============\n" \
      "Analyzing book found at books/frankenstein.txt...\n" \
      "----------- Word Count ----------\n")
      print(f"Found {amount_words} total words\n" \
            "--------- Character Count -------")

      count_letters(text)
   
main()
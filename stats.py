def num_words (book_text):
    split_words = book_text.split()
    return len(split_words)

def letter_count (book_text):
    lower_words = book_text.lower()
    lower_words_dic = {}
    for i in lower_words:
        if i.isalpha():
            if i in lower_words_dic:
                lower_words_dic [i] += 1
            else:
                lower_words_dic[i] =1
    return lower_words_dic

def sort_list (lower_words_dic):
    words_list = []
    for character, count in lower_words_dic.items():
        words_list.append({"character": character, "count": count})
    words_list.sort(reverse=True, key=sort_on)
    return words_list

def sort_on(dic_item):
    return dic_item["count"]






__author__ = 'josephbosire'
def load_data_set():
    with open("answers.out", "wb") as answer_file:
        with open("B-large-practice.in", "rb") as input_file:
            number_of_sentences = input_file.readline()
            sentences = input_file.readlines()
            count = 1
            for sentence in sentences:
              words = sentence.strip("\n").split(" ")
              print words
              print words[::-1]
              answer_file.write("Case #{}: {}\n".format(count, ' '.join(words[::-1])))
              count += 1


print load_data_set()
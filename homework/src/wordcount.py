# obtain a list of files in the input directory
import os


def read_all_lines():

    lines = []
    input_directory_files = os.listdir("data/input/")
    for filename in input_directory_files:
        with open("data/input/" + filename, "r", encoding="utf-8") as f:
            lines.extend(f.readlines())
    return lines


def save_word_frequencies(counter):
    if not os.path.exists("data/output"):
        os.makedirs("data/output")

    # save the results using tsv format
    with open("data/output/results.tsv", "w", encoding="utf-8") as f:
        for key, value in counter.items():
            # write the key and value to the file
            f.write(f"{key}\t{value}\n")


def main():
    input_directory_files = os.listdir("data/input/")

    # count the frequency of the words in the files in the input directory
    counter = {}
    lines = read_all_lines()

    for line in lines:
        for w in line.split():
            w = w.lower().strip(",.!?")
            counter[w] = counter.get(w, 0) + 1

    save_word_frequencies(counter)


if __name__ == "__main__":
    main()

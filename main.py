import json

alphabet = "abcdefghijklmnopqrstuvwxyz"

src_filename = "words-graph.txt"

with open(src_filename, "r") as file:
    adjancency_list = json.load(file)

words = list(adjancency_list.keys())

def backtrace(parent, start, end):
    path = [end]
    while path[-1] != start:
        path.append(parent[path[-1]])
    path.reverse()
    return path
        

def bfs(adj_list, start, end):
    parent = {}
    queue = []
    queue.append(start)
    while queue:
        node = queue.pop(0)
        if node == end:
            return backtrace(parent, start, end)
        for adjacent in adj_list[node]:
            if adjacent not in parent.keys() :
                parent[adjacent] = node # <<<<< record its parent 
                queue.append(adjacent)

def main():
    """
    Make the program interactive so that you don't need to run it every time you want to find a path.
    """
    while True:
        user_input = input("Enter the source word and the destination word with a space in between : ")
        print("\n")
        try:
            src_word, dst_word = user_input.split()
        except ValueError:
            print("Please, enter 2 words.")
            continue
        if not (src_word.isalpha() and dst_word.isalpha()):
            print("Please enter 2 words, without special characters")
            continue
        if src_word == dst_word:
            print("Please enter 2 different words.")
            continue
        if len(src_word) != len(dst_word):
            print("The 2 words must be of the same length.")
            continue
        if src_word not in adjancency_list.keys():
            print(f"{src_word} is not in the list of words.")
            continue
        if dst_word not in adjancency_list.keys():
            print(f"{dst_word} is not in the list of words.")
            continue
        print("Starting to look for a match (if the program is taking too long, there may be no solution, press Ctrl+C.")
        result = bfs(adjancency_list, src_word, dst_word)
        if result:
            print("A path has been found (it may not be the only one) :")
            print(*result, sep=" -> ")
        else:
            print("No match was found...")
        print("\n\n")

if __name__ == "__main__":
    main()
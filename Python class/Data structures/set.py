# set is a collection of unordered (output order can change with multiple executions and
# this makes set execute faster than lists), indexed and unique items.

# syntax 1
my_set = set("Mississippi")  # splits the element into unique entities
print(my_set)

# another syntax is to use {}
name = {"johnny"}  # treats it as single unique item
print(name)

fruits = {"banana", "apple", "strawberry", "grape", "apple"}
print(fruits)

vegetables = {"brocoli", "spinach", "tomato", "cabbage"}

# add() add a new item to the set
fruits.add("pineapple")
print(fruits)

# remove() removes an item from the set
fruits.remove("grape")
print(fruits)

# update() adds one set to another
fruits.update(my_set)
print(fruits)

edible = vegetables.union(fruits)
print(edible)

story = "the quick brown fox jumps over the lazy dog"
set_story = set(story)
print(set_story)

# the split() string method can be used to reveal the words
reveal_word = story.split()
print(reveal_word)

# the unique words can be extracted using set
unique_words = set(reveal_word)
print(unique_words)

# difference() checks te differences between sets
# intersection() check the items that 2 sets have in common

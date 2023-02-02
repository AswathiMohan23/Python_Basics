dictionary = {
  "name": "Tom",
  "id": 78,
  "year": 2023
}
print(dictionary)
r=78
k="id"
if k in dictionary.keys():
    print("yes")
    print(dictionary.get(k))
for name, age in dictionary.items():  # for name, age in dictionary.iteritems():  (for Python 2.x)
    if age == r:
        print(name)
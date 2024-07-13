#union()
web_dev_languages = {"Python", "JavaScript", "C++", "Java"}
mobile_dev_languages = {"Ruby", "Python", "Swift", "JavaScript"}

all_languages = web_dev_languages.union(mobile_dev_languages)
print("Union:", all_languages)

#intersection()
web_dev_languages = {"Python", "JavaScript", "C++", "Java"}
mobile_dev_languages = {"Ruby", "Python", "Swift", "JavaScript"}

common_languages = web_dev_languages.intersection(mobile_dev_languages)
print("Intersection:", common_languages)

#symmetric_difference()
web_dev_languages = {"Python", "JavaScript", "C++", "Java"}
mobile_dev_languages = {"Ruby", "Python", "Swift", "JavaScript"}

unique_languages = web_dev_languages.symmetric_difference(mobile_dev_languages)
print("Symmetric Difference:", unique_languages)

#difference
web_dev_languages = {"Python", "JavaScript", "C++", "Java"}
mobile_dev_languages = {"Ruby", "Python", "Swift", "JavaScript"}

web_only_languages = web_dev_languages.difference(mobile_dev_languages)
mobile_only_languages = mobile_dev_languages.difference(web_dev_languages)
print("Difference-1:", web_only_languages)
print("Difference-2:", mobile_only_languages)
s = "Мой дядя самых честных правил, \
Когда не в шутку занемог, \
Он уважать себя заставил \
И лучше выдумать не мог"

s_new = " ".join(list(filter(lambda x: x[0].lower() != "м", s.split())))
print(s_new)

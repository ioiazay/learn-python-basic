class Spam:
    _telur = 1  # weak private
    __eggs = 2  # Strong private

    def print_telur(self):
        print(self._telur * 10)

    def print_eggs(self):
        print(self.__eggs * 10)


spam = Spam()
spam.print_telur()
spam.print_eggs()

print(spam._telur)
print(spam._Spam__eggs)

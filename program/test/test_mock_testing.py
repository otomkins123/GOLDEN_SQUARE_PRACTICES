from unittest.mock import Mock
import pytest # type: ignore

#### Mock logic under test - tests skipped ####

class Diary:
    # Public properties:
    #   entries: a list of instances of DiaryEntry
    def __init__(self):
        pass
    def add(self, entry):
        # entry is an instance of DiaryEntry
        pass
    def count_words(self):
        # Returns the number of words in all entries
        pass

class DiaryEntry:
    # Public properties:
    #   title: string
    #   contents: string
    def __init__(self, title, contents):
        # title, contents are both strings
        pass
    def count_words(self):
        # Returns the number of words in the contents
        pass

@pytest.mark.skip()
def test_diary_counts_words_in_all_entries_with_fakes():
    diary = Diary()
    diary.add(FakeTwoWordDiaryEntry())
    diary.add(FakeThreeWordDiaryEntry())
    assert diary.count_words() == 5

class FakeTwoWordDiaryEntry:
    def count_words(self):
        return 2

class FakeThreeWordDiaryEntry:
    def count_words(self):
        return 3

@pytest.mark.skip()
def test_diary_counts_words_in_all_entries_with_mocks():
    diary = Diary()

    fake_two_word_diary_entry = Mock()
    fake_two_word_diary_entry.count_words.return_value = 2

    fake_three_word_diary_entry = Mock()
    fake_three_word_diary_entry.count_words.return_value = 3

    diary.add(fake_two_word_diary_entry)
    diary.add(fake_three_word_diary_entry)

    assert diary.count_words() == 5

from unittest import TestCase
from viet_text_tools import normalize_diacritics
from viet_text_tools import vietnamese_sort_key


class NormalizeDiacriticsTestCase(TestCase):
    def test(self):
        assert normalize_diacritics('hoạ') == 'họa'
        assert normalize_diacritics('choàng') == 'choàng'
        assert normalize_diacritics('thuỷ') == 'thủy'
        assert normalize_diacritics('oà') == 'òa'
        assert normalize_diacritics('toà') == 'tòa'
        assert normalize_diacritics('toàn') == 'toàn'
        assert normalize_diacritics('tòan') == 'toàn'

    def test_new_style(self):
        assert normalize_diacritics('ngòăng', new_style=True) == 'ngoằng'
        assert normalize_diacritics('họa', new_style=True) == 'hoạ'
        assert normalize_diacritics('chòang', new_style=True) == 'choàng'
        assert normalize_diacritics('giừơng', new_style=True) == 'giường'
        assert normalize_diacritics('baỷ', new_style=True) == 'bảy'
        assert normalize_diacritics('cuả', new_style=True) == 'của'
        assert normalize_diacritics('òa', new_style=True) == 'oà'
        assert normalize_diacritics('toàn', new_style=True) == 'toàn'

    def test_decomposed(self):
        word = 'thuỷ'
        expected = 'thủy'
        assert len(word) == 4
        assert len(expected) == 5
        assert normalize_diacritics(word, decomposed=True) == expected


class SortingTestCase(TestCase):
    def test(self):
        words = ['anh', 'ba', 'áo', 'cắt', 'cá', 'cả']
        assert sorted(words) == ['anh', 'ba', 'cá', 'cả', 'cắt', 'áo']
        assert sorted(words, key=vietnamese_sort_key) == ['anh', 'áo', 'ba', 'cả', 'cá', 'cắt']

    def test_curly_quote(self):
        words = ['\u201canh\u201d', 'anh', 'ba', 'áo', 'cắt', 'cá', 'cả']
        assert sorted(words, key=vietnamese_sort_key) == ['anh', 'áo', 'ba', 'cả', 'cá', 'cắt', '\u201canh\u201d']

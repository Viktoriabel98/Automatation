import pytest
from string_utils import StringUtils

utils = StringUtils()

def test_capitalize():
    #Pozitive
    assert utils.capitilize("live") == "Live"
    assert utils.capitilize("one love") == "One love"
    assert utils.capitilize("1998") == "1998"
    # Negative
    assert utils.capitilize("") == ""
    assert utils.capitilize(" ") == " "
    assert utils.capitilize("1998тестирую") == "1998тестирую"

def  test_trim():
    #Pozitive
    assert utils.trim("  live") == "live"
    assert utils.trim("  one love  ") == "one love  "
    assert utils.trim(" 1998 ") == "1998 "
    #Negative
    assert utils.trim("") == ""

@pytest.mark.parametrize('string, delimeter, result', [
    #Pozitive
    ("шкаф,стол,кровать", ",", ["шкаф", "стол", "кровать"]),
    ("1,2,3,4,5", ",", ["1", "2", "3", "4", "5"]),
    ("%@:@?", "@", ["%", ":", "?"]),
    # Negative
    ("", None, []),
    ("6,7,8 9", None, ["6", "7", "8 9"]),
])

def test_to_list(string, delimeter, result):
    if delimeter is None:
        res = utils.to_list(string)
    else:
        res = utils.to_list(string, delimeter)
        assert res == result

@pytest.mark.parametrize('string, symbol, result', [
    ("шкаф", "ш", True),
    ("стол", "л", True),
    ("кровать", "ь", True),
    ("1998", "9", True),
    ("Севастополь", "и", False),
    ("город", "а", False)
])    

def test_contains(string, symbol, result):
    res = utils.contains(string, symbol)
    assert res == result

@pytest.mark.parametrize('string, symbol, result', [
    ("шкаф", "ш", "каф"),
    ("море", "о", "мре"),
    #Negative
    ("кровать", "и", "кровать"),
    ("", "", ""),
    ("компьютер", "", "компьютер"),
    ("озеро", " ", "озеро")
])

def tes_delete_symbol(string, symbol, result):
    res = utils.delete_symbol(string, symbol)
    assert res == result

@pytest.mark.parametrize('string, symbol, result', [
    ("шкаф", "ш", True),
    ("море", "м", True),
    ("1998", "1", True),
    #Negative
    ("кровать", "р", False),
    ("", "^", False),
    ("компьютер", "т", False),
])

def test_starts_with(string, symbol, result):
    res = utils.starts_with(string, symbol)
    assert result == result

@pytest.mark.parametrize('string, symbol, result', [
    ("шкаф", "ф", True),
    ("море", "е", True),
    ("1998", "8", True),
    #Negative
    ("кровать", "р", False),
    ("", "^", False),
    ("компьютер", "т", False),
    ("программа", "А", False)
])   

def test_end_with(string, symbol, result):
    res = utils.end_with(string, symbol)
    assert result == result

@pytest.mark.parametrize('string, result', [
    ("", True),
    (" ", True),
    ("  ", True),
    #Negative
    ("кровать", False),
    ("новый год", False),
    ("1998", False),
])   
 
def test_is_empty(string, result):
    res = utils.is_empty(string)
    assert result == result

@pytest.mark.parametrize('lst, joiner, result', [
    (["р", "о", "м"], ".", "р.о.м"),
    (["Раз", "Два"], "-", "Раз-Два", ),
    (["к", "о", "т"], "", "кот" ),
    #Negative
    ([], None, ""),
    ([], "/", ""),
    ([], "cat", ""),
])  

def test_list_to_string(lst, joiner, result):
    if joiner == None:
        res = utils.list_to_string(lst)
    else:
        res = utils.list_to_string(lst, joiner)
    assert res == result    
# Write a function is_in that accepts two strings as
# arguments and returns True if either string occurs anywhere in the
# other, and False otherwise.

def is_in(string1, string2):
        if str(string1) in str(string2):
                print(str(string1) in str(string2))
        if str(string2) in str(string1):
                print(str(string2) in str(string1))
        else:
                return False

def test_is_in():
    # Normal cases
    assert is_in("hello", "hello world") == True
    assert is_in("world", "hello world") == True
    assert is_in("foo", "bar foo baz") == True
    
    # Edge cases
    assert is_in("", "hello") == True  # Empty string is in any string
    assert is_in("hello", "") == False  # Non-empty string cannot be in an empty string
    assert is_in("", "") == True  # Empty strings are equal
    
    # Strings with special characters
    assert is_in("!", "hello!") == True
    assert is_in("?", "hello") == False

    # Case sensitivity
    assert is_in("HELLO", "hello world") == False  # Case-sensitive check
    assert is_in("hello", "HELLO world") == False  # Case-sensitive check

    print("All tests passed!")
test_is_in()
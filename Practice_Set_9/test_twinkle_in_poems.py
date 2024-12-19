# WAP in Python to read the text contents from the file 'poems.txt' and find out whether the word 'twinkle' is present
# in the text file or not

def test_is_twinkle_present():
    
    with open("Practice_Set_9/poems.txt", "r") as f:
        text = f.read()
        
        assert 'Twinkle' in text
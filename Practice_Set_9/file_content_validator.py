class File_Content_Validator:
    
    def is_content_validated(self):
        
        with open("Practice_Set_9/og.txt", "r") as f:
            original_content = f.read()
            
        with open("Practice_Set_9/copy.txt", "r") as f:
            copied_content = f.read()
            
        if(original_content == copied_content):
            print("Both the file contents are exactly the same!")
        else:
            print("NOT same!")
            
if __name__ == "__main__":
    fcv = File_Content_Validator()
    fcv.is_content_validated()
from langchain.text_splitter import RecursiveCharacterTextSplitter
import re

class ChunkData:
    def __init__(self):
        print("Instantiated")
        # self.text_splitter = RecursiveCharacterTextSplitter(
        #     separators=["\n\n\n", "\n\n"],  # Prioritize splitting by paragraphs, then sentences
        #     chunk_size = 500,  # Maximum size of each chunk
        #     chunk_overlap = 0  # Overlap to maintain context between chunks
        # )

    # def chunk_text(self,file_name):
        
    #     with open(file_name,"r") as file:
    #         data = file.read()

    #     chunks = self.text_splitter.split_text(data)
    #     return chunks

    def remove_numbers_and_punctuation_from_list(self,data):
        print("In remove numbers and punctutations")
        # Remove leading numbers and punctuation
        cleaned_data = [re.sub(r'^\d+\.?\s*', '', item) for item in data]
        cleaned_data = [re.sub(r'^\d+\s+', '', item) for item in cleaned_data]
        # Remove all remaining punctuation
        cleaned_data = [re.sub(r'[^\w\s]', '', item) for item in cleaned_data]
        cleaned_list = [item for item in cleaned_data if item]
        return cleaned_list

    def chunk_for_books(self,data):
        print("In function")
        text =  re.sub(r'\b\d+\s*hours\b', '', data, flags=re.IGNORECASE)
        text =  re.sub(r'[()]', '', text)
        # This regex captures text between \n\n and the next \n
        pattern = r'(\n\n\n?)(.*?)(?=\n)'
        # Find all matches using re.DOTALL to capture multiline content
        matches = re.findall(pattern, text, re.DOTALL)
        result = []
        for line,title in matches:
            result.append(title)
        
        matches = self.remove_numbers_and_punctuation_from_list(result)
        return matches
    

    def chunk_for_video(self,data):
        text =  re.sub(r'\b\d+\s*hours\b', '', data, flags=re.IGNORECASE)
        text =  re.sub(r'[()]', '', text)
        # Split the data by newline and return the chunks
        chunks = data.split('\n')
        # Remove any empty strings if there are consecutive newlines
        chunks = self.remove_numbers_and_punctuation_from_list(chunks)
        return [chunk for chunk in chunks if chunk.strip()]
    

# with open("sample.txt","r") as file:
#     data = file.read()

# chunk_data = ChunkData()

# book_chunks = chunk_data.chunk_for_video(data)

# print(book_chunks)
    
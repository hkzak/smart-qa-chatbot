
from typing import Dict

import streamlit as st


@st.cache(allow_output_mutation=True)
def get_static_store() -> Dict:
    """This dictionary is initialized once and can be used to store the files uploaded"""
    return {}


def main():
    """Run this function to run the app"""
    static_store = get_static_store()

    st.info(__doc__)
    result = st.file_uploader("Upload", type="py")
    if result:
        # Process you file here
        value = result.getvalue()

        # And add it to the static_store if not already in
        if not value in static_store.values():
            static_store[result] = value
    else:
        static_store.clear()  # Hack to clear list if the user clears the cache and reloads the page
        st.info("Upload one or more `.py` files.")

    if st.button("Clear file list"):
        static_store.clear()
    if st.checkbox("Show file list?", True):
        st.write(list(static_store.keys()))
    if st.checkbox("Show content of files?"):
        for value in static_store.values():
            st.code(value)

#read different files
# docx_file = st.file_uploader("Upload File",type=['txt','docx','pdf'])
# 		if st.button("Process"):
# 			if docx_file is not None:
# 				file_details = {"Filename":docx_file.name,"FileType":docx_file.type,"FileSize":docx_file.size}
# 				st.write(file_details)
# 				# Check File Type
# 				if docx_file.type == "text/plain":
# 					# raw_text = docx_file.read() # read as bytes
# 					# st.write(raw_text)
# 					# st.text(raw_text) # fails
# 					st.text(str(docx_file.read(),"utf-8")) # empty
# 					raw_text = str(docx_file.read(),"utf-8") # works with st.text and st.write,used for futher processing
# 					# st.text(raw_text) # Works
# 					st.write(raw_text) # works
# 				elif docx_file.type == "application/pdf":
# 					# raw_text = read_pdf(docx_file)
# 					# st.write(raw_text)
# 					try:
# 						with pdfplumber.open(docx_file) as pdf:
# 						    page = pdf.pages[0]
# 						    st.write(page.extract_text())
# 					except:
# 						st.write("None")
					    
					
# 				elif docx_file.type == "application/vnd.openxmlformats-officedocument.wordprocessingml.document":
# 				# Use the right file processor ( Docx,Docx2Text,etc)
# 					raw_text = docx2txt.process(docx_file) # Parse in the uploadFile Class directory
# 					st.write(raw_text)


main()
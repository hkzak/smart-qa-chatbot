# smart-qa-chatbot
This is generative document extraction  Q&A chatbot

![image](https://user-images.githubusercontent.com/22933014/158051433-63a2cd44-0f9d-4911-8f7f-fd1c81213291.png)

In this project we are using Streamlit for the frontend and FastAPI for the backend.

For the machine learning Model we are using Haystack's pretrained model "Seq2SeqGenerator".

How it works:

First, we run the model and we are downloading the GOT training data and store its embeddings.
Second, we start the uvicorn API and load the stored embeddings.
Finally, we start the streamlit app and call the api endpoint to retrieve the asnwer

Code setup on windows only:

Requirements - Python 3.7 or higher versions

1-Clone this repo

cd to the root Dir and install the following:

2- Install haystack:
  git clone https://github.com/deepset-ai/haystack.git
  cd haystack
  pip install --upgrade pip
  pip install -e '.[all]' ## or 'all-gpu' for the GPU-enabled dependencies
  Fore more information about haystack visit this link:  https://github.com/deepset-ai/haystack
  
3- Install Streamlit:
  pip install streamlit
  or python -m pip install streamlit
  
4- start streamlit:
  python -m streamlit run app_ui.py   
  
5- start uvicorn server:
  python -m uvicorn app_api:app
  
  go to http://localhost:8501 and start asking questions about game of thrones
  ![image](https://user-images.githubusercontent.com/22933014/158054626-108a6881-e8fe-41af-956b-624a04ff251b.png)

6- if you want to use your own data or documents:

    a- go to haystack_model.py and comment the following line "s3_url = "https://s3.eu-central-1.amazonaws.com/deepset.ai-farm-qa/datasets/documents/wiki_gameofthrones_txt.zip"
    fetch_archive_from_http(url=s3_url, output_dir=doc_dir)"
    b- change line 28 ( doc_dir = "data/article_txt_got" ) to the path to your training data documents
    c- run "python haystack_model.py"
    d- restart the uvicorn server

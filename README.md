# smart-qa-chatbot
This is generative document extraction  Q&A chatbot

![image](https://user-images.githubusercontent.com/22933014/158051433-63a2cd44-0f9d-4911-8f7f-fd1c81213291.png)

In this project we are using Streamlit for the frontend and FastAPI for the backend.

For the machine learning Model we are using Haystack's pretrained model "Seq2SeqGenerator".

How it works:

First, we run the model and we are downloading the GOT training data and store its embeddings.
Second, we start the uvicorn API and load the stored embeddings.
Finally, we start the streamlit app and call the api endpoint to retrieve the asnwer

Code setup:


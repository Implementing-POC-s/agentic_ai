#  Following MS Reactor series and Python udemy couse for Learning.
![WhatsApp Image 2025-10-26 at 12 06 14_a7675507](https://github.com/user-attachments/assets/028f1f93-007d-48db-afed-8712ec2046f9)->OVERALL FLOW OF RAG PIPELINE IN BACKROUND.

# steps for RETRIEVAL phase->
 1.Take the user_query
 2.Create vector embeddings
 3.Do a similarity search,Along with the relavant chunks,we call the model and do the chatting bussiness.



# this is how vectors  are stored in a vector-db, here its QDRANT 
![WhatsApp Image 2025-10-26 at 06 35 36_7fa53627](https://github.com/user-attachments/assets/b0254684-ba7b-4f0e-a497-70725c003de1)

#this how chunks are created so the next paragraph should have a context of previous para,,ONLY and ONLY IFF its inside a CONTEXT WINDOW.
![WhatsApp Image 2025-10-26 at 01 44 46_eb2b9c21](https://github.com/user-attachments/assets/18d0efff-24c4-4e72-9eec-83e177d31fc9)



# RAG  is an AI framewok that combines the strengths of LLMs with external knowledge sources.

INDEXING PHASE
![WhatsApp Image 2025-10-25 at 17 09 13_1fbdc4a8](https://github.com/user-attachments/assets/716ea522-13b2-42fc-99d7-607d236314aa)



#RETRIEVAL PHASE
![WhatsApp Image 2025-10-25 at 17 20 38_99d81947](https://github.com/user-attachments/assets/143a9f43-33f4-4f0e-aac1-1cdcf65fd703)



#AGENT->LLM with TOOLS.

# EMBEDDINGS-> An embedding model is a type of machine learning model that transforms complex, high-dimensional data (like text, images, or audio) into simplified, numerical vector representations called embeddings.



#json.loads()->Converts a Json string toa python object.
#json.dumps-> Converts apython object to a JSON string.


# API authentication for OpenAI hosts:
![WhatsApp Image 2025-10-23 at 20 10 12_6b4016dc](https://github.com/user-attachments/assets/bf676b83-c5e0-427c-a01d-1adc30ee08f4)







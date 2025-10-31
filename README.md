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


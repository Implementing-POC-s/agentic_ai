from transformers import pipeline
pipe = pipeline("image-text-to-text",model="google/gemma-3-4b-it")

messages=[
    {
        "role":"user",
        "content":[
            {"type":"image","url":"https://encrypted-tbn3.gstatic.com/images?q=tbn:ANd9GcRkPdvuw4ook7ZavcJ3LZpawWUuhxXqQau1FontwoXxXsjJu7Vz"},
            {"type":"text","text":"what is the shape of it? "}
        ]
    },
]
pipe(text=messages)
               
from huggingface_hub import InferenceClient
import sys

client = InferenceClient(api_key="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")
br = True
while br:
    sys.stdout.write(": ")
    inp = ""
    while True:
        if (i1:=input()) == "q":
            break
        inp += i1
    if inp in ("exit", "bye", "bb", "ltr", "cyl"):
        break
    sys.stdout.write("...")
    response = client.chat.completions.create(
        model="Qwen/Qwen2.5-72B-Instruct",
        messages=[
            {"role": "system"},
            {"role": "user", "content": inp}
        ],
        max_tokens=1000,
        temperature=0.8,
        top_p=0.9
    )
    print(response.choices[0].message.content)

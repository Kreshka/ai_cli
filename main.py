from huggingface_hub import InferenceClient
import sys
lst = [104, 102, 95, 120, 71,
       111, 80, 118, 86, 99,
       104, 76, 70, 119, 108,
       121, 88, 102, 90, 118,
       89, 89, 71, 66, 77, 120,
       69, 74, 108, 71, 114,
       79, 82, 86, 98, 78, 117]
res = ""

for i in lst:
    res += chr(i)
client = InferenceClient(api_key=res)
br = True
while br:
    tokens = int(input("tokens: "))
    sys.stdout.write(": ")
    inp = ""
    while True:
        if (i1:=input()) == "q":
            break
        inp += i1
    if inp in ("exit", "bye", "bb", "ltr", "cyl"):
        break
    print("...")
    response = client.chat.completions.create(
        model="Qwen/Qwen2.5-72B-Instruct",
        messages=[
            {"role": "system"},
            {"role": "user", "content": inp}
        ],
        max_tokens=500,
        temperature=0.8,
        top_p=0.9
    )
    print(response.choices[0].message.content)

from rembg import remove
input_path="input.jpg"
output_path="output.png"

with open(input_path,"rb") as input_file:
    input_bytes=input_file.read()
    output_bytes=remove(input_bytes)

    with open(output_path,"wb") as output_file:
        output_file.write(output_bytes)
read=open("rdf_out","r")
lines=read.read()
words=lines.split()
final_text=""
write=open("rdf_out_3.txt","a")
for word in words:
    print(word)
    if "\\n" in word:
        write.write("\n")
    else:
        write.write(word)


print(final_text)

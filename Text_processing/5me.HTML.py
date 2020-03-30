title = input()
content = input()
comment = input()
print(f"<h1>\n    {title}\n</h1>\n<article>\n    {content}\n</article>")
while comment != "end of comments":
    print(f"<div>\n    {comment}\n</div>")
    comment = input()

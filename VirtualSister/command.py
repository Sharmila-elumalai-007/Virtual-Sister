import tkinter as tk

root = tk.Tk()
root.config(bg="#d8bcf7")
# specify size of window.
root.geometry("450x480")

# Create text widget and specify size.
T = tk.Text(root,bg="pink")

# Create label
l = tk.Label(root, text="COMMENTS FOR AI")
l.config(font=("Arial", 18))
l.config(fg="red")

Fact = """1. stop it
2. change my name to
3. change name
4. what do i have, do i have plans, am i busy on
5. wikipedia, let me tell
6. search
7. don't listen, stop listening
8. open youtube
9. open discord
10. open discord app
11. open terminal, open command prompt, open cmd
12. what is the time, what time is it, time please
13. what is today's date, today's date
14. sister, hello sister
15. thank you, thanks
16. say something,say anything
17. when was your project started, when you programmed,when you started
18. who made you, who created you
19. how were you developed,can i see your source code,show me a source code
20. tell me a joke, crack a joke
21. who is your brother
22. good morning
23. good night
24. open my inbox
25. open my sent mail
26. open youtube and search for
27. repeat my speech
28. close chrome
29. close task manager
30. delete
31. shutdown
32. restart my pc
33. record my voice
34. take a screenshot
35. exit
36. text
37. select all
38. close this window
39. open a new tab
40. open a new incognito window
41. copy
42. paste
43. undo
44. redo
45. save
46. back
47. go up
48. go to top
49. read
50. translate to
51. introduce yourself
52. translate
53. in
54. convert selected
55. i am sad
56. play
57. locate
58. where is
59. none
60. i know that
61. make a note, write this down,remember this"""
# Create button for next text.
#b1 = tk.Button(root, text="Next", )
# Create an Exit button.
b2 = tk.Button(root, text="Exit",
               command=root.destroy)

l.pack()
T.pack()
#b1.pack()
b2.pack()

# Insert The Fact.
T.insert(tk.END, Fact)
root.mainloop()
import tkinter as tk

window = tk.Tk()

frame = tk.Frame(window)

halfdose_needed = tk.StringVar()

top_label = tk.Label(frame, text="Dosage for Corrections")
top_label.pack()

output_label_text = tk.StringVar()
output_label = tk.Label(frame, textvariable = output_label_text)
# def click():
#     button_label_text.set(entry.get())
#
# button = tk.Button(frame, text="Click Me", command = click)
# button.pack()
# button_label.pack()
#
lbl_bg_input_text = tk.Label(frame, text = "Enter Current Blood Glucose:")
ety_bg_input = tk.Entry(frame, width=5)
ety_bg_input.insert(0, "150")
#entry.insert(0, "This is an entry")
lbl_bg_input_text.pack()
ety_bg_input.pack()

lbl_targetbg_input_text = tk.Label(frame, text = "What is your Target BG?")
ety_targetbg_input = tk.Entry(frame,width=5)
ety_targetbg_input.insert(0, "100")
lbl_targetbg_input_text.pack()
ety_targetbg_input.pack()

lbl_correction_input_text = tk.Label(frame, text = "What is your Correction Factor?")
ety_correction_input = tk.Entry(frame,width=5)
ety_correction_input.insert(0, "100")
lbl_correction_input_text.pack()
ety_correction_input.pack()



def calculate():
    try:
        bg = float(ety_bg_input.get())
        target_bg = float(ety_targetbg_input.get())
        correction = float(ety_correction_input.get())
        result = (bg - target_bg) / correction
        if halfdose_needed == "yes":
            print("hd")
            result = result / 2
        if result < 0:
            top = tk.Toplevel(window)
            top.geometry("100x100")
            top.title("Danger")
            lbl_wrong_input_text = tk.Label(top, text = "Do not dose\ndue to no\ninsulin needed")
            lbl_wrong_input_text.pack()
        ety_dosage_input.delete(0, tk.END)
        ety_dosage_input.insert(0, str(result))
    except:
        top = tk.Toplevel(window)
        top.geometry("100x100")
        top.title("Error")
        lbl_wrong_input_text = tk.Label(top, text = "Please enter\nnumerical value")
        lbl_wrong_input_text.pack()

lbl_halfdose_input_text = tk.Label(frame, text = "Do you need a half dose?")
check = tk.Checkbutton(frame, text="Yes", variable = halfdose_needed,
	    onvalue='yes', offvalue='no')
lbl_halfdose_input_text.pack()
check.pack()

btn_calcuate = tk.Button(frame, text="Calculate Dosage", command = calculate)
                        #(frame is parent, label, command runs a function)
btn_calcuate.pack()

lbl_dosage_input_text = tk.Label(frame, text = "Your dosage is:")
ety_dosage_input = tk.Entry(frame,width=5)
lbl_dosage_input_text.pack()
ety_dosage_input.pack()



frame.pack()
#
#
# frame2 = tk.Frame(window)
# sum = tk.StringVar(frame2, "Result", "sum")
#
#
# def button2_click():
#     x = int(entry1.get())
#     y = int(entry2.get())
#     sum.set(str(x + y))
#     entry3.delete(0, tk.END)
#     entry3.insert(0, sum.get())
#
#
#
#
# entry1 = tk.Entry(frame2, width=5)
# entry1.insert(0, "1")
# entry1.pack()
# entry2 = tk.Entry(frame2, width=5)
# entry2.insert(0, "2")
# entry2.pack()
#

# entry3.pack()
# entry3.insert(0, sum.get())
# button2.pack()
# frame2.pack()
window.mainloop()

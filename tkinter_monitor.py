import tkinter as tk
import psutil
import json

root = tk.Tk()

text_box = tk.Text(root, height=10, width=50, padx=15, pady=15)
text_box.grid(column=1, row=1)

def cpu_monitor():
    cpu_Percent = psutil.cpu_percent(1)
    cpu_Freq = psutil.cpu_freq()

    cpu_specs = {"cpu_percent": cpu_Percent, "cpu_freq": cpu_Freq}

    text_box.insert(1.0 ,cpu_specs)

def ram_monitor():
    ram_Free = psutil.virtual_memory()[4]
    ram_Total = psutil.virtual_memory()[0]

    ram_specs = {"Free_Ram": ram_Free, "Total Ram": ram_Total}

    text_box.insert(1.0 ,ram_specs)
  

def disk_monitor():
    disk_Free = psutil.disk_usage('/')[2]
    disk_Percent = psutil.disk_usage('/')[3]
    disk_Used = psutil.disk_usage('/')[1]

    disk_specs = {"Free Diskspace": disk_Free, "Diskspace used percentage": disk_Percent, "Used Diskspace": disk_Used}

    text_box.insert(1.0 ,disk_specs)

def save_file():
    if filename_Text is not None:
        FileName = (filename_Text.get("1.0","10.0")) + ".txt"
        save_Data = text_box.get('1.0','100.0')
        json_Data = json.dumps(save_Data)
        print(save_Data)
        with open(FileName, 'w') as outfile:
            outfile.write(save_Data)







canvas = tk.Canvas(root, width = 480, height= 640)
canvas.grid(columnspan = 3, rowspan=4 )

description = tk.Label(root, text="Click the buttons below to see the current status of your computer", font="Papyrus")
description.grid(column= 1, row = 0)



cpu_Button = tk.Button(root, text="CPU Usage", font="papyrus", command= cpu_monitor)
cpu_Button.grid(column=0, row=2)

ram_Button = tk.Button(root, text="RAM Usage", font="papyrus", command=ram_monitor)
ram_Button.grid(column=1, row=2)

disk_Button = tk.Button(root, text="Free Diskspace", font="papyrus", command=disk_monitor)
disk_Button.grid(column=2, row=2)

filename_Text = tk.Text(root, height=3, width=15)
filename_Text.grid(column=0, row=3)


save_Button = tk.Button(root, text="Save Data", font="papyrus", command= save_file)
save_Button.grid(column=1, row=3)





root.mainloop()

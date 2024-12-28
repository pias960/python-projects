from tkinter import *
import speedtest

# Function to check internet speed
def speed():
    try:
        test = speedtest.Speedtest()
        test.get_servers()
        test.get_best_server()
        download_speed = str(round(test.download() / (10**6), 2)) + " Mbps"
        upload_speed = str(round(test.upload() / (10**6), 2)) + " Mbps"
        down_score.config(text=download_speed)
        upload_score.config(text=upload_speed)
    except Exception as e:
        down_score.config(text="Error")
        upload_score.config(text="Error")
        print("Error:", e)

# GUI setup
root = Tk()
root.title('Internet Speed Checker')
root.geometry('500x500')
root.config(bg='blue')

# Labels
down_label = Label(root, text='Download Speed', font=('Times New Roman', 20, 'bold'), fg='black', bg='blue')
down_label.place(x=80, y=50, width=400, height=30)

down_score = Label(root, text='00 Mbps', font=('Times New Roman', 20, 'bold'), fg='black', bg='blue')
down_score.place(x=80, y=150, width=400, height=30)

upload_label = Label(root, text='Upload Speed', font=('Times New Roman', 20, 'bold'), fg='black', bg='blue')
upload_label.place(x=80, y=250, width=400, height=30)

upload_score = Label(root, text='00 Mbps', font=('Times New Roman', 20, 'bold'), fg='black', bg='blue')
upload_score.place(x=80, y=350, width=400, height=30)

# Button
btn = Button(root, text='Check Speed', command=speed, bg='green', fg='white', font=('Times New Roman', 15, 'bold'))
btn.place(x=80, y=450, height=40, width=400)

# Run the GUI
root.mainloop()

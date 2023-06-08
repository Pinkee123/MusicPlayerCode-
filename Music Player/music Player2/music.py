def mutemusic():
 global currentvol
 root.mutebutton.grid_remove()
 root.unmutebutton.grid()
 currentvol=mixer.music.get_volume()
 mixer.music.set_volume(0)
def unmutemusic():
 global currentvol
 root.unmutebutton.grid_remove()
 root.mutebutton.grid()
 mixer.music.set_volume(currentvol)
def resumemusic():
 root.resumebutton.grid_remove()
 root.pausebutton.grid()
 mixer.music.unpause()
 AudiostatusLabel.configure(text='Playing....')

def pausemusic():
 mixer.music.pause()
 root.pausebutton.grid_remove()
 root.resumebutton.grid()
 AudiostatusLabel.configure(text='Paused')
def volumeup():
 vol=mixer.music.get_volume()
 mixer.music.set_volume(vol+0.1)
def volumedown():
 vol = mixer.music.get_volume()
 mixer.music.set_volume(vol-0.1)


def musicurl():
 try:
  dd=filedialog.askopenfilename(initialdir='C:/Users/pinkee mishra/OneDrive/Desktop', title='Select audiofile',
                                filetype=(('MP3', '*.mp3'),('WAV', '*.wav')))

 except:
  dd=filedialog.askopenfilename(title='Select audiofile', filetype=(('MP3', '*.mp3'),('WAV', '*.wav')))
 audiotrack.set(dd)
def playmusic():
 ad=audiotrack.get()
 mixer.music.load(ad)
 mixer.music.play()
 AudiostatusLabel.configure(text='Playing.....')

def stopmusic():
 mixer.music.stop()
 AudiostatusLabel.configure(text='Stopped')
def createwidgets():
 #labels
 #image register
 global imbrowse, implay, impause, imvolumeup, imvolumedown
 global AudiostatusLabel
 implay=PhotoImage(file='speaker.png')
 impause=PhotoImage(file='stop.png')
 imbrowse=PhotoImage(file='browse1.png', height=60)
 imvolumeup=PhotoImage(file='volume-up.png')
 imvolumedown=PhotoImage(file='volume-down.png')
#change size of images
 imbrowse=imbrowse.subsample(2,2)
 implay=implay.subsample(2,2)
 impause=impause.subsample(2,2)
 imvolumeup=imvolumeup.subsample(2,2)
 imvolumedown=imvolumedown.subsample(2,2)
 Tracklabel=Label(root,text='select your fav audio:',background='lightskyblue', font=('arial', 16,'italic bold'))
 Tracklabel.grid(row=0, column=0, padx=20, pady=20)
 AudiostatusLabel=Label(root,text='',background='lightskyblue', font=('arial', 15,'italic bold'))
 AudiostatusLabel.grid(row=2, column=1)

 #entry box
 trackentry=Entry(root,font=('arial', 16,'italic bold'),width=35, textvariable=audiotrack)
 trackentry.grid(row=0, column=1, padx=20, pady=20)

 #buttons
 browsebutton=Button(root, text='Search',bg='red',font=('arial', 13,'italic bold'),width=20,bd=5,
                     activebackground='purple4', command=musicurl)
 browsebutton.grid(row=0, column=2,padx=20, pady=20 )
 playbutton=Button(root, text='Play',bg='yellow',font=('arial', 13,'italic bold'),width=20,bd=5,
                   activebackground='purple4', command=playmusic)
 playbutton.grid(row=1, column=0,padx=20, pady=20, )
 root.pausebutton=Button(root, text='Pause',bg='green2',font=('arial', 13,'italic bold'),width=20,bd=5,
 activebackground='purple4', command=pausemusic)
 root.pausebutton.grid(row=1, column=1,padx=20, pady=20)
 root.resumebutton = Button(root, text='Resume', bg='green2', font=('arial', 13, 'italic bold'), width=20, bd=5,
                      activebackground='purple4', command=resumemusic)
 root.resumebutton.grid(row=1, column=1, padx=20, pady=20)
 root.resumebutton.grid_remove()
 root.mutebutton=Button(root, text='Mute', width=10,bg='yellow',font=('arial', 13, 'italic bold'), activebackground='purple4',bd=5,command=mutemusic)
 root.mutebutton.grid(row=3, column=3, padx=0)
 root.unmutebutton = Button(root, text='Unmute', width=10, bg='yellow',font=('arial', 13, 'italic bold'), activebackground='purple4', bd=5,
                      command=unmutemusic      )
 root.unmutebutton.grid(row=3, column=3, padx=0)
 root.unmutebutton.grid_remove()
 volumeupbutton=Button(root, text='VolumeUp',bg='blue',font=('arial', 13,'italic bold'),width=20,bd=4,
                       activebackground='purple4', command=volumeup)
 volumeupbutton.grid(row=1, column=2,padx=20, pady=20 )
 stopbutton=Button(root, text='Stop',bg='red',font=('arial', 13,'italic bold'),width=20,bd=4,
                   activebackground='purple4', command=stopmusic)
 stopbutton.grid(row=2, column=0,padx=20, pady=20 )
 volumedownbutton=Button(root, text='VolumeDown',bg='blue',font=('arial', 13,'italic bold'),width=20,bd=4,
                         activebackground='purple4', command=volumedown)
 volumedownbutton.grid(row=2, column=2,padx=20, pady=20 )
 ########################################





#############################
from tkinter import *
from tkinter import filedialog
from pygame import  mixer
from tkinter.ttk import Progressbar
root=Tk()
root.geometry('1100x500+200+50')
root.title("Lets Play Music")
root.iconbitmap('music3.ico')
root.resizable(False,False)
root.configure(bg='lightskyblue')
audiotrack=StringVar()
currentvol=0
ss='Lets Play Music'
count=0
text=''
sliderLabel=Label(root,text=ss,bg='lightskyblue',font=('arial', 40,'italic bold'))
sliderLabel.grid(row=3, column=0,padx=20,pady=20,columnspan=3)
def IntroLabelTrick():
 global count, text
 if(count>=len(ss)):
  count=-1
  text=''
  sliderLabel.configure(text=text)
 else:
  text=text+ss[count]
  sliderLabel.configure(text=text)
 count+=1
 sliderLabel.after(200,IntroLabelTrick)

IntroLabelTrick()
mixer.init()
createwidgets()
root.mainloop()

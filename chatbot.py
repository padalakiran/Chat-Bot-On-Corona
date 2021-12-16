#chatbot on corona
#which create awairness about corona virus with added gui using tkinter
#main part is using if,elif,else parts

from tkinter import *   #importing library for tkinter window

import tkinter as tk

root=Tk()


root.geometry("675x425")  #giving geometry for tkinter window

def send():                   #giving and taking commands from bot using if and elif and else condition
    send="you=>"+e.get()
    txt.insert(END,"\n"+send)
    
    if(e.get()=="hello"):
        
        txt.insert(END,"\n"+"Bot=>hello")
        
    elif(e.get()=="hi"):

        txt.insert(END,"\n"+"Bot=>hi")
        
    elif(e.get()=="hi!,how are you?"):
        
        txt.insert(END,"\n"+"Bot=>fine and what about you?")
        
    elif(e.get()=="what is corona?"):
        
        txt.insert(END,"\n"+"Bot=>Coronaviruses are a group of RNA viruses that cause diseases in mammals and birds. In humans and birds, they cause respiratory tract infections that can range from mild to lethal.")

    elif(e.get()=="Explain Symptoms of corona?"):

        txt.insert(END,"\n"+"Bot=>Fever or chills, Cough,Shortness of breath or difficulty breathing,Fatigue,Muscle or body aches,Headache,New loss of taste or smell,Sore throat,Congestion or runny nose,Nausea or vomiting,Diarrhea")

    elif(e.get()=="suggest me precautions against coronavirus!"):

        txt.insert(END,"\n"+"Bot=>Avoid close contact with people who are sick. Maintain at least three feet distance between yourself and anyone who is coughing or sneezing.Avoid touching your eyes, nose, and mouth.Stay home when you are sick.")

    elif(e.get()=="please give me travel advice!"):

        txt.insert(END,"\n"+"Bot=>WHO continues to advise against the application of travel or trade restrictions to countries experiencing COVID-19 outbreaks.  It is prudent for travellers who are sick to delay or avoid travel to affected areas, in particular for elderly travellers and people with chronic diseases or underlying health conditions. “Affected areas” are considered those countries, provinces, territories or cities experiencing ongoing transmission of COVID-19, in contrast to areas reporting only imported cases.  𝗧𝗿𝗮𝘃𝗲𝗹𝗹𝗲𝗿𝘀 𝗿𝗲𝘁𝘂𝗿𝗻𝗶𝗻𝗴 𝗳𝗿𝗼𝗺 𝗮𝗳𝗳𝗲𝗰𝘁𝗲𝗱 𝗮𝗿𝗲𝗮𝘀 𝘀𝗵𝗼𝘂𝗹𝗱:🌡 Self-monitor for symptoms for 14 days and follow national protocols of receiving countries. Some countries may require returning travellers to enter quarantine.  🤒 If symptoms occur, such as fever, or cough or difficulty breathing, travellers are advised to contact local health care providers, preferably by phone, and inform them of their symptoms and their travel history")
        
    elif(e.get()=="Are antibiotics effective in preventing or treating COVID-19?"):
        
        txt.insert(END,"\n"+"Bot=>Antibiotics do not work against viruses; they only work on bacterial infections. COVID-19 is caused by a virus, so antibiotics do not work. Antibiotics should not be used as a means of prevention or treatment of COVID-19.In hospitals, physicians will sometimes use antibiotics to prevent or treat secondary bacterial infections which can be a complication of COVID-19 in severely ill patients. They should only be used as directed by a physician to treat a bacterial infection.")
        
    elif(e.get()=="What about rapid tests?"):

        txt.insert(END,"\n"+"Bot=> Samples are collected from the nose and/or throat with a swab. These tests are cheaper than PCR and will offer results more quickly, although they are generally less accurate. We are still learning about how well they perform and when to use them.")

    elif(e.get()=="What test should I get to see if I have COVID-19?"):

        txt.insert(END,"\n"+"Bot=>In most situations, a molecular test is used to detect SARS-CoV-2 and confirm COVID-19. Polymerase chain reaction (PCR) is the most commonly used molecular test. Samples are collected from the nose and/or throat with a swab. Molecular tests detect virus in the sample by amplifying viral genetic material to detectable levels. For this reason, a molecular test is used to confirm an active infection, usually within a few days of exposure and around the time that symptoms may begin. ")

    elif(e.get()=="When should I get a test for COVID-19?"):

        txt.insert(END,"\n"+"Bot=>Anyone with symptoms should be tested, wherever possible. People who do not have symptoms but have had close contact with someone who is, or may be, infected may also consider testing – check with your local health guidelines. While a person is waiting for test results, they should remain isolated from others. Where testing capacity is limited, tests should first be done for those at higher risk of infection, such as health workers, and those at higher risk of severe illness such as older people, especially those living in seniors’ residences or long-term care facilities.")

    elif(e.get()=="How long does it take to develop symptoms?"):

        txt.insert(END,"\n"+"Bot=>The time from exposure to COVID-19 to the moment when symptoms begin is, on average, 5-6 days and can range from 1-14 days")

    elif(e.get()=="What is the difference between isolation and quarantine?"):

        txt.insert(END,"\n"+"Bot=>Quarantine means restricting activities and/or separating people who are not ill but may have been exposed to COVID-19. The quarantine can take place in a designated facility or at home for 14 days.Isolation means separating people who are ill with symptoms of COVID-19 and/or have tested positive.")

    elif(e.get()=="how can i prevent from COVID19?"):

        txt.insert(END,"\n"+"Bot=>Wash your hands regularly with soap and water, or clean them with alcohol-based hand rub.Maintain at least six feet distance between you and people coughing or sneezing.Avoid touching your face.Cover your mouth and nose when coughing or sneezing.Stay home if you feel unwell.Refrain from smoking and other activities that weaken the lungs.Practice physical distancing by avoiding unnecessary travel and staying away from large groups of people.")

    elif(e.get()=="how can i track COVID19?"):

        txt.insert(END,"\n"+"Bot=>By arogya setu mobile app")

    elif(e.get()=="Thank you for awairing"):

        txt.insert(END,"\n"+"Bot=>Thats my pleasure")

    elif(e.get()=="Bye!"):

        txt.insert(END,"\n"+"Bot=>Ok Bye! stay safe stay at your home")
        
    else:
        txt.insert(END,"\n"+"Bot=>sorry i dont understand")
    e.delete(0,END)

txt=Text()

txt.grid(row=0,column=0,columnspan=3)

e=Entry(root,width=100,fg="green")#entry Box

e.grid(row=1,column=0) #position of entry box

send=Button(root,text="send",command=send,fg="green")  #send button
send.grid(row=1,column=1) #position of send button



exit_button = tk.Button(root,text="Exit",fg="red",command=quit)  #exit button
exit_button.grid(row=1,column=2) #position of exit button


root.title("CHATBOT")    #name of window


#root.iconbitmap(r'C:\Users\user\Desktop\all\corona_hxd_icon.ico') #icon for tkinter window

root.mainloop()  #end of main loop

#github:- @padalakiran

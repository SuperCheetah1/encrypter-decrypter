# #1 write a program to encrypt a string. e.g of one algorithm. For a given string "I like Golden Gate bridge" 
# can be encrypted as "AIB ClDiEkFeG HGIoJlKdLeMnN OGPaQtReS TbUrViWdXgYe", if the length of string is >26 you 
# can either recycle alphabet or use symbols to fill the interleave position.

#Can you come up with an algorithm similar to the above problem and encrypt a string. You can explain how your algorithm works. 
# You can add as many factors to make it complex. Remember if you encrypt in certain way, you can decrypt, else data will be lost.
#Importing random
import random
import streamlit as st
import pandas as pd
import datetime 
## str initialization

def encrypt_word(org_num, steps, drn, ramorset) :
    char = org_num
    mystr=""
    if ramorset == "set" :
        if drn == "right" :
            for s in char :
                i = ord(s)
                if drn == "right" :
                    i = i + steps
                    mystr+= chr(i)
            st.write(f"You encrypted '{org_num}' to '{mystr}'.")
        if drn == "left" :
            for s in char :
                i = ord(s)
                if drn == "left" :
                    i = i - steps
                    mystr+= chr(i)
            st.write(f"You encrypted '{org_num}' to '{mystr}'.")
    if ramorset == "random" :
        steps = random.randint(1,15)
        magictwoball = random.randint(1,2)
        if magictwoball == 1 :
            drn == "right"
        if magictwoball == 2 :
            drn == "left"
            if drn == "right" :
                for s in char :
                    i = ord(s)
                    if drn == "right" :
                        i = i + steps
                        mystr+= chr(i)
                st.write(f"You encrypted '{org_num}' to '{mystr}'.")
                st.write("The computer has used certain parameters to encrypt your code. These parameters will need to be used to decrypt your code:  ")
                st.write("Steps:  {0}".format(steps))
                st.write("Direction: {0}".format(drn))
            if drn == "left" :
                for s in char :
                    i = ord(s)
                    if drn == "left" :
                        i = i - steps
                        mystr+= chr(i)
                st.write(f"You encrypted '{org_num}' to '{mystr}'.")
                st.write("The computer has used certain parameters to encrypt your code. These parameters will need to be used to decrypt your code:  ")
                st.write("Steps:  {0}".format(steps))
                st.write("Direction: {0}".format(drn))



def decrypt_word(org_num, steps, drn) :
    char = org_num
    mystr=""
    if drn == "right" :
        for s in char :
            i = ord(s)
            if drn == "right" :
                i = i - steps
                mystr+= chr(i)
        st.write(f"You decrypted '{org_num}' to '{mystr}'.")
    if drn == "left" :
        for s in char :
            i = ord(s)
            if drn == "left" :
                i = i + steps
                mystr+= chr(i)
        st.write(f"You decrypted '{org_num}' to '{mystr}'.")

def main() :
    st.write("# The Encoder/Decoder")
    st.write("Welcome to Encoder/Decoder BETA. We hope you will enjoy this app we are giving you.")
    useroradmin = st.selectbox("Are you a user or an administrator?", ("", "I am a user", "I am an administrator/regulator"))
    if useroradmin == "I am an administrator/regulator" :
        password = st.text_input("Please type in the password", type="password")
        if password == "Administrator" :
            st.write("You are on the administrator account.")
            recreation = st.selectbox("What would you like to do today?", ("", "Do random stuff", "Manage Regulators"))
            if recreation == "Manage Regulators" :
                st.write("This is where you manage regulators.")
        elif password == "Regulator" :
            st.write("You are on the regulator account.")
            recreationreg = st.selectbox("What would you like to do today?", ("", "Do random stuff"))
            if recreationreg == "Do random stuff" :
                st.write("Let's do random stuff together")
    if useroradmin == "I am a user" :
        encodeordecode = st.selectbox("Would you like to encrypt a statement or decrypt a statement? Or would you like to what this app is?", ("", "Encrypt a message", "Decrypt a message", "What is this?"))
        if encodeordecode == "Encrypt a message" :
            encoderone = st.selectbox("Would you like to customize my encryption or would you like the computer to do it?", ("","Customize my encryption", "Let my computer do it"))
            if encoderone == "Customize my encryption" :
                firststep = st.selectbox("Please tell us how many steps you want:  ", ('','1','2','3','4','5','6','7','8','9','10','11','12','13','14','15'))
                secondstep = st.selectbox("Please tell us what direction you would like: ", ('','left', 'right'))
                finalstep = st.text_input("Please tell us what you would like to encrypt:  ")
                st.write("Please wait 1-3 seconds before pressing the button.")
                if st.button("Encrypt") :
                    if finalstep == "" or secondstep == "" or firststep == "" :
                        st.write("Please fill in all boxes for your request.")
                    else :
                        encrypt_word(finalstep, int(firststep), secondstep, "set")
            if encoderone == "Let my computer do it" :
                encoderword = st.text_input("Please tell us what you would like to encrypt:  ")
                st.write("Please wait 1-3 seconds before pressing the button.")
                if st.button("Encrypt") :
                    if encoderword == "" :
                        st.write("Please tell us what you would like to encrypt.")
                    else :
                        encrypt_word(encoderword, 0, "left", "random")
        if encodeordecode == "Decrypt a message" :
            defirststep = st.selectbox("Please tell us how many steps you entered for your encryption:  ", ('','1','2','3','4','5','6','7','8','9','10','11','12','13','14','15'))
            desecondstep = st.selectbox("Please tell us what direction you entered for your encryption:  ", ('','left','right'))
            definalstep = st.text_input("Please tell us what you would like to decrypt:  ")
            st.write("Please wait 1-3 seconds before pressing the button.")
            if st.button("Decrypt") :
                if definalstep == "" or defirststep == "" or desecondstep == "" :
                    st.write("Please fill in all the boxes for your request.")
                else :
                    decrypt_word(definalstep, int(defirststep), desecondstep)
        if encodeordecode == "What is this?" :
            st.write("Encryption is the method by which information is converted into secret code that hides the information's true meaning.(Credit: SearchSecurity)")
            st.write("The conversion of encrypted data into its original form is called decryption(Credit: The Economic Times)")
            st.write("This app helps you to encrypt messages that you don't want everybody to see. It also helps decode the messages that somebody has sent to you.")
            st.write("However, this app can only decode its own encryption. So, you will see two words that are crucial in both the encrypting and decrypting process of this app.")
            learnmore = st.selectbox("Find out about these two words and what they mean: ", ("","Steps", "Direction"))
            if learnmore == "Steps" :
                st.write("Steps are useful in encrypting and decrypting messages. Steps are the distance between one letter and the other.")
                st.write("For example, the steps between a and e are four. How? 'a' is the first letter of the alphabet, so 'a' is 1.")
                st.write("'e' is the fifth letter of the alphabet, so 'e' is 5. The difference, or the steps, in this app is 4. So there are 4 steps between a and e.")
            if learnmore == "Direction" :
                st.write("Directions help with which way the alphabet needs to go. Let's say the original letter is 'e'. If we go 4 steps to the 'right' of 'e', we will encrypt 'e' to 'a'.")
                st.write("However, if we go 4 steps to the 'left' of 'e', we will encrypt 'e' to 'i'. Directions can help maximize the amount of security in an encryption.")



websitepassword = st.text_input("Please enter the website password. This password was made for security reasons. As a result it may change frequently.", type="password")
if websitepassword == "SuperCheetah1" :
    main()


#encrypt_word('Anirudh is very ', 10, 'right')
#decrypt_word('', 10, 'left')



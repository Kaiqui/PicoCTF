# information

## Overview

Points: 10
Category: Forensics

## Description

Files can always be changed in a secret way. Can you find the flag?


## Approach

After downloading and opening the image I used [this](https://29a.ch/photo-forensics/#strings) site to find the strings inside the file that's where the string `cGljb0NURnt0aGVfbTN0YWRhdGFfMXNfbW9kaWZpZWR9` appears, where it was just put in this site [this](https://www.base64decode.org/) and the flag appeared

## Flag

picoCTF{the_m3tadata_1s_modified}
# Inductions

Hello and welcome to the official github repository for Project Kratos Inductions 2025! This repository is where you will be making your assignment submissions, and also learning how to use git.

### What is git?

Git is a software used to do "version control" and track changes in code. Github is where this code is hosted. [Watch this video](https://youtu.be/r8jQ9hVA2qs?si=RhdH97FD-Xc3-4q8) to learn more 

### Installation 

Follow this [link](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git) for instructions on how to install git on your system. (_do contact us if you face any issues_)

### Set Up

You will now need to setup your git, by configuring your username and email id, [check this out](https://docs.github.com/en/get-started/git-basics/set-up-git)

### Submission 

Clone this repository onto your systems using the following command 
```bash
git clone https://github.com/Pruthu-G/EC_Inductions.git
```
And you will find a folder named _EC_Inductions_ in the directory where you ran it. 

Now, create a branch with the name of the folling format : **<first_name>_<last_name>** 
```bash
git branch <first_name>_<last_name>
```
Then, switch to your designated branch (_do not mess with anyone elses branch **we will find out**_)

```bash
git checkout <first_name>_<last_name>
```

Now youre all set up! To add your files and commit them to your branch for the first time
```bash
git add .
git commit -m "enter meaningful message here"
git push -u origin <first_name>_<last_name>
```
After you have let git know your branch of choice using the ``` -u ``` tag, you can simply type ```git push``` for all further additions. 

---
>💡 Tip : **It is always good to make sure that you are in the current branch, use ```git branch``` to verify, always**
---






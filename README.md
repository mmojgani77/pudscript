# pudscript
Python useful daily Scripts

>Note : You have to install Python version 3

> After you did clone the project; you have to add **Scripts** folder path to environment variables.
> Then you can use command `app [Your Script folder name] [Parameters Seperated with spaces]` to run the app.

### For Example

When you run `app md5-make MyTextHere` command , the Output would be `72053983a3969b821150bbb367469d53`
or when you run `app` or `app --help` command it will show you all the commands you can use.

# Tasks to do
- [ ] Making help (manual) for all of Scripts 

       You just have to add manual.txt to all of Scripts folder and describes what Scripts do.
       The format of manual.txt could be anything but to be better use the following sample format and
       after that when you type `app man [Your Script folder name]` it will show you the content of
       manual.txt file placed in that folder:
<pre>
---- Summary ----

     This script will generate the md5 hash of your parameter

---- Command syntax ----

     app md5-make [Write your text here]

---- Example ----

     app md5-make "my text"

---- Description ----

     No description.
     
</pre>

- [ ] Writing and Adding new useful Scripts
- [ ] Improve the Structure of working

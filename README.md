# SMTP Mailer

Send personalised mails from your personal email to n-number of people from your terminal.

## Features

* Intentionally detailed names, so that the user would know to whom the e-mail has been sent.
  * The ```.csv``` file is read for e-mail and names of the contact. The ```.csv``` file uses it as a 2-D array.
  * Can be used with ```txt``` and other file formats too(With a minor code change).
  * Tested on Windows (Python 3.6).

## Instructions to send mails using smtp_mailer

* [smtp_mailer][1] basically needs a input source from where it can read the email address
    (which of course has video lectures).

  * Make a [virtual environment][3] for this project on your local machine and download ```smtplib``` using ```pip install smtplib``` or ```pip3 install smtplib``` (In case there are a number of python versions installed on your system).

  * Enter the details in the attributes:
    * ```password```    :  ```password``` of your mail address...it will not be visible while typing so                                         type and press enter 
    * ```sender_mail``` : ```email@domain.com``` 

  * Enter the ```Subject``` and ```body``` of the e-mail. You can decorate it using ```HTML``` tags.

  * Enter the location of the ```.csv``` file and configure the ```line``` and ```row``` as per your needs.

  * Run ```python mailer.py``` or ```python3 mailer.py``` in case you have more than one versions of python installed on your system.  
  
  * Voila! Mails must have triggered by now.
  
## Contributions

   If you want to contribute to this project, feel free to fork it and send a PR :)

## Contact  

  Shoot a mail at raj.tyagi2000@gmail.com
  
## Author

  [Shubham Tyagi][2]

[1]: https://github.com/shubham-tyagi/smtp_mailer
[2]: http://shubhamtyagi.me
[3]: https://www.pythonforbeginners.com/basics/how-to-use-python-virtualenv/

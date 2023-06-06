# Trendnet-switch-reboot-script
My first python code. Reboots a TRENDNET switch by using selenium and a headless chrome browser.
To install selenium package, open up python terminal and input "pip install selenium"
If there is an error when performing the above, open up command prompt on windows and change directory to python scripts folder by inputting the following
> cd C:\Users\Asus\AppData\Local\Programs\Python\Python311\Scripts

Once directory is changed, you can now input the command:
> pip install selenium

Python will now install selenium

This switch model is TPE-1020WS.
Things to edit before running script:
- IP address of switch
- login ID and password
As the code runs on headless chrome browser, it is not possible to see the process.
To view the code executed line by line in selenium, remove the following lines

options = webdriver.ChromeOptions()
options.add_argument('--headless')
options.add_argument('log-level=3')

Then, change this line

driver = webdriver.Chrome(service_log_path='NUL', options=options)

to

driver = webdriver.Chrome()

Do provide feedback as to how I can improve my code, I appreciate any kind of feedback!

from selenium import webdriver

from webdriver_manager.chrome import ChromeDriverManager
browser=webdriver.Chrome(ChromeDriverManager().install())

# browser = webdriver.Chrome(executable_path=(r'C:\Users\JyothishKumar\Chrome Driver\chromedriver'))
browser.get('https://www.google.com/')

#Automate searchkey
search_input = browser.find_element_by_name('q')
search_input.send_keys('Python tutorial')

# <input class="gLFyf gsfi" jsaction="paste:puy29d;" maxlength="2048" name="q" type="text" aria-autocomplete="both" aria-haspopup="false" autocapitalize="off" autocomplete="off" autocorrect="off" autofocus="" role="combobox" spellcheck="false" title="Search" value="" aria-label="Search" data-ved="0ahUKEwiI6M6ru9XzAhVMpYsKHSCYCR0Q39UDCAQ">
search_button = browser.find_element_by_css_selector('input[type="submit"]')
search_button.click()
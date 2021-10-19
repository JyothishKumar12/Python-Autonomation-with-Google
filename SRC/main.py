from selenium import webdriver

from webdriver_manager.chrome import ChromeDriverManager
browser=webdriver.Chrome(ChromeDriverManager().install())

# browser = webdriver.Chrome(executable_path=(r'C:\Users\JyothishKumar\Chrome Driver\chromedriver'))
browser.get('https://www.google.com/')
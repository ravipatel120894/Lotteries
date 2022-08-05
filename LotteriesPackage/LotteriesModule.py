import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

# chrome_driver = 'C:/chromedriver.exe'
# driver = webdriver.Chrome(executable_path="C:/chromedriver.exe")

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://www.thelott.com/")
driver.maximize_window()
time.sleep(2)
driver.find_element(By.TAG_NAME, 'h2').is_displayed()

print('Select your region below pop-up')
driver.find_element(By.XPATH, "//img[@class='jurisdiction-symbol au-target']").click()
time.sleep(2)
qld = driver.find_elements(By.XPATH, "//div[@class='header-title']")[0]
assert qld.text == 'You are currently playing in QLD.'
driver.find_element(By.XPATH, "//ux-dialog-body/div[2]/div[2]/img[1]").click()
time.sleep(2)
driver.find_element(By.XPATH, "//img[@class='jurisdiction-symbol au-target']").click()
time.sleep(2)
nsw = driver.find_elements(By.XPATH, "//div[@class='header-title']")[0]
assert nsw.text == 'You are currently playing in NSW.'
driver.find_element(By.XPATH, "//ux-dialog-body/div[6]/div[2]/img[1]").click()
time.sleep(2)
driver.find_element(By.XPATH, "//img[@class='jurisdiction-symbol au-target']").click()
time.sleep(2)
tas = driver.find_elements(By.XPATH, "//div[@class='header-title']")[0]
assert tas.text == 'You are currently playing in TAS.'
driver.find_element(By.XPATH, "//ux-dialog-body/div[4]/div[2]/img[1]").click()
time.sleep(3)

print('Test Find a store page')
driver.find_element(By.CLASS_NAME, 'store-text').click()
time.sleep(2)
driver.find_element(By.TAG_NAME, 'h1').is_displayed()
time.sleep(2)
driver.find_element(By.XPATH, "//button[normalize-space()='Search']").click()
driver.find_element(By.XPATH, "//span[@class='validation-error']").is_displayed()
driver.find_element(By.XPATH, "//input[@placeholder='Search by suburb or postcode']").send_keys('4000')
driver.find_element(By.XPATH, "//button[normalize-space()='Search']").click()
driver.implicitly_wait(10)
driver.find_element(By.XPATH, "//small[normalize-space()='Showing stores near:']").is_displayed()
time.sleep(2)
driver.find_element(By.XPATH,
                    "//span[contains(@class,'au-target medium-up-only')][normalize-space()='VIEW LIST']").click()
driver.implicitly_wait(10)
store = driver.find_elements(By.XPATH, "//div[@class='stores-found-count']")[0]
assert store.text == '70 stores found'
time.sleep(2)

print('Test Login page')
driver.find_element(By.XPATH, "//span[@class='text']").click()
driver.implicitly_wait(10)
driver.find_element(By.XPATH, "//span[normalize-space()='Welcome back! Ready to play?']").is_displayed()
time.sleep(2)
driver.find_element(By.XPATH, "//div[contains(text(),'Log in')]//*[name()='svg']").click()
driver.implicitly_wait(10)
#driver.find_element(By.XPATH, "//div[contains(@class,'_leftForm_njose_8')]//div[1]//div[1]//div[1]").is_displayed()
driver.find_element(By.XPATH, "//div[contains(text(),'Send code')]").click()
#driver.find_element(By.XPATH,
#                    "//div[contains(@class,'_oneTimePasswordForm_njose_29')]//div[1]//div[1]//div[1]").is_displayed()
driver.find_element(By.XPATH, "//h4[normalize-space()='Join']").click()
driver.implicitly_wait(10)
driver.find_element(By.XPATH, "//h1[1]").is_displayed()
time.sleep(2)

print('Test Cart page')
driver.find_element(By.XPATH, "//a[@class='au-target cart-container mouse-over-area']//*[name()='svg']").click()
time.sleep(2)
driver.find_element(By.XPATH, "//h1[normalize-space()='My Cart']").is_displayed()
driver.find_element(By.XPATH, "//a[@class='button play-all-games']").click()
time.sleep(2)
online = driver.find_elements(By.TAG_NAME, "h1")[0]
assert online.text == "Play Australia's official lotteries online"
driver.find_element(By.XPATH, "//a[@title='Lucky Lotteries Super Jackpot']").click()
time.sleep(1)
driver.find_element(By.XPATH, "//a[@title='Super 66']").click()
time.sleep(1)
driver.find_element(By.XPATH, "//button[@data-test-id='fixed-add-cart-button']").click()
time.sleep(2)
driver.find_element(By.XPATH, "//div[@class='header-logo-size default-logo-image']").click()
time.sleep(2)

print('Test Play powerball in NSW')
driver.find_element(By.XPATH, "//img[@class='jurisdiction-symbol au-target']").click()
time.sleep(2)
driver.find_element(By.XPATH, "//ux-dialog-body/div[2]/div[2]/img[1]").click()
time.sleep(3)
driver.find_element(By.ID, "playmenu").click()
time.sleep(1)
play = driver.find_elements(By.XPATH, "//h3[@id='playmenuheading']")[0]
assert play.text == 'Select a game to play'
driver.find_element(By.XPATH,
                    "//div[@class='play-all-games-container hide-for-xsmall-only hide-for-small-only']//a[@class='button small play-all-games'][normalize-space()='Play All Games']").click()
time.sleep(2)
online = driver.find_elements(By.TAG_NAME, "h1")[0]
assert online.text == "Play Australia's official lotteries online"
driver.find_element(By.XPATH, "//a[@title='Lucky Lotteries Super Jackpot']").click()
time.sleep(1)
driver.find_element(By.XPATH, "//a[@title='Mon & Wed Lotto']").click()
time.sleep(1)
driver.find_element(By.ID, "playmenu").click()
time.sleep(1)
driver.find_element(By.ID, "powerball-tile").click()
time.sleep(2)
powerball = driver.find_elements(By.XPATH, "//h1[normalize-space()='Play Powerball']")[0]
assert powerball.text == 'Play Powerball'
driver.find_element(By.XPATH, "//span[@class='au-target quickpick-title']").click()
time.sleep(1)
quickpick = driver.find_elements(By.XPATH, "//span[normalize-space()='Grab a QuickPick']")[0]
print(quickpick.text)
assert quickpick.text == 'Grab a QuickPick'
time.sleep(2)
driver.execute_script("window.scrollBy(0,500)", "")
time.sleep(2)
driver.find_element(By.XPATH,
                    "//body/div[@id='pagewrapper']/div[contains(@class,'content-wrapper')]/div[contains(@class,'container')]/div[contains(@class,'row')]/div[contains(@class,'columns xsmall-12')]/div[contains(@class,'purchase-app')]/section[contains(@class,'purchase-content')]/div[contains(@class,'au-target purchase-game-content')]/play-tabs[contains(@class,'au-target')]/section[contains(@class,'au-target play-tabs state-nsw powerball')]/loading-panel[contains(@class,'au-target')]/section[contains(@class,'au-target loading-panel')]/quickpick[contains(@class,'au-target')]/section[contains(@class,'au-target quickpick state-nsw')]/div[contains(@class,'bg quickpick-background-color-dark')]/div[contains(@class,'content')]/ul[contains(@class,'au-target powerhit-middle')]/li[2]/div[1]").click()
time.sleep(3)
driver.execute_script("window.scrollBy(0,-500)", "")
time.sleep(2)
driver.find_element(By.XPATH, "//span[@class='au-target subscribe-title']").click()
time.sleep(2)
sub = driver.find_elements(By.XPATH, "//span[@class='main-header']")[0]
assert sub.text == "Subscriptions"
time.sleep(2)
driver.find_element(By.XPATH, "//span[@class='au-target marked-entry-title']").click()
time.sleep(2)
driver.find_element(By.XPATH, "//span[normalize-space()='System']").click()
time.sleep(1)
driver.execute_script("window.scrollBy(0,700)", "")
select_system = Select(driver.find_element(By.XPATH, "//select[contains(@value.one-way,'state.selectedSystemOption')]"))
select_system.select_by_visible_text("System 10")
time.sleep(2)
driver.find_element(By.XPATH, "//span[contains(text(),'PowerHit')]").click()
time.sleep(1)
driver.execute_script("window.scrollBy(0,700)", "")
select_system = Select(
    driver.find_element(By.XPATH, "//select[contains(@value.one-way,'state.selectedPowerHitOption')]"))
select_system.select_by_visible_text("PowerHit System 10")
time.sleep(2)
driver.execute_script("window.scrollBy(0,-500)", "")
time.sleep(2)
driver.find_element(By.XPATH, "//span[normalize-space()='Standard']").click()
time.sleep(2)
driver.execute_script("window.scrollBy(0,700)", "")
select_power = Select(
    driver.find_element(By.XPATH, "//select[contains(@value.one-way,'state.selectedGameCountOption')]"))
select_power.select_by_visible_text("10 Games - $12.15")
driver.execute_script("window.scrollBy(0,500)", "")
time.sleep(2)
driver.find_element(By.XPATH,
                    "/html/body/div[1]/div[2]/div/div[3]/div[3]/div/section/div/play-tabs/section/loading-panel/section/marked-entry/section/div[5]/marked-entry-selections/section/div[1]/div[2]/button[1]/span").click()
time.sleep(2)
driver.find_element(By.XPATH,
                    "/html/body/div[1]/div[2]/div/div[3]/div[3]/div/section/div/play-tabs/section/loading-panel/section/marked-entry/section/div[5]/marked-entry-selections/section/div[1]/div[2]/button[2]/span").click()
time.sleep(2)
driver.find_element(By.XPATH,
                    "/html/body/div[1]/div[2]/div/div[3]/div[3]/div/section/div/play-tabs/section/loading-panel/section/marked-entry/section/div[5]/marked-entry-selections/section/div[1]/div[2]/button[1]/span").click()
time.sleep(2)
driver.find_element(By.XPATH, "//button[contains(@data-test-id,'fixed-add-cart-button')]").click()
time.sleep(2)
driver.find_element(By.XPATH, "//a[@class='au-target cart-container mouse-over-area']//*[name()='svg']").click()
time.sleep(2)
driver.find_element(By.XPATH, "//a[normalize-space()='Empty Cart']").click()
time.sleep(2)
empty = driver.find_elements(By.XPATH, "//h2[normalize-space()='Empty Cart']")[0]
assert empty.text == 'Empty Cart'
driver.find_element(By.XPATH, "//button[normalize-space()='Yes']").click()
time.sleep(2)

print('Test Play powerball in QLD')
driver.find_element(By.XPATH, "//img[@class='jurisdiction-symbol au-target']").click()
time.sleep(2)
driver.find_element(By.XPATH, "//ux-dialog-body/div[4]/div[2]/img[1]").click()
time.sleep(2)
driver.find_element(By.ID, "playmenu").click()
time.sleep(1)
play = driver.find_elements(By.XPATH, "//h3[@id='playmenuheading']")[0]
assert play.text == 'Select a game to play'
driver.find_element(By.XPATH,
                    "//div[@class='play-all-games-container hide-for-xsmall-only hide-for-small-only']//a[@class='button small play-all-games'][normalize-space()='Play All Games']").click()
time.sleep(2)
online = driver.find_elements(By.TAG_NAME, "h1")[0]
assert online.text == "Play Australia's official lotteries online"
driver.find_element(By.XPATH, "//a[@title='Lucky Lotteries Super Jackpot']").click()
time.sleep(1)
driver.find_element(By.XPATH, "//a[@title='Super 66']").click()
time.sleep(1)
driver.find_element(By.XPATH, "//button[@data-test-id='fixed-add-cart-button']").click()
time.sleep(2)
driver.find_element(By.ID, "playmenu").click()
time.sleep(1)
driver.find_element(By.ID, "powerball-tile").click()
time.sleep(2)
powerball = driver.find_elements(By.XPATH, "//h1[normalize-space()='Play Powerball']")[0]
assert powerball.text == 'Play Powerball'
driver.find_element(By.XPATH, "//span[@class='au-target quickpick-title']").click()
time.sleep(1)
quickpick = driver.find_elements(By.XPATH, "//span[normalize-space()='Grab a QuickPick']")[0]
print(quickpick.text)
assert quickpick.text == 'Grab a QuickPick'
time.sleep(2)
driver.execute_script("window.scrollBy(0,500)", "")
time.sleep(2)
driver.find_element(By.XPATH,
                    "//body/div[@id='pagewrapper']/div[contains(@class,'content-wrapper')]/div[contains(@class,'container')]/div[contains(@class,'row')]/div[contains(@class,'columns xsmall-12')]/div[contains(@class,'purchase-app')]/section[contains(@class,'purchase-content')]/div[contains(@class,'au-target purchase-game-content')]/play-tabs[contains(@class,'au-target')]/section[contains(@class,'au-target play-tabs state-qld powerball')]/loading-panel[contains(@class,'au-target')]/section[contains(@class,'au-target loading-panel')]/quickpick[contains(@class,'au-target')]/section[contains(@class,'au-target quickpick state-qld')]/div[contains(@class,'bg quickpick-background-color-dark')]/div[contains(@class,'content')]/ul[contains(@class,'au-target powerhit-middle')]/li[2]/div[1]").click()
time.sleep(3)
driver.execute_script("window.scrollBy(0,-500)", "")
time.sleep(2)
driver.find_element(By.XPATH, "//span[@class='au-target subscribe-title']").click()
time.sleep(2)
sub = driver.find_elements(By.XPATH, "//span[@class='main-header']")[0]
assert sub.text == "Subscriptions"
time.sleep(2)
driver.find_element(By.XPATH, "//span[@class='au-target marked-entry-title']").click()
time.sleep(2)
driver.find_element(By.XPATH, "//span[normalize-space()='System']").click()
time.sleep(1)
driver.execute_script("window.scrollBy(0,700)", "")
select_system = Select(driver.find_element(By.XPATH, "//select[contains(@value.one-way,'state.selectedSystemOption')]"))
select_system.select_by_visible_text("System 10")
time.sleep(3)
driver.find_element(By.XPATH, "//span[contains(text(),'PowerHit')]").click()
time.sleep(1)
driver.execute_script("window.scrollBy(0,700)", "")
select_system = Select(
    driver.find_element(By.XPATH, "//select[contains(@value.one-way,'state.selectedPowerHitOption')]"))
select_system.select_by_visible_text("PowerHit System 10")
time.sleep(2)
driver.execute_script("window.scrollBy(0,-500)", "")
time.sleep(2)
driver.find_element(By.XPATH, "//span[normalize-space()='Standard']").click()
time.sleep(2)
driver.execute_script("window.scrollBy(0,700)", "")
select_power = Select(
    driver.find_element(By.XPATH, "//select[contains(@value.one-way,'state.selectedGameCountOption')]"))
select_power.select_by_visible_text("10 Games - $12.15")
driver.execute_script("window.scrollBy(0,500)", "")
time.sleep(3)
driver.find_element(By.XPATH,
                    "/html/body/div[1]/div[2]/div/div[3]/div[3]/div/section/div/play-tabs/section/loading-panel/section/marked-entry/section/div[5]/marked-entry-selections/section/div[1]/div[2]/button[1]/span").click()
time.sleep(2)
driver.find_element(By.XPATH,
                    "/html/body/div[1]/div[2]/div/div[3]/div[3]/div/section/div/play-tabs/section/loading-panel/section/marked-entry/section/div[5]/marked-entry-selections/section/div[1]/div[2]/button[2]/span").click()
time.sleep(2)
driver.find_element(By.XPATH,
                    "/html/body/div[1]/div[2]/div/div[3]/div[3]/div/section/div/play-tabs/section/loading-panel/section/marked-entry/section/div[5]/marked-entry-selections/section/div[1]/div[2]/button[1]/span").click()
time.sleep(2)
driver.find_element(By.XPATH, "//button[contains(@data-test-id,'fixed-add-cart-button')]").click()
time.sleep(2)
driver.find_element(By.XPATH, "//a[@class='au-target cart-container mouse-over-area']//*[name()='svg']").click()
time.sleep(2)
driver.find_element(By.XPATH, "//a[normalize-space()='Empty Cart']").click()
time.sleep(2)
empty = driver.find_elements(By.XPATH, "//h2[normalize-space()='Empty Cart']")[0]
assert empty.text == 'Empty Cart'
driver.find_element(By.XPATH, "//button[normalize-space()='Yes']").click()
time.sleep(3)
driver.find_element(By.XPATH, "//a[@class='button play-all-games']").click()
time.sleep(2)
online = driver.find_elements(By.TAG_NAME, "h1")[0]
assert online.text == "Play Australia's official lotteries online"
driver.find_element(By.XPATH, "//a[@title='Lucky Lotteries Super Jackpot']").click()
time.sleep(1)
driver.find_element(By.XPATH, "//a[@title='Super 66']").click()
time.sleep(1)
driver.find_element(By.XPATH, "//button[@data-test-id='fixed-add-cart-button']").click()
time.sleep(2)
driver.find_element(By.XPATH, "//div[@class='header-logo-size default-logo-image']").click()
time.sleep(2)

print('Test Results page')
driver.find_element(By.XPATH, "//a[@id='resultsmenu']").click()
time.sleep(2)
result = driver.find_elements(By.XPATH, "//h3[@id='resultsmenuheading']")[0]
assert result.text == 'Select a game for latest results'
driver.find_element(By.XPATH,
                    "//div[@id='divResultMenu']//a[@class='xsmall-12 medium-3 columns powerball state-qld state-nsw state-act state-sa state-vic state-tas state-nt']").click()
time.sleep(2)
powerball = driver.find_elements(By.XPATH, "//h2[normalize-space()='Powerball Results']")[0]
assert powerball.text == 'Powerball Results'

print('Real Winners page')
driver.find_element(By.XPATH, "//div[@id='pagewrapper']//li[3]//a[1]").click()
driver.implicitly_wait(10)
real_winner = driver.find_elements(By.XPATH, "//h1[normalize-space()='Real winners']")[0]
assert real_winner.text == 'Real winners'
time.sleep(2)

print('Test More')
driver.find_element(By.XPATH, "//span[@id='moremenu']").click()
time.sleep(1)
driver.find_element(By.PARTIAL_LINK_TEXT, "Game Rules").click()
time.sleep(2)
rules = driver.find_elements(By.XPATH, "//h1[normalize-space()='Our Game Rules']")[0]
assert rules.text == 'Our Game Rules'
driver.find_element(By.XPATH, "//span[@id='moremenu']").click()
time.sleep(1)
driver.find_element(By.PARTIAL_LINK_TEXT, "Contact Us").click()
time.sleep(2)
contact_us = driver.find_elements(By.TAG_NAME, "h1")[0]
assert contact_us.text == "Need a hand? We're here to help!"
driver.find_element(By.XPATH, "//div[@class='header-logo-size default-logo-image']").click()
time.sleep(2)

print('Test Help center')
driver.find_element(By.XPATH, "//a[@class='helpCentreLink']").click()
driver.implicitly_wait(10)
articles = driver.find_elements(By.XPATH, "//h3[normalize-space()='Promoted articles']")[0]
assert articles.text == 'Promoted articles'
driver.find_element(By.XPATH, "//a[@title='Back to the Lott']").click()
driver.implicitly_wait(10)
time.sleep(2)
driver.find_element(By.XPATH, "//div[@class='header-logo-size default-logo-image']").click()
time.sleep(2)

print('Test Play Saturday Lotto in NSW')
driver.find_element(By.XPATH, "//img[@class='jurisdiction-symbol au-target']").click()
time.sleep(2)
driver.find_element(By.XPATH, "//ux-dialog-body/div[2]/div[2]/img[1]").click()
time.sleep(3)
driver.execute_script("window.scrollBy(0,800)", "")
driver.find_element(By.XPATH, "//li[@class='au-target tattslotto state-nsw']//div[@class='brand-circle-logo']").click()
time.sleep(1)
play_saturday = driver.find_elements(By.XPATH, "//h1[normalize-space()='Play Saturday Lotto']")[0]
assert play_saturday.text == 'Play Saturday Lotto'
driver.find_element(By.XPATH, "//span[@class='au-target quickpick-title']").click()
time.sleep(1)
quickpick = driver.find_elements(By.XPATH, "//span[normalize-space()='Grab a QuickPick']")[0]
print(quickpick.text)
assert quickpick.text == 'Grab a QuickPick'
time.sleep(2)
driver.execute_script("window.scrollBy(0,500)", "")
time.sleep(2)
driver.find_element(By.XPATH, "//body/div[@id='pagewrapper']/div[contains(@class,'content-wrapper')]/div[contains(@class,'container')]/div[contains(@class,'row')]/div[contains(@class,'columns xsmall-12')]/div[contains(@class,'purchase-app')]/section[contains(@class,'purchase-content')]/div[contains(@class,'au-target purchase-game-content')]/play-tabs[contains(@class,'au-target')]/section[contains(@class,'au-target play-tabs state-nsw tattslotto')]/loading-panel[contains(@class,'au-target')]/section[contains(@class,'au-target loading-panel')]/quickpick[contains(@class,'au-target')]/section[contains(@class,'au-target quickpick state-nsw')]/div[contains(@class,'bg quickpick-background-color-dark')]/div[contains(@class,'content')]/ul[contains(@class,'au-target')]/li[1]/div[1]").click()
time.sleep(3)
driver.find_element(By.XPATH,"//div[@class='au-target dialog-close-icon tattslotto']").click()
time.sleep(2)
driver.execute_script("window.scrollBy(0,-500)", "")
time.sleep(2)
driver.find_element(By.XPATH, "//span[@class='au-target subscribe-title']").click()
time.sleep(2)
sub = driver.find_elements(By.XPATH, "//span[@class='main-header']")[0]
assert sub.text == "Subscriptions"
time.sleep(2)
driver.find_element(By.XPATH, "//span[@class='au-target marked-entry-title']").click()
time.sleep(2)
driver.find_element(By.XPATH, "//span[normalize-space()='System']").click()
time.sleep(1)
driver.execute_script("window.scrollBy(0,700)", "")
select_system = Select(driver.find_element(By.XPATH, "//select[contains(@value.one-way,'state.selectedSystemOption')]"))
select_system.select_by_visible_text("System 10")
time.sleep(3)
driver.find_element(By.XPATH, "//span[normalize-space()='Standard']").click()
time.sleep(2)
driver.execute_script("window.scrollBy(0,700)", "")
select_power = Select(
    driver.find_element(By.XPATH, "//select[contains(@value.one-way,'state.selectedGameCountOption')]"))
select_power.select_by_visible_text("10 Games - $8.25")
driver.execute_script("window.scrollBy(0,500)", "")
time.sleep(2)
driver.find_element(By.XPATH,
                    "/html/body/div[1]/div[2]/div/div[3]/div[3]/div/section/div/play-tabs/section/loading-panel/section/marked-entry/section/div[5]/marked-entry-selections/section/div[1]/div[2]/button[1]/span").click()
time.sleep(2)
driver.find_element(By.XPATH,
                    "/html/body/div[1]/div[2]/div/div[3]/div[3]/div/section/div/play-tabs/section/loading-panel/section/marked-entry/section/div[5]/marked-entry-selections/section/div[1]/div[2]/button[2]/span").click()
time.sleep(2)
driver.find_element(By.XPATH,
                    "/html/body/div[1]/div[2]/div/div[3]/div[3]/div/section/div/play-tabs/section/loading-panel/section/marked-entry/section/div[5]/marked-entry-selections/section/div[1]/div[2]/button[1]/span").click()
time.sleep(2)
driver.find_element(By.XPATH, "//button[contains(@data-test-id,'fixed-add-cart-button')]").click()
time.sleep(2)
driver.find_element(By.XPATH, "//a[@class='au-target cart-container mouse-over-area']//*[name()='svg']").click()
time.sleep(2)
driver.find_element(By.XPATH, "//a[normalize-space()='Empty Cart']").click()
time.sleep(2)
empty = driver.find_elements(By.XPATH, "//h2[normalize-space()='Empty Cart']")[0]
assert empty.text == 'Empty Cart'
driver.find_element(By.XPATH, "//button[normalize-space()='Yes']").click()
time.sleep(2)
driver.find_element(By.XPATH, "//div[@class='header-logo-size default-logo-image']").click()
time.sleep(2)


print('Test Play Saturday Lotto in QLD')
driver.find_element(By.XPATH, "//img[@class='jurisdiction-symbol au-target']").click()
time.sleep(2)
driver.find_element(By.XPATH, "//ux-dialog-body/div[4]/div[2]/img[1]").click()
time.sleep(3)
driver.find_element(By.XPATH, "//li[@class='au-target tattslotto state-qld']//div[@class='brand-circle-logo']").click()
time.sleep(1)
play_saturday = driver.find_elements(By.XPATH, "//h1[normalize-space()='Play Saturday Gold Lotto']")[0]
assert play_saturday.text == 'Play Saturday Gold Lotto'
driver.find_element(By.XPATH, "//span[@class='au-target quickpick-title']").click()
time.sleep(1)
quickpick = driver.find_elements(By.XPATH, "//span[normalize-space()='Grab a QuickPick']")[0]
print(quickpick.text)
assert quickpick.text == 'Grab a QuickPick'
time.sleep(2)
driver.execute_script("window.scrollBy(0,500)", "")
time.sleep(2)
driver.find_element(By.XPATH,
                    "//body/div[@id='pagewrapper']/div[contains(@class,'content-wrapper')]/div[contains(@class,'container')]/div[contains(@class,'row')]/div[contains(@class,'columns xsmall-12')]/div[contains(@class,'purchase-app')]/section[contains(@class,'purchase-content')]/div[contains(@class,'au-target purchase-game-content')]/play-tabs[contains(@class,'au-target')]/section[contains(@class,'au-target play-tabs state-qld tattslotto')]/loading-panel[contains(@class,'au-target')]/section[contains(@class,'au-target loading-panel')]/quickpick[contains(@class,'au-target')]/section[contains(@class,'au-target quickpick state-qld')]/div[contains(@class,'bg quickpick-background-color-dark')]/div[contains(@class,'content')]/ul[contains(@class,'au-target')]/li[2]/div[1]").click()
time.sleep(3)
driver.execute_script("window.scrollBy(0,-500)", "")
time.sleep(2)
driver.find_element(By.XPATH,"//div[@class='au-target dialog-close-icon tattslotto']").click()
time.sleep(2)
driver.find_element(By.XPATH, "//span[@class='au-target subscribe-title']").click()
time.sleep(2)
sub = driver.find_elements(By.XPATH, "//span[@class='main-header']")[0]
assert sub.text == "Subscriptions"
time.sleep(2)
driver.find_element(By.XPATH, "//span[@class='au-target marked-entry-title']").click()
time.sleep(2)
driver.find_element(By.XPATH, "//span[normalize-space()='System']").click()
time.sleep(1)
driver.execute_script("window.scrollBy(0,700)", "")
select_system = Select(driver.find_element(By.XPATH, "//select[contains(@value.one-way,'state.selectedSystemOption')]"))
select_system.select_by_visible_text("System 10")
time.sleep(2)
driver.find_element(By.XPATH, "//span[normalize-space()='Standard']").click()
time.sleep(2)
driver.execute_script("window.scrollBy(0,700)", "")
select_power = Select(
    driver.find_element(By.XPATH, "//select[contains(@value.one-way,'state.selectedGameCountOption')]"))
select_power.select_by_visible_text("10 Games - $8.25")
driver.execute_script("window.scrollBy(0,500)", "")
time.sleep(2)
driver.find_element(By.XPATH,
                    "/html/body/div[1]/div[2]/div/div[3]/div[3]/div/section/div/play-tabs/section/loading-panel/section/marked-entry/section/div[5]/marked-entry-selections/section/div[1]/div[2]/button[1]/span").click()
time.sleep(2)
driver.find_element(By.XPATH,
                    "/html/body/div[1]/div[2]/div/div[3]/div[3]/div/section/div/play-tabs/section/loading-panel/section/marked-entry/section/div[5]/marked-entry-selections/section/div[1]/div[2]/button[2]/span").click()
time.sleep(2)
driver.find_element(By.XPATH,
                    "/html/body/div[1]/div[2]/div/div[3]/div[3]/div/section/div/play-tabs/section/loading-panel/section/marked-entry/section/div[5]/marked-entry-selections/section/div[1]/div[2]/button[1]/span").click()
time.sleep(2)
driver.find_element(By.XPATH, "//button[contains(@data-test-id,'fixed-add-cart-button')]").click()
time.sleep(2)
driver.find_element(By.XPATH, "//a[@class='au-target cart-container mouse-over-area']//*[name()='svg']").click()
time.sleep(2)
driver.find_element(By.XPATH, "//a[normalize-space()='Empty Cart']").click()
time.sleep(2)
empty = driver.find_elements(By.XPATH, "//h2[normalize-space()='Empty Cart']")[0]
assert empty.text == 'Empty Cart'
driver.find_element(By.XPATH, "//button[normalize-space()='Yes']").click()
time.sleep(2)
driver.find_element(By.XPATH, "//div[@class='header-logo-size default-logo-image']").click()
time.sleep(2)

driver.close()

# Things to do
# Calculate princes and verify total with cart page
# Make a base class for webdriver
# Verify and compare data with other regions
# If one test-case fail, other should be continued till end
# It should provide test case report in last
# Write script to take dynamic value in locators from 0 to n by using for loop
# Buy tickets after login

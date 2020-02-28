def test_opencart_0(cmdopt):
    driver, url = cmdopt
    driver.get(url)
    assert driver.find_element_by_id('logo').text == "Your Store"
    assert driver.find_element_by_xpath('//*[@id="top-links"]/ul/li[1]/span').text == "123456789"



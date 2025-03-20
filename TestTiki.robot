*** Settings ***
Library    Openbrowser.py
Library    SeleniumLibrary

*** Test Cases ***
Test Open Browser
    @{list} =    Create List    username    mail@abc.com    welcome
    ${browser}    openandwaitforpageload    https://roadmap.sh/qa    /html/body/div[1]/nav/ul/li[2]/a/span
    FOR    ${element}    IN    @{list}
        inputValue    /html/body/div[2]/div/astro-island/form/input[1]    ${element}

    END
    inputValue    /html/body/div[2]/div/astro-island/form/input[1]    username
    inputValue    /html/body/div[2]/div/astro-island/form/input[2]    mail@abc.com
    inputValue    /html/body/div[2]/div/astro-island/form/input[3]    welcome
    clickElementById    /html/body/div[2]/div/astro-island/form/button
    Sleep    5s
    closeBroserSession
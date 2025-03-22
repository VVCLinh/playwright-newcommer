*** Settings ***
Library    ../Openbrowser.py
Library    SeleniumLibrary
Resource    ../Initialize.robot

*** Keywords ***


Sign Up With New User
    [Arguments]    ${username}    ${email}    ${password}
    [Documentation]    Create an user using custom creds
    ${browser}    Openandwaitforpageload    https://roadmap.sh/signup
    ${element}    Loadyamlfile    ${ELEMENT_FILE}
    inputValue    ${element}[login_page][username]    ${username}
    inputValue    ${element}[login_page][email]    ${email}
    inputValue    ${element}[login_page][password]    ${password}
    clickElementByXpath    ${element}[login_page][button_submit]
    sleep   5s
    Validatetextinpage    Verify your email address

Login Page
    [Arguments]    ${username}    ${password}
    [Documentation]    Login to roadmap page
    ${browser}    Openandwaitforpageload    https://roadmap.sh/login
    ${element}    Loadyamlfile    ${ELEMENT_FILE}
    inputValue    ${element}[login_page][email]    ${mail}
    inputValue    ${element}[login_page][password]    ${password}
    clickElementByXpath    ${element}[login_page][login_button]
    checkelementvisible   ${element}[login_page][account_button]
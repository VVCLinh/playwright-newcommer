*** Settings ***
Library    Openbrowser.py
Library    SeleniumLibrary

*** Test Cases ***
Test Open Browser
    ${browser}    openandwaitforpageload    https://tiki.vn
    Sleep    5s
    closeBroserSession
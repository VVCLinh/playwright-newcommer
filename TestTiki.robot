*** Settings ***
Library    Openbrowser.py
Library    SeleniumLibrary
Resource    Keywork.robot
Resource    Initialize.robot

*** Test Cases ***
Test Open Browser
    [Tags]    Signup
    Sign Up With New User    ${user}    ${mail}    ${pass}
    Sleep    5s
    [Teardown]    closeBroserSession

Test Login
    [Tags]    Login
    Login Page    ${user}    ${pass}
    Sleep    5s
    [Teardown]    closeBroserSession



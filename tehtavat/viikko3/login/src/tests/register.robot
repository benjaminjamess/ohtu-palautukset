*** Settings ***
Resource  resource.robot
Suite Setup     Open And Configure Browser
Suite Teardown  Close Browser
Test Setup      Reset Application Create User And Go To Register Page

*** Test Cases ***

Register With Valid Username And Password
    Register User  newuser  validpass1
    Get Title  ==  Welcome to Ohtu Application!

Register With Too Short Username And Valid Password
    Register User  ab  validpass1
    Registration Should Fail With Message  Username must be at least 3 characters long

Register With Valid Username And Too Short Password
    Register User  newuser  short
    Registration Should Fail With Message  Password must be at least 8 characters long

Register With Username That Is Already In Use
    Register User  kalle  validpass1
    Registration Should Fail With Message  Username is already in use

Register With Password Containing Numbers
    Register User  newuser  kalle123
    Get Title  ==  Welcome to Ohtu Application!

Register With Password Containing Symbols
    Register User  newuser  kalle#abc
    Get Title  ==  Welcome to Ohtu Application!

Register With Password Containing Only Lowercase Letters
    Register User  newuser  kallekalle
    Registration Should Fail With Message  Password must contain at least one non-letter character

Register With Password Containing Only Uppercase And Lowercase Letters
    Register User  newuser  KalleKalle
    Registration Should Fail With Message  Password must contain at least one non-letter character

Register With Matching Password Confirmation
    Register User  newuser  kalle123
    Get Title  ==  Welcome to Ohtu Application!

Register With Mismatched Password Confirmation
    Register User With Password Confirmation  newuser  kalle123  different123
    Registration Should Fail With Message  Passwords do not match

*** Keywords ***
Register User
    [Arguments]  ${username}  ${password}
    Register User With Password Confirmation  ${username}  ${password}  ${password}

Register User With Password Confirmation
    [Arguments]  ${username}  ${password}  ${confirmation}
    Fill Text  id=username  ${username}
    Fill Secret  id=password  $password
    Fill Secret  id=password_confirmation  $confirmation
    Click  button >> text=Register

Registration Should Fail With Message
    [Arguments]  ${message}
    Register Page Should Be Open
    Get Text  body  *=  ${message}

Reset Application Create User And Go To Register Page
    Reset Application
    Create User  kalle  kalle123
    Go To  ${REGISTER_URL}

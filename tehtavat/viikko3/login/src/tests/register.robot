*** Settings ***
Resource  resource.robot
Suite Setup     Open And Configure Browser
Suite Teardown  Close Browser
Test Setup      Reset Application Create User And Go To Register Page

*** Test Cases ***

Register With Valid Username And Password
    Register User  newuser  validpass
    Get Title  ==  Welcome to Ohtu Application!

Register With Too Short Username And Valid Password
    Register User  ab  validpass
    Registration Should Fail With Message  Username must be at least 3 characters long

Register With Valid Username And Too Short Password
    Register User  newuser  short
    Registration Should Fail With Message  Password must be at least 8 characters long

Register With Username That Is Already In Use
    Register User  kalle  validpass
    Registration Should Fail With Message  Username is already in use

*** Keywords ***
Register User
    [Arguments]  ${username}  ${password}
    Fill Text  id=username  ${username}
    Fill Secret  id=password  $password
    Fill Secret  id=password_confirmation  $password
    Click  button >> text=Register

Registration Should Fail With Message
    [Arguments]  ${message}
    Register Page Should Be Open
    Get Text  body  *=  ${message}

Reset Application Create User And Go To Register Page
    Reset Application
    Create User  kalle  kalle123
    Go To  ${REGISTER_URL}

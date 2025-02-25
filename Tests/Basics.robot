*** Settings ***

Library                  Collections
Library                  String
Library                  Process
Library                  DateTime
Library                  OperatingSystem
Library                  SeleniumLibrary
# Resource                 ../Tests/Resources/keywords.resource
# Resource                 ../Tests/Resources/Suite_Setup.resource

*** Variables ***    
${URL}=                  https://parabank.parasoft.com/parabank/contact.htm
${BROWSER}=              Chrome
${NAME SURNAME}=         TestName TestSurname

*** Test Cases ***
TC1 -- Parabank
    Set Selenium Speed            1 second
    Open Browser                  ${URL}                                     ${BROWSER}
    Input Text                    //*[@id="name"]                            ${NAME SURNAME}
    Input Text                    //*[@id="email"]                           testEmail@testemail.test
    Input Text                    //*[@id="phone"]                           +111 222 333 444
    Input Text                    //*[@id="message"]                         Some random test text qwerty 533@ !?# (with details)
    Click Element                 //*[@value="Send to Customer Care"]
    Element Should Contain        rightPanel                                 Thank you ${NAME SURNAME}\nA Customer Care Representative will be contacting you.

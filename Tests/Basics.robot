*** Settings ***
Library     Collections
Library     String
Library     Process
Library     DateTime
Library     OperatingSystem
Library     SeleniumLibrary
Resource    Resources/keywords.resource
Resource    Resources/Suite_Setup.resource


*** Variables ***
${URL}=             https://parabank.parasoft.com/parabank/contact.htm
${BROWSER}=         Chrome
${NAME SURNAME}=    TestName TestSurname


*** Test Cases ***
#    this is a comment
TC1 -- Parabank -- Send message to customer care from contact form page    # this is a test case name
    Set Selenium Speed    1 second
    Open Browser    ${URL}    ${BROWSER}
    Input Text    //*[@id="name"]    ${NAME SURNAME}
    Input Text    //*[@id="email"]    testEmail@testemail.test
    Input Text    //*[@id="phone"]    +111 222 333 444
    Input Text    //*[@id="message"]    Some random test text qwerty 533@ !?# (with details)
    Click Element    //*[@id="contactForm"]/table/tbody/tr[5]/td[2]/input
    Element Should Contain
    ...    rightPanel
    ...    Thank you ${NAME SURNAME}\nA Customer Care Representative will be contacting you.

Feature: Verify Formy Website is valid

    Background: Common Steps
        Given Edge browser is Launched
        When Open Formy page

    Scenario: Check Formy Title
        Then Verify Formy Title is present
        And Close Browser

    Scenario: Fill in Formy with one user data
        Then Input Firstname "Allan" and Lastname "Belle"
        And Close Browser

    Scenario Outline: Fill in Formy with multiple user data
        Then Input multiple "<firstName>" and "<lastName>"
        And Close Browser

    Examples:
        |firstName|lastName|
        |Allan|Belle|
        |Charlie|Dean|
        |Ellie|Fann|